# -*- coding: utf-8 -*-
"""建 308 㒳部：兩（lv1）+ 㒼（lv2）+ 50 族卡，并整理照片/索引。
只写卡与素材，不改知识库。

【已过期，勿再运行】308 卡已于 c2b374a86 提交，其后用 fix-308-luodian.py 改过
落点、assets 脚本改过索引。重跑本脚本会覆盖这些回改。以
web/public/cards/兩.json、web/public/cards/㒼.json 为唯一真源。
"""
import json, io, os, re, shutil, zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
C = os.path.join(ROOT, "web", "public", "cards")
G = os.path.join(ROOT, "web", "public", "glyphs")
DOCX = r"D:/字谱智能体/卷五十四  网.docx"
BUS = {"num": 308, "name": "㒳"}
JUAN = {"t": "卷", "ch": "卷五十四网", "label": "卷五十四网"}

z = zipfile.ZipFile(DOCX)
_doc = z.read("word/document.xml").decode("utf-8")
P = re.findall(r"<w:p[ >].*?</w:p>", _doc, re.S)


def txt(i):
    return "".join(re.findall(r"<w:t[^>]*>(.*?)</w:t>", P[i], re.S)).strip()


def strip_label(s, label):
    return re.sub(r"^\s*" + label + r"[：:]", "", s).strip()


def sec(key, label, text, **kw):
    d = {"key": key, "label": label, "text": text}
    d.update(kw)
    return d


def fam(ch, head, pinyin, parent, shiyi, shengmu, aliases):
    d = {"char": ch, "head": head, "pinyin": pinyin, "bus": BUS, "level": 3, "parent": parent}
    if aliases:
        d["aliases"] = aliases
    d["sections"] = [
        sec("shiyi", "釋義", shiyi),
        sec("shengmu", "聲母擬態", shengmu),
        sec("suoshujuan", "所属卷", "", links=[JUAN]),
    ]
    return d


LAB = {"本義": "benyi", "轉義": "zhuanyi", "辯證": "bianzheng", "音源": "yinyuan"}

# ---------------- 兩 ----------------
benyi = [strip_label(txt(333), "本義")]
zhuanyi = [strip_label(txt(i), "轉義") for i in (334, 335, 336)]
bianzheng = [strip_label(txt(338), "辯證")]
yinyuan = [strip_label(txt(339), "音源"), txt(340)]

