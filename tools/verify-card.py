# -*- coding: utf-8 -*-
"""verify-card.py —— 建卡后的统一核验与反馈报告。

一次跑完「结构 / 字族 / 落点 / 声母 / 释义 / 图 / 页面」，输出可直接交给
建卡 agent 自修的结构化报告，而不是只有一串计数。

用法：
    python tools/verify-card.py 兩                 # 单卡（部头）
    python tools/verify-card.py --bu 兩            # 部头 + 二级字根 + 族卡
    python tools/verify-card.py --bu 兩 --page     # 加页面核验（需 8099 服务）
    python tools/verify-card.py --bu 兩 --json .tmp-verify.json
    python tools/verify-card.py --cards-dir .tmp-pilot --file 緉.json
    python tools/verify-card.py --bu 兩 --expect .tmp-expect.json

--expect 是 `{字: 原稿整行}`，用于核对族卡「釋義」是否整行照录。
报告：人类可读表格 + `--json` 机器可读；有 error 时 exit 1。

反馈约定（给 agent 用）：
  - 每条 issue 有 code（稳定，可 grep）、severity、card、where、message、hint。
  - 修完只重跑自己那张：`verify-card.py <字>`；全部 error 清掉再交。
  - warn 不一定改，但要在交付说明里解释为什么不改。
"""
import argparse
import glob
import importlib.util
import io
import json
import os
import re
import struct
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CARDS = os.path.join(ROOT, "web", "public", "cards")
GLYPHS = os.path.join(ROOT, "web", "public", "glyphs")
PHOTOS = os.path.join(GLYPHS, "photos")

HAN = "\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff\U00020000-\U0002a6df"
HAN_RE = re.compile("[" + HAN + "]")
SM_RE = re.compile(r"^((?:[a-zA-Z]{1,2}|零)「[^」]+」(取「[^」]」：|不系：)|不取義：)")
INITIALS = ("zh", "ch", "sh")
SKIP_FILES = {"index.json", "alias-index.json", "variants.json"}
REQUIRED = {"benyi", "zizu", "shengmu", "suoshujuan"}
LV3_KEYS = ("shiyi", "shengmu", "suoshujuan")

ISSUES = []
CARDS_MAP = {}
GLYPH_INDEX = {}
PHOTO_INDEX = {}
CAPTIONS = {}
VARIANTS = {}


# ---------------------------------------------------------------- helpers
def iss(code, sev, card, where, msg, hint, evidence=""):
    ISSUES.append({
        "code": code, "severity": sev, "card": card, "where": where,
        "message": msg, "hint": hint, "evidence": str(evidence)[:160],
    })


