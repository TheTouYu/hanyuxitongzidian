# -*- coding: utf-8 -*-
"""make-charmap.py —— 从卷的纯文本缓存里，为一批族字抓原稿整行，供 check-shiyi.py。

用法：
    python tools/make-charmap.py 兩 㒼            # 指定字
    python tools/make-charmap.py --bu 兩          # 该部所有三级族字
    python tools/make-charmap.py --bu 兩 --txt "web/.cache/txt/卷五十四  网.txt"

输出 `.tmp-charmap.json`：`{字: {"txt": "原稿整行"}}`；跑完 check-shiyi 后可删。

抓行规则：行首就是该字，且字后紧跟（异体）/拼音/冒号；同一字多行时优先取带《》书证的那行。
"""
import argparse
import glob
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CARDS = os.path.join(ROOT, "web", "public", "cards")
DEFAULT_TXT = os.path.join(ROOT, "web", ".cache", "txt", "卷五十四  网.txt")

HAN = "\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff\U00020000-\U0002a6df"
PINYIN = "a-zA-Z\u0261āáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜüńňǹḿ"
START_RE = re.compile(r"^[%s]{1,4}" % HAN)
NEXT_RE = re.compile(r"^[（(：:%s]" % PINYIN)


def load(p):
    with io.open(p, encoding="utf-8") as f:
        return json.load(f)


def members_of(bu):
    """该部所有 level3 族字（沿 parent 链）。"""
    cards = {}
    for fp in glob.glob(os.path.join(CARDS, "*.json")):
        name = os.path.basename(fp)
        if name in ("index.json", "alias-index.json", "variants.json"):
            continue
        try:
            d = load(fp)
        except Exception:
            continue
        if isinstance(d, dict) and d.get("char"):
            cards[d["char"]] = d
    out = []
    for ch, d in cards.items():
        if d.get("level") != 3:
            continue
        cur, chain = d.get("parent"), []
        while cur and cur not in chain and len(chain) < 8:
            chain.append(cur)
            if cur == bu:
                out.append(ch)
                break
            cur = (cards.get(cur) or {}).get("parent")
    return sorted(out)


def find_line(ch, lines):
    cands = []
    for ln in lines:
        t = ln.strip()
        if not t.startswith(ch):
            continue
        rest = t[len(ch):]
        if rest and NEXT_RE.match(rest):
            cands.append(t)
    if not cands:
        return ""
    for t in cands:
        if "《" in t[:60]:
            return t
    return cands[0]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("chars", nargs="*")
    ap.add_argument("--bu")
    ap.add_argument("--txt", default=DEFAULT_TXT)
    ap.add_argument("--out", default=os.path.join(ROOT, ".tmp-charmap.json"))
    ap.add_argument("--expect", help="另写一份 verify-card --expect 用的扁平表 {字:整行}")
    args = ap.parse_args()

    chars = list(args.chars)
    if args.bu:
        chars += members_of(args.bu)
    chars = sorted(set(c for c in chars if c))
    if not chars:
        sys.exit("没有字：给字或 --bu")

    with io.open(args.txt, encoding="utf-8") as f:
        lines = f.read().splitlines()

    cm, missing = {}, []
    for ch in chars:
        line = find_line(ch, lines)
        if line:
            cm[ch] = {"txt": line}
        else:
            missing.append(ch)
    with io.open(args.out, "w", encoding="utf-8", newline="\n") as f:
        json.dump(cm, f, ensure_ascii=False, indent=1)
        f.write("\n")
    print("charmap: %d 字 → %s" % (len(cm), args.out))
    if args.expect:
        flat = {ch: v["txt"] for ch, v in cm.items()}
        with io.open(args.expect, "w", encoding="utf-8", newline="\n") as f:
            json.dump(flat, f, ensure_ascii=False, indent=1)
            f.write("\n")
        print("expect: %d 字 → %s" % (len(flat), args.expect))
    if missing:
        print("缺原稿行 %d：%s" % (len(missing), " ".join(missing)))


if __name__ == "__main__":
    main()