about = [
    # ch, head, pinyin, cls, luodian, shengmu, group
    ("緉（䩫）", "liǎng", "糸",
     "《說文》「履兩枚也。」——履成雙而耦，故以兩計。",
     "l「拢离」取「拢」：兩履聚而相屬（推）。", 0),
    ("脼（朖）", "liǎng", "肉",
     "《說文》「膎肉也。」——夾脊之肉分處兩旁，耦而相對。",
     "l「拢离」取「离」：肉分夾脊，離處兩邊（推）。", 0),
    ("輛", "liàng", "車",
     "《漢書注》「車一乗曰一兩」——輪轅兩兩相耦，故車以兩計。",
     "l「拢离」取「拢」：兩輪攏轅，耦而成車（推）。", 0),
    ("倆（𢎏）", "liǎng", "人",
     "《集韻》「伎倆，巧也。」——一身具兩手之能，故稱伎倆。",
     "l「拢离」取「拢」：巧技聚於兩手（推）。", 0),
    ("啢", "liǎng", "口",
     "英美制重量單位，常衡一啢是一磅的十六分之一——音譯字，只取其音。",
     "l「拢离」不系：英美制單位之譯音，聲義無涉（照實）。", 0),
    ("𩀝（雙）", "shuāng", "隹",
     "《篇海》「俗雙字。」——二隹並棲，耦而成雙。",
     "sh「失收」取「收」：二隹並棲，收而成耦（推）。", 0),
    ("𩭫", "zhǎng", "髟",
     "《篇韻》「髮也。」——髮分兩鬢，各綰一邊。",
     "zh「凿总」取「总」：髮總於頂，分綰兩鬢（推）。", 0),
    ("蜽（魎𩳮）", "liǎng", "虫",
     "《玉篇》「魍魎，水神，如三歲小兒，赤黑色。」——夜出魅人，夢魘如受軛壓。",
     "l「拢离」取「拢」：魘魅攏身，如受套而壓（推）。", 1),
    ("𩗾（魎）", "liǎng", "風",
     "《字海》「同魎。」——鬼魅壓身，如軛套項而不得脫。",
     "l「拢离」取「离」：欲離魘壓而不得（推）。", 1),
    ("掚", "liǎng", "手",
     "《集韻》「整飾也。」——手攏其飾，如軛正頸。",
     "l「拢离」取「拢」：手攏而正其飾（推）。", 1),
    ("裲", "liǎng", "衣",
     "《釋名》「裲襠，其一當胸，其一當背也。」——兩片夾身，如軛套肩背。",
     "l「拢离」取「拢」：兩片攏覆肩背（推）。", 1),
    ("𣓈", "liǎng", "木",
     "《集韻》「松液。」——松節狀如軛，脂液聚於受壓處。",
     "l「拢离」取「拢」：脂液攏結於節（推）。", 1),
    ("㔝", "liǎng", "力",
     "《集韻》「㔝勥，力拒也。」——力相拒，如受軛套而抗。",
     "l「拢离」取「离」：力相拒而離（推）。", 1),
    ("䠃", "liǎng", "足",
     "《篇海》「足踞也。」——足踞如套，拘而不得行。",
     "l「拢离」取「拢」：足踞而攏地（推）。", 1),
    ("𥇑（䀶）", "lǎng", "目",
     "《集韻》「目明。或从良。」——目光聚於一，如軛之收束。",
     "l「拢离」取「拢」：目光收攏而明（推）。", 1),
    ("𥮩（𥲈）", "mǎn", "竹",
     "《字彙補》「𥲈字省文。」——竹器斂物，如套而拘。",
     "m「蒙末」取「蒙」：竹器蒙覆而藏物（推）。", 1),
    ("𨨄（鋃）", "lǎng", "金",
     "《字海》「同鋃字。」——鎖拘物，如軛套頸。",
     "l「拢离」取「拢」：鎖攏而拘物（推）。", 1),
]