def load(path):
    try:
        with io.open(path, encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return None


def norm(s):
    s = re.sub(r"\s+", "", s or "")
    s = s.replace("“", '"').replace("”", '"').replace("‘", "'").replace("’", "'")
    s = s.replace("：", ":").replace("，", ",")
    return s


PINYIN = "a-zA-Z\u0261āáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜüńňǹḿ"
HEAD_RE = re.compile(
    r"^[\u3400-\u9fff\U00020000-\U0002a6df]{1,4}"
    r"(?:[（(][^）)]*[）)])?"
    r"[\s、，,]*[%s]+(?:[\s、，,]+[%s]+)*[\s、，,：:]*" % (PINYIN, PINYIN))


def rowtail(t):
    t = (t or "").strip()
    m = HEAD_RE.match(t)
    if m:
        rest = t[m.end():]
        if rest:
            return rest
    cut = min([i for i in (t.find("《"), t.find("“"), t.find("「")) if 0 < i <= 12] or [0])
    if cut:
        return t[cut:]
    m2 = re.match(r"^[\u3400-\u9fff\U00020000-\U0002a6df]{1,4}[：:]?", t)
    return t[m2.end():] if m2 else t


def han_only(s):
    return "".join(HAN_RE.findall(s or ""))


def png_meta(path):
    """读 PNG 头，返回 (宽, 高, 位深, 颜色类型)；非 PNG/读不了返回 None。"""
    try:
        with open(path, "rb") as f:
            head = f.read(29)
    except OSError:
        return None
    if len(head) < 29 or head[:8] != b"\x89PNG\r\n\x1a\n":
        return None
    w, h = struct.unpack(">II", head[16:24])
    return w, h, head[24], head[25]


def looks_like_modern_glyph(path):
    """字形图疑似现代字/符号的启发式。

    两种信号取其一：
      A. 极小且 ≤2-bit（字体渲染的位图字，如 29×35、1-bit、240 B）；
      B. 文件 <350 B（纯线条图，扫描件极少这么小）。
    只用于 warn：古文字里也有极简的线条形，交人复核。
    """
    meta = png_meta(path)
    if not meta:
        return None
    w, h, bd, ct = meta
    size = os.path.getsize(path)
    if max(w, h) <= 40 and bd <= 2:
        return "仅 %d×%d、%d-bit、%d B" % (w, h, bd, size)
    if size < 350:
        return "仅 %d×%d、%d B" % (w, h, size)
    return None


def head_alias_chars(card):
    """head 括注里的汉字（不含本字）。"""
    m = re.search(r"[（(]([^）)]*)[）)]", str(card.get("head") or ""))
    if not m:
        return []
    me = card.get("char") or ""
    return [c for c in han_only(m.group(1)) if c != me]


def pinyin_initial(py):
    py = re.sub(r"[^a-zA-Z\u00c0-\u024f]", "", (py or "").split("、")[0].split(",")[0]).lower()
    if not py:
        return ""
    for i in INITIALS:
        if py.startswith(i):
            return i
    return py[0]


def any_pinyin_initial(py):
    out = set()
    for part in re.split(r"[、,，]", py or ""):
        ini = pinyin_initial(part)
        if ini:
            out.add(ini)
    return out


def load_luodian():
    p = os.path.join(ROOT, "tools", "check-luodian.py")
    spec = importlib.util.spec_from_file_location("check_luodian", p)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


LUO = load_luodian()


def load_all(cards_dir):
    global CARDS_MAP, GLYPH_INDEX, PHOTO_INDEX, CAPTIONS, VARIANTS
    CARDS_MAP = {}
    for fp in sorted(glob.glob(os.path.join(cards_dir, "*.json"))):
        name = os.path.basename(fp)
        if name in SKIP_FILES:
            continue
        d = load(fp)
        if isinstance(d, dict):
            ch = d.get("char") or name[:-5]
            CARDS_MAP[ch] = dict(d, _path=fp, _file=name)
    GLYPH_INDEX = load(os.path.join(GLYPHS, "index.json")) or {}
    PHOTO_INDEX = load(os.path.join(PHOTOS, "index.json")) or {}
    CAPTIONS = load(os.path.join(PHOTOS, "captions.json")) or {}
    VARIANTS = load(os.path.join(CARDS, "variants.json")) or {}


def sections(card):
    return [s for s in (card.get("sections") or []) if isinstance(s, dict)]


def sec(card, key):
    for s in sections(card):
        if s.get("key") == key:
            return s
    return None


def rows(card):
    out = []
    z = sec(card, "zizu")
    if not z:
        return out
    for gi, g in enumerate(z.get("groups") or []):
        title = g.get("title") or ""
        for ri, r in enumerate(g.get("rows") or []):
            out.append((gi, ri, title, r))
    return out


def is_ezi(title):
    return any(k in (title or "") for k in ("訛", "譌", "形近"))


# ---------------------------------------------------------------- scope
def scope_members(bu):
    """部头 + erji 链 + 字族成员（跳过讹字组、已并入别名的字）。"""
    if bu not in CARDS_MAP:
        return []
    head = CARDS_MAP[bu]
    out = [bu]
    links = []
    for s in sections(head):
        if s.get("key") == "erji":
            links += [x.get("ch") for x in (s.get("links") or []) if x.get("ch")]
    for ch in links:
        if ch in CARDS_MAP and ch not in out:
            out.append(ch)
    aliases = set(head.get("aliases") or [])
    for ch in member_map(bu):
        if ch in CARDS_MAP and ch not in out and ch not in aliases:
            out.append(ch)
    return out


def member_map(bu):
    """{族字: 父卡}，递归二级字根。"""
    out = {}
    queue = [bu]
    while queue:
        parent = queue.pop(0)
        card = CARDS_MAP.get(parent)
        if not card:
            continue
        links = []
        for s in sections(card):
            if s.get("key") == "erji":
                links += [x.get("ch") for x in (s.get("links") or []) if x.get("ch")]
        for ch in links:
            if ch in CARDS_MAP and ch not in out:
                out[ch] = parent
                queue.append(ch)
        for gi, ri, title, r in rows(card):
            if is_ezi(title) or not r:
                continue
            ch = str(r[0] or "").split("（")[0].split("(")[0].strip()
            if not ch or ch == parent or ch in links or ch in (card.get("aliases") or []):
                continue
            out.setdefault(ch, parent)
    return out


# ---------------------------------------------------------------- card checks
def check_shape(card, ch):
    for k in ("char", "head", "pinyin", "bus", "level"):
        if not card.get(k):
            iss("E003", "error", ch, "top", "缺字段 %s" % k, "补上；照邻居卡抄结构")
    if card.get("char") != ch:
        iss("E003", "error", ch, "char", "char=%r 与文件名 %s 不一致" % (card.get("char"), ch),
            "char 必须等于文件名（部名可以不同）")


def check_sections(card, ch):
    lv = card.get("level") or 3
    ss = sections(card)
    keys = [s.get("key") for s in ss]
    if len(keys) != len(set(keys)):
        dup = sorted({k for k in keys if keys.count(k) > 1})
        iss("E011", "error", ch, "sections", "栏重复 %s" % dup, "一栏只能出现一次")
    if lv == 3:
        if not keys or keys[0] != "shiyi":
            iss("E012", "error", ch, "sections", "族卡首栏应为 shiyi，实为 %s" % keys,
                "释义务必放第一栏")
        for k in LV3_KEYS:
            if k not in keys:
                iss("E010", "error", ch, "sections", "缺 %s 栏" % k, "族卡只有釋義/聲母擬態/所属卷")
        if "zizu" in keys or "zixing" in keys:
            iss("E013", "warn", ch, "sections", "族卡带 zizu/zixing", "确认它是三级字根，否则删栏")
    else:
        for k in REQUIRED:
            if k not in keys:
                iss("E010", "error", ch, "sections", "缺 %s 栏" % k,
                    "部头/二级字根至少要有 本義、字族衍義、聲母擬態、所属卷")
        order = [k for k in keys if k in
                 ("benyi", "erji", "zhuanyi", "bianzheng", "yinyuan", "shengmu",
                  "zizu", "zixing", "suoshujuan")]
        rank = {k: i for i, k in enumerate(
            ("benyi", "erji", "zhuanyi", "bianzheng", "yinyuan", "shengmu",
             "zizu", "zixing", "suoshujuan"))}
        if order != sorted(order, key=lambda k: rank[k]):
            iss("E010", "error", ch, "sections", "栏序不对：%s" % order,
                "固定 benyi→[erji]→zhuanyi→bianzheng→[yinyuan]→shengmu→zizu→zixing→suoshujuan（646 张卡的实际惯例）")


def check_lineage(card, ch, bu):
    lv = card.get("level") or 3
    if lv == 1:
        return
    parent = card.get("parent")
    if not parent:
        iss("E020", "error", ch, "parent", "缺 parent", "二级填部头，三级填所属字根")
        return
    if parent not in CARDS_MAP:
        iss("E020", "error", ch, "parent", "parent=%s 无卡" % parent, "先建父卡")
        return
    # 沿 parent 链上溯，能到部头即可
    cur, chain = parent, []
    while cur and cur not in chain and len(chain) < 8:
        chain.append(cur)
        if cur == bu:
            break
        pc = CARDS_MAP.get(cur)
        if not pc:
            break
        cur = pc.get("parent")
    if bu not in chain:
        iss("E020", "error", ch, "parent", "parent 链 %s 到不了部头 %s" % (chain, bu),
            "修正 parent；二级字根挂部头，族字挂字根")
    rc = card.get("rootChain")
    if rc:
        if not isinstance(rc, list) or len(rc) < 2 or rc[-1] != ch or rc[0] != bu:
            iss("E021", "warn", ch, "rootChain", "rootChain=%s 不像 [部头,…,本字]" % rc,
                "二级一般 [parent, self]；族字可不写")


def check_aliases(card, ch):
    aliases = list(card.get("aliases") or [])
    for c in head_alias_chars(card):
        if c not in aliases and c not in CARDS_MAP:
            iss("E030", "error", ch, "aliases", "head 括注字「%s」未入 aliases" % c,
                "括注异体入 aliases；已有独立卡的不入")
    for a in aliases:
        if a in CARDS_MAP and a != ch:
            iss("E031", "warn", ch, "aliases", "alias「%s」自己有卡，会抢注" % a,
                "已有独立条目的字不入 aliases")
    # 释义务必整行：把「字（异体）」里的异体也并进 aliases
    shi = (sec(card, "shiyi") or {}).get("text") or ""
    m = re.match("^([%s]+)\\s*[（(]([^）)]*)[）)]" % HAN, shi)
    if m:
        for c in han_only(m.group(2)):
            if c != ch and c not in aliases and c not in CARDS_MAP:
                iss("E030", "error", ch, "shiyi", "釋義首「字（异体）」的「%s」未入 aliases" % c,
                    "照 check-aliases.py 的规则补")


def check_zizu(card, ch):
    z = sec(card, "zizu")
    if not z:
        return
    groups = z.get("groups") or []
    if not groups:
        iss("E041", "error", ch, "zizu", "字族表为空", "至少一组；确实无族字才可省 zizu")
        return
    if len(groups) >= 2:
        for g in groups:
            t = g.get("title") or ""
            if not re.match(r"^[①②③④⑤⑥⑦⑧⑨]", t):
                iss("E045", "warn", ch, "zizu", "多组但组题无编号：%s" % t,
                    "两组以上组题要 ①②③（原稿没有就照原稿）")
    for gi, g in enumerate(groups):
        title = g.get("title") or ""
        if not title.strip():
            iss("E040", "error", ch, "zizu#%d" % gi, "组题为空", "组题照原稿录入")
        rs = g.get("rows") or []
        if not rs:
            iss("E041", "error", ch, "zizu#%d" % gi, "空组", "空组不收")
        for ri, r in enumerate(rs):
            where = "zizu#%d row%d" % (gi, ri + 1)
            if not isinstance(r, list) or len(r) != 4:
                iss("E042", "error", ch, where, "行不是四格：%r" % (r,), "字｜读音｜类属｜取义落点")
                continue
            label, py, cls, text = [str(x or "") for x in r]
            if not label.strip():
                iss("E044", "error", ch, where, "首格空", "填 字（异体）")
            if not cls.strip() or cls.strip() == "-":
                iss("E043", "error", ch, where, "类属空/为-", "取形旁；原稿「从X」优先")
            if not py.strip():
                iss("E043", "warn", ch, where, "读音空", "照原稿拼音")
            if is_ezi(title):
                if "——" in text:
                    iss("E081", "error", ch, where, "讹字组落点含「——」", "整行原文照录，不搭桥")
                continue
            if "——" not in text:
                if text.startswith("音譯字") or text.startswith("译音字"):
                    continue
                iss("E080", "warn", ch, where, "落点无「——」（专名/音译可无）", "有义理可释则搭桥；否则只录原文")
                continue
            head_part, bridge = text.split("——", 1)
            if (head_part.lstrip().startswith(("《", "「")) or "」" in head_part) \
                    and not head_part.rstrip().endswith(("」", "”")):
                iss("E082", "error", ch, where, "引文未以」收尾：%s" % head_part[-12:],
                    "引文用《》「」，不用半截引号")
            bridge = bridge.strip()
            for code in LUO.check(label, title, text, (sec(card, "shiyi") or {}).get("text") or ""):
                sev = "error"
                hint = "桥句 ≤12 字、不用因果连词、不复述原文/组题"
                if code.startswith("F4"):
                    hint = "删到 12 字以内，只留物象与本组义项的对应"
                elif code.startswith("F5"):
                    hint = "去掉因果/解释词，改成名词性短语"
                elif code.startswith("F6"):
                    hint = "别复述釋義原文，换一个角度点物性"
                elif code.startswith("F7"):
                    hint = "只有音译字能写借声；其余删掉"
                elif code.startswith("F8"):
                    hint = "别复述组题，写这一行自己的落点"
                elif code.startswith("F3"):
                    hint = "桥句去掉起首标点"
                iss(code.split("-")[0], sev, ch, where, "桥句 %s" % code, hint, text)


def check_shengmu(card, ch):
    s = sec(card, "shengmu")
    if not s:
        if (card.get("level") or 3) != 1:
            iss("E060", "error", ch, "shengmu", "缺声母拟态", "每张卡都要有声母拟态")
        return
    text = (s.get("text") or "").strip()
    if not SM_RE.match(text):
        iss("E060", "error", ch, "shengmu", "格式不合规：%s" % text[:40],
            "`<声母>「组名」取「某」：…（推）。` 或 `不系：…（照實）`")
        return
    m = re.match(r"^([a-zA-Z]{1,2}|零)「([^」]+)」", text)
    if not m:
        return
    ini, group = m.group(1).lower(), m.group(2)
    if "零聲母" in group:
        if ini != "y":
            iss("E061", "warn", ch, "shengmu", "零声母前缀是 %s 不是 y" % ini, "零声母统一写 y「零聲母」")
        return
    tm = re.search(r"取「([^」]?)」", text)
    if tm and tm.group(1) and tm.group(1) not in group:
        iss("E062", "error", ch, "shengmu", "取项「%s」不在组名「%s」里" % (tm.group(1), group),
            "只能取组名两字之一")
    py = card.get("pinyin") or ""
    inits = any_pinyin_initial(py)
    if inits and ini not in inits:
        iss("E061", "error", ch, "shengmu", "声母 %s 与读音 %s 的首字母不符" % (ini, py),
            "按今读首字母；z/c/s 归 zh/ch/sh；多音取与卡义相符的那一读")


def check_images(card, ch):
    g = GLYPH_INDEX.get("chars", {}).get(ch) or {}
    gimgs = (sec(card, "zixing") or {}).get("gimgs") or []
    for f in gimgs:
        p = os.path.join(GLYPHS, *str(f).split("/"))
        if not os.path.exists(p):
            iss("E050", "error", ch, "zixing", "字形文件不存在：%s" % f, "补图或改 index")
    files = g.get("files") or []
    if gimgs and files and len(gimgs) != len(files):
        iss("E051", "error", ch, "zixing", "卡里 %d 图，glyphs/index 记 %d 图" % (len(gimgs), len(files)),
            "以 index 为准重写 gimgs")
    if files and not gimgs and (card.get("level") or 3) <= 2:
        iss("E051", "warn", ch, "zixing", "index 有 %d 图，卡里 gimgs 空" % len(files),
            "部头/二级补 gimgs；族卡由 index 自动出图，可不补")
    # 字形图本身是否像现代字（极小位图/纯线条小文件）
    seen = []
    for f in list(gimgs) + list(files):
        if f and f not in seen:
            seen.append(f)
    for f in seen:
        p = os.path.join(GLYPHS, *str(f).split("/"))
        if not os.path.exists(p):
            continue
        why = looks_like_modern_glyph(p)
        if why:
            iss("E056", "warn", ch, "zixing",
                "字形图疑为现代字/符号（%s）：%s" % (why, f),
                "确认原图；若是简化字/现代字，移到 glyphs/chars/<小写hex>.png 补字图索引，"
                "并从 glyphs/index 的 files 与卡 gimgs 移除", f)
    # 句中形
    for s in sections(card):
        gdir = s.get("gdir") or ""
        txt = "\n".join([s.get("text") or ""] + [str(x) for x in (s.get("paras") or [])])
        for m in re.finditer(r"\{\{([^}]+)\}\}", txt):
            rel = (gdir + "/" + m.group(1)) if gdir else m.group(1)
            p = os.path.join(GLYPHS, *rel.split("/"))
            if not os.path.exists(p):
                iss("E052", "error", ch, "inline", "占位符指向的文件不存在：%s" % rel,
                    "检查 gdir 与 {{栏/NN.png}} 是否对得上")
    # 插图
    ph = card.get("photos") or []
    top = (GLYPH_INDEX.get("photos") or {}).get(ch) or []
    for p in ph:
        f = p.get("file") if isinstance(p, dict) else p
        if not f:
            continue
        if not os.path.exists(os.path.join(PHOTOS, ch, os.path.basename(str(f)))):
            iss("E053", "error", ch, "photos", "插图文件不存在：%s" % f, "补文件或删条目")
    for p in top:
        f = (p.get("file") if isinstance(p, dict) else p) or ""
        if f and not str(f).startswith("photos/"):
            iss("E055", "error", ch, "glyphs/index photos", "顶层 photos 必须写全路径 photos/%s/…" % ch,
                "写 01.jpg 会 404")
    if ph and top and len(ph) != len(top):
        iss("E054", "error", ch, "photos", "卡里 %d 图，index 顶层 %d 图" % (len(ph), len(top)),
            "两处同步")


def check_shiyi(card, ch, expect):
    if (card.get("level") or 3) != 3:
        return
    s = sec(card, "shiyi")
    if not s:
        return
    t = (s.get("text") or "").strip()
    if not t:
        iss("E014", "error", ch, "shiyi", "釋義为空", "整行原稿不能空；原稿没有就补查，不能留空")
        return
    if re.match(r"^%s[（(]?[^《“「]{0,8}[a-zA-Zāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜüńňǹḿ]"
                % re.escape(ch), t):
        iss("E071", "warn", ch, "shiyi", "釋義带字头+拼音：%s…" % t[:16],
            "页头已显示字与音，釋義从《/「 处开始；否则页面重复")
    line = (expect or {}).get(ch)
    if not line:
        return
    def cmp_norm(x):
        # 句内形占位符与 txt 缓存的 [图] 都是图，不是文字：比对时剥掉
        x = re.sub(r"\{\{[^{}]*\}\}", "", x or "")
        x = x.replace("[图]", "")
        return norm(x)

    shi = cmp_norm(t)
    tail = cmp_norm(rowtail(str(line)))
    if shi != tail:
        iss("E070", "error", ch, "shiyi", "釋義不是原稿整行",
            "从《/「 处开始整行照录，只剥字头与拼音", "card=%s | orig=%s" % (shi[:40], tail[:40]))


# ---------------------------------------------------------------- page checks
def http_get(url, timeout=15):
    req = urllib.request.Request(url, headers={"User-Agent": "verify-card/1"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.status, r.read()


def check_page(card, ch, base):
    url = base.rstrip("/") + "/card/" + urllib.parse.quote(ch)
    try:
        status, body = http_get(url)
    except urllib.error.HTTPError as e:
        iss("E090", "error", ch, "page", "页面 HTTP %s" % e.code, "检查卡文件与服务")
        return
    except Exception as e:
        iss("E090", "error", ch, "page", "页面取不到：%s" % type(e).__name__, "确认 8099 服务在跑")
        return
    html = body.decode("utf-8", "replace")
    figs = len(re.findall(r"<figcaption", html))
    g = GLYPH_INDEX.get("chars", {}).get(ch) or {}
    exp = len(g.get("files") or []) + len((GLYPH_INDEX.get("photos") or {}).get(ch) or [])
    for e in (g.get("extra") or []):
        c2 = e.get("char") if isinstance(e, dict) else e
        g2 = GLYPH_INDEX.get("chars", {}).get(c2) or {}
        exp += len(g2.get("files") or [])
    for s in sections(card):
        exp += len(s.get("cimgs") or [])
    if figs != exp:
        iss("E091", "error", ch, "page", "图注 %d 个，应为 %d（字形+参证+插图）" % (figs, exp),
            "多/少图通常是 glyphs/index 与卡不一致")
    if "{{" in html:
        iss("E092", "error", ch, "page", "页面有残留 {{ 占位符", "补 gdir 或改占位符")
    srcs = []
    for m in re.finditer(r'src="(/glyphs/[^"?]+)', html):
        u = m.group(1)
        if u not in srcs:
            srcs.append(u)
    for u in srcs[:8]:
        try:
            st, _ = http_get(base.rstrip("/") + u)
            if st != 200:
                iss("E093", "error", ch, "page", "图片 %s HTTP %s" % (u, st), "补图")
        except Exception:
            iss("E093", "error", ch, "page", "图片 %s 取不到" % u, "补图")


def check_alias_pages(card, ch, base):
    for a in card.get("aliases") or []:
        url = base.rstrip("/") + "/card/" + urllib.parse.quote(a)
        try:
            st, _ = http_get(url)
            if st != 200:
                iss("E094", "warn", ch, "alias", "/card/%s HTTP %s" % (a, st), "检查 alias-index")
        except Exception:
            iss("E094", "warn", ch, "alias", "/card/%s 取不到" % a, "检查 alias-index")


# ---------------------------------------------------------------- main
def verify(chars, bu, cards_dir, expect, page, base, do_alias_pages, overrides=None):
    load_all(cards_dir)
    for _ch, _card in (overrides or {}).items():
        CARDS_MAP[_ch] = _card
    if bu:
        if bu not in CARDS_MAP:
            iss("E001", "error", bu, "file", "部头卡 %s.json 不存在" % bu, "先写部头卡")
            return []
        chars = scope_members(bu)
    chars = [c for c in chars if c]
    for ch in chars:
        card = CARDS_MAP.get(ch)
        if not card:
            iss("E001", "error", ch, "file", "%s.json 不存在" % ch, "缺卡")
            continue
        check_shape(card, ch)
        check_sections(card, ch)
        if bu:
            check_lineage(card, ch, bu)
        check_aliases(card, ch)
        check_zizu(card, ch)
        check_shengmu(card, ch)
        check_images(card, ch)
        check_shiyi(card, ch, expect)
        if page:
            check_page(card, ch, base)
            if do_alias_pages:
                check_alias_pages(card, ch, base)
    return chars


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("chars", nargs="*")
    ap.add_argument("--bu")
    ap.add_argument("--cards-dir", default=CARDS)
    ap.add_argument("--file", action="append", default=[], help="只验某个卡文件（试跑用）")
    ap.add_argument("--expect")
    ap.add_argument("--page", action="store_true")
    ap.add_argument("--base", default="http://127.0.0.1:8099")
    ap.add_argument("--alias-pages", action="store_true")
    ap.add_argument("--json")
    ap.add_argument("--max", type=int, default=40)
    args = ap.parse_args()

    expect = load(args.expect) if args.expect else {}
    if args.expect and expect is None:
        ap.error("--expect 文件读不了：%s（不会静默跳过释义核对）" % args.expect)
    chars = list(args.chars)
    overrides = {}
    for f in args.file:
        p = f if os.path.exists(f) else os.path.join(args.cards_dir, os.path.basename(f))
        d = load(p)
        if isinstance(d, dict) and d.get("char"):
            chars.append(d["char"])
            overrides[d["char"]] = d
        else:
            ap.error("读不出卡：%s" % f)
    if not chars and not args.bu:
        ap.error("给字、--bu 或 --file")

    verify(chars, args.bu, args.cards_dir, expect, args.page, args.base,
           args.alias_pages, overrides)

    order = {"error": 0, "warn": 1}
    issues = sorted(ISSUES, key=lambda x: (order.get(x["severity"], 2), x["code"], x["card"]))
    errs = [x for x in issues if x["severity"] == "error"]
    warns = [x for x in issues if x["severity"] == "warn"]

    scope = ("部 " + args.bu) if args.bu else ("%d 张卡" % len(set(chars)))
    print("verify %s · %s" % (scope, datetime.now().strftime("%Y-%m-%d %H:%M")))
    shown = 0
    last = None
    for x in issues:
        if shown >= args.max:
            print("  … 还有 %d 条，见 --json" % (len(issues) - shown))
            break
        if x["card"] != last:
            print("[%s]" % x["card"])
            last = x["card"]
        print("  %-5s %s %s: %s" % (x["severity"].upper(), x["code"], x["where"], x["message"]))
        print("        → %s" % x["hint"])
        if x["evidence"]:
            print("        证据: %s" % x["evidence"])
        shown += 1
    print("RESULT %s · error %d · warn %d" % ("FAIL" if errs else "PASS", len(errs), len(warns)))

    if args.json:
        report = {
            "tool": "verify-card", "version": 1,
            "generated": datetime.now().isoformat(timespec="seconds"),
            "scope": {"bu": args.bu, "cards": len(set(chars))},
            "verdict": "fail" if errs else "pass",
            "counts": {"error": len(errs), "warn": len(warns)},
            "issues": issues,
        }
        with io.open(args.json, "w", encoding="utf-8", newline="\n") as f:
            json.dump(report, f, ensure_ascii=False, indent=1)
            f.write("\n")
        print("json → %s" % args.json)
    sys.exit(1 if errs else 0)


if __name__ == "__main__":
    main()