abao = [
    ("鬗", "mán", "髟",
     "《說文》「髮長也。」——長髮覆肩，如物蒙其上。",
     "m「蒙末」取「蒙」：長髮蒙覆肩背（推）。", 0),
    ("滿（懣）", "mán", "水",
     "《說文》「盈溢也。」——水滿容器，充塞而外溢。",
     "m「蒙末」取「末」：水盈至末，更無餘地（推）。", 0),
    ("瞞", "mán", "目",
     "《說文》「平目也。」——目皮重覆，故平闔而不露。",
     "m「蒙末」取「蒙」：目皮垂蒙，故平闔（推）。", 0),
    ("慲（𢟮）", "mán", "心",
     "《說文》「忘也。」——心為物所覆，故忘。",
     "m「蒙末」取「蒙」：心為事蒙，故忘（推）。", 0),
    ("懣", "mèn", "心",
     "《說文》「煩也。」——氣鬱積至末，故煩悶。",
     "m「蒙末」取「末」：氣鬱至末，塞而煩（推）。", 0),
    ("顢", "mān", "頁",
     "《廣韻》「顢頇，大面皃。」——面大而覆，故稱顢頇。",
     "m「蒙末」取「蒙」：面大蒙覆，故稱顢頇（推）。", 0),
    ("蹣（𨃟跘）", "pán", "足",
     "《玉篇》「蹣跚，旋行皃。」——足盤旋而進，如被裹覆。",
     "p「拼辟」取「辟」：足盤辟而行（推）。", 0),
    ("襔", "mǎn", "衣",
     "《漢典》「絲棉襖。」——衣厚覆身，故曰襔。",
     "m「蒙末」取「蒙」：衣厚蒙身（推）。", 0),
    ("𤡁（䝡𧴝獌）", "mǎn", "犬",
     "《集韻》「獌，獸名，似貍。」——獸毛蒙茸，故以為名。",
     "m「蒙末」取「蒙」：獸毛蒙茸（推）。", 0),
    ("䊟", "mén", "米",
     "《集韻》「粥凝。」——粥面凝膜，覆於其上。",
     "m「蒙末」取「蒙」：粥面凝膜蒙覆（推）。", 0),
    ("䤍（𨢥）", "mí", "酉",
     "《廣韻》「醭䤍，醬上白也。」——醬敗生黴，覆於表面。",
     "m「蒙末」取「蒙」：白黴蒙於醬面（推）。", 0),
    ("暪", "mèn", "日",
     "《玉篇》「暗。」——日光被遮，故暗。",
     "m「蒙末」取「蒙」：日為雲蒙，故暗（推）。", 0),
    ("濷", "fèi", "水",
     "《搜眞玉鏡》「溢也。」——水沸而漫，覆出於外。",
     "f「附分」取「附」：水沸漫附而出（推）。", 0),
    ("㙢（墁）", "mán", "土",
     "《類篇》「土覆。」——以土覆物。",
     "m「蒙末」取「蒙」：土蒙覆其上（推）。", 0),
    ("㨺（捫）", "miǎn", "手",
     "《集韻》「飾也。」——手覆而飾之。",
     "m「蒙末」取「蒙」：手蒙而飾（推）。", 0),
    ("䐽", "mán", "肉",
     "《字韻合璧》「乾肉也；又肉也。」——乾肉以鹽覆而藏。",
     "m「蒙末」取「蒙」：鹽蒙肉而乾（推）。", 0),
    ("𡒗", "mái", "土",
     "同「埋」——以土覆物而藏之。",
     "m「蒙末」取「蒙」：土蒙物而藏（推）。", 0),
    ("𡠪（嫚）", "màn", "女",
     "《字海》「同嫚。」——侮慢陵人，如以勢覆壓。",
     "m「蒙末」取「蒙」：勢凌而蒙壓（推）。", 0),
    ("𡣩（婆）", "pó", "女",
     "《字彙補》「佛經婆字」——音譯字，只取其音。",
     "p「拼辟」不系：佛經譯音，聲義無涉（照實）。", 0),
    ("𤂀", "bì", "水",
     "《字彙補》「行不止也。」——水流漫衍，剝岸而不止。",
     "b「闭剥」取「剥」：水剝岸而漫行（推）。", 0),
    ("𤅎", "màn", "水",
     "《集韻》「𤅎𣽥，水皃。」——水漫覆之貌。",
     "m「蒙末」取「蒙」：水漫蒙物（推）。", 0),
    ("𥲈（𥵥）", "mǎn", "竹",
     "《集韻》「竹器。」——竹器斂物而覆藏。",
     "m「蒙末」取「蒙」：竹器蒙物（推）。", 0),
    ("𧫩（謾）", "màn", "言",
     "《正字通》「同謾。」——以言覆蓋其實。",
     "m「蒙末」取「蒙」：言蒙其實（推）。", 0),
    ("𧱼（䝡）", "mán", "豕",
     "《字彙》「豕屬。」——豕毛蒙茸，故从㒼。",
     "m「蒙末」取「蒙」：豕毛蒙茸（推）。", 0),
    ("𩞘（滿）", "mán", "食",
     "《漢典》「同滿。」——食盈至末而飽。",
     "m「蒙末」取「末」：食至末而飽（推）。", 0),
    ("𩺴（鰻）", "màn", "魚",
     "《正字通》「俗鰻字。」——鰻體黏滑，蒙覆泥沙。",
     "m「蒙末」取「蒙」：黏液蒙體（推）。", 0),
    ("樠（槾榔）", "mán", "木",
     "《說文》「松心木。」——木心微赤，如丹蒙其中。",
     "m「蒙末」取「蒙」：赤心蒙於木中（推）。", 1),
    ("𣯩", "mén", "毛",
     "《說文》「以毳為𦇧，色如虋。」——赤色毳布，色如赤苗。",
     "m「蒙末」取「蒙」：赤毳蒙身（推）。", 1),
    ("璊（玧）", "mén", "玉",
     "《說文》「玉䞓色也。」——玉色赤如虋苗。",
     "m「蒙末」取「蒙」：赤色蒙於玉（推）。", 1),
    ("蟎", "mǎn", "虫",
     "蟎蟲叮後皮膚發紅發癢——其害見於赤色。",
     "m「蒙末」取「蒙」：蟲蒙膚而叮（推）。", 1),
    ("鏋", "mǎn", "金",
     "《集韻》「金精謂之鏋。」——金精即赤金，色赤。",
     "m「蒙末」取「蒙」：赤金蒙於精（推）。", 1),
    ("𥡹（虋𧄸穈）", "mén", "禾",
     "《集韻》「赤苗嘉穀也。」——赤粱粟，苗色赤。",
     "m「蒙末」取「蒙」：赤苗蒙於禾（推）。", 1),
]

# 註：族卡 pinyin 取行首音；類屬取形旁。
# 已另有卡者不入 aliases。
extra = {"兩": {"𠓜", "㒳", "两", "両"}, "㒼": {"䓣", "𦲸"}}
allrows = {r[0].split("（")[0] for r in about + abao}


def aliases_of(head, ch):
    m = re.match(re.escape(ch) + r"[（(]([^）)]*)[）)]", head)
    if not m:
        return []
    return [c for c in m.group(1) if re.match(r"[\u3400-\u9fff\U00020000-\U0002FFFF]", c)
            and c not in allrows and c != ch]


def zizu(groups):
    return sec("zizu", "字族衍義", "", groups=groups)


def rows_of(table, parent):
    out = {}
    for ch, py, cls, ld, sm, gi in table:
        head = ch
        out.setdefault(gi, []).append([ch, py, cls, ld])
    return out


g1 = []
g2 = []
for ch, py, cls, ld, sm, gi in about:
    (g1 if gi == 0 else g2).append([ch, py, cls, ld])

groups_liang = [
    {"title": "①指雙軛，表示偶、雙", "rows": g1},
    {"title": "②指套軛，表示壓制、牽拉", "rows": g2},
    {"title": "③形近字“圣”之訛", "rows": [["𧶪（貴）", "guì", "貝", "《字彙補》：“古文貴字。”"]]},
]

a1 = []
a2 = []
for ch, py, cls, ld, sm, gi in abao:
    (a1 if gi == 0 else a2).append([ch, py, cls, ld])

groups_bao = [
    {"title": "①指遮蓋、蒙覆", "rows": a1},
    {"title": "②指赤色", "rows": a2},
]

liang = {
    "char": "兩", "head": "兩（𠓜㒳两両）", "pinyin": "liǎng",
    "aliases": ["𠓜", "㒳", "两", "両"], "bus": BUS, "level": 1,
    "sections": [
        sec("benyi", "本義", benyi[0]),
        {"key": "erji", "label": "本部字根", "text": "", "paras": [],
         "links": [{"ch": "㒼", "label": "㒼（䓣𦲸）"}]},
        sec("zhuanyi", "轉義", "\n".join(zhuanyi)),
        sec("bianzheng", "辯證", bianzheng[0]),
        sec("yinyuan", "音源", "\n".join(yinyuan)),
        sec("shengmu", "聲母擬態", "l「拢离」取「拢」：一衡兩軛，耦攏而分套兩馬（推）。"),
        zizu(groups_liang),
        sec("zixing", "字形", "", gimgs=["兩/%02d.png" % i for i in range(1, 29)]),
        sec("suoshujuan", "所属卷", "", links=[JUAN]),
    ],
    "photos": [{"file": "01.jpg", "caption": ""}],
}

benyi_b = [strip_label(txt(364), "本義")]
zhuanyi_b = [strip_label(txt(i), "轉義") for i in (365, 366, 367)]
bianzheng_b = [strip_label(txt(370), "辯證"), txt(371)]
yinyuan_b = [strip_label(txt(372), "音源")]

bao = {
    "char": "㒼", "head": "㒼（䓣𦲸）", "pinyin": "mán",
    "aliases": ["䓣", "𦲸"], "bus": BUS, "level": 2, "parent": "兩",
    "rootChain": ["兩", "㒼"], "rootLabel": "兩",
    "sections": [
        sec("benyi", "本義", benyi_b[0]),
        sec("zhuanyi", "轉義", "\n".join(zhuanyi_b)),
        sec("bianzheng", "辯證", "\n".join(bianzheng_b)),
        sec("yinyuan", "音源", yinyuan_b[0]),
        sec("shengmu", "聲母擬態", "m「蒙末」取「蒙」：革甲覆於肩背，蒙而護之（推）。"),
        zizu(groups_bao),
        sec("zixing", "字形", "", gimgs=["㒼/%02d.png" % i for i in range(1, 6)]),
        sec("suoshujuan", "所属卷", "", links=[JUAN]),
    ],
    "photos": [{"file": "01.jpg", "caption": "披馬甲的唐三彩"}],
}


def dump(obj, path):
    with io.open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=1)
        f.write("\n")


def shiyi_from_pi(ch, head, py, pi):
    t = txt(pi)
    assert t.startswith(head), (head, t[:30])
    rest = t[len(head):]
    rest = rest.strip()
    assert rest.startswith(py), (ch, py, rest[:20])
    rest = rest[len(py):].lstrip()
    rest = re.sub(r"^[：:]\s*", "", rest)
    return rest


# 段号：兩族 343-362；㒼族 375-407（蟎 405）
PI = {
    "緉（䩫）": 343, "脼（朖）": 344, "輛": 345, "倆（𢎏）": 346, "啢": 347,
    "𩀝（雙）": 348, "𩭫": 349, "蜽（魎𩳮）": 351, "𩗾（魎）": 352, "掚": 353,
    "裲": 354, "𣓈": 355, "㔝": 356, "䠃": 357, "𥇑（䀶）": 358,
    "𥮩（𥲈）": 359, "𨨄（鋃）": 360,
    "鬗": 375, "滿（懣）": 376, "瞞": 377, "慲（𢟮）": 378, "懣": 379,
    "顢": 380, "蹣（𨃟跘）": 381, "襔": 382, "𤡁（䝡𧴝獌）": 383, "䊟": 384,
    "䤍（𨢥）": 385, "暪": 386, "濷": 387, "㙢（墁）": 388, "㨺（捫）": 389,
    "䐽": 390, "𡒗": 391, "𡠪（嫚）": 392, "𡣩（婆）": 393, "𤂀": 394,
    "𤅎": 395, "𥲈（𥵥）": 396, "𧫩（謾）": 397, "𧱼（䝡）": 398,
    "𩞘（滿）": 399, "𩺴（鰻）": 400, "樠（槾榔）": 402, "𣯩": 403,
    "璊（玧）": 404, "蟎": 405, "鏋": 406, "𥡹（虋𧄸穈）": 407,
}
sm_of = {}
for ch, py, cls, ld, sm, gi in about + abao:
    sm_of[ch] = sm

fam_cards = []
for ch, py, cls, ld, sm, gi in about + abao:
    base = ch.split("（")[0]
    body = shiyi_from_pi(base, ch, py, PI[ch])
    d = fam(base, ch, py, "兩" if ch in {r[0] for r in about} else "㒼",
            body, sm, aliases_of(ch, base))
    fam_cards.append((base, d))

dump(liang, os.path.join(C, "兩.json"))
dump(bao, os.path.join(C, "㒼.json"))
for base, d in fam_cards:
    dump(d, os.path.join(C, base + ".json"))

print("cards:", len(fam_cards) + 2)
print("兩 groups:", [(g["title"], len(g["rows"])) for g in groups_liang])
print("㒼 groups:", [(g["title"], len(g["rows"])) for g in groups_bao])
