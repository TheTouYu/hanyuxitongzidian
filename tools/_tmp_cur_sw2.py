# -*- coding: utf-8 -*-
"""Patch memory/CURRENT.md for 说物解字 卷二 树木."""
import io

p = r"memory\CURRENT.md"
t = io.open(p, encoding="utf-8").read()
orig = t
hits = []


def rep(old, new, label):
    global t
    if old not in t:
        hits.append("MISS " + label)
        return
    n = t.count(old)
    t = t.replace(old, new)
    hits.append("OK %s x%d" % (label, n))


rep("5 个节点、134 个主题", "5 个节点、135 个主题", "head-topics")
rep("5 个节点 / 134 个主题 / 7279 条 Claim",
    "5 个节点 / 135 个主题 / 7303 条 Claim", "tail-count")
rep("前言 9 条、卷一 草卉 34 条已入库（134 主题 / 7279 条）；下一步卷二 树木（21 篇），再卷三虫鱼、卷四鸟兽、卷五山川、卷六器用、卷七人文",
    "前言 9 条、卷一 草卉 34 条、卷二 树木 24 条已入库（135 主题 / 7303 条）；下一步卷三 虫鱼（13 篇），再卷四鸟兽、卷五山川、卷六器用、卷七人文",
    "next-step")

anchor = "- 2026-10-21 新增 34 条（`bnd_f95f556ac2f9cfeb68df2cece0`"
i = t.find(anchor)
if i < 0:
    hits.append("MISS anchor-caohui")
else:
    j = t.find("\n", i)
    block = (
        "\n- 2026-10-21 新增 24 条（`bnd_ad739a5172923619e16f564f73`，hash "
        "`ad739a5172923619e16f564f737807a061dc081a9df3664c9580834073d9ee66`）：《说物解字》卷二·树木 24 条，"
        "主题 `topic-shuowu-shumu`（`knowledge/hanzi-origin/shuowu-shumu.md`）；21 篇树木之字理——椿（屯声发芽）、"
        "桂（圭形叶脉辨肉桂与木樨）、楝（柬声练丝与包粽）、㭔（黄栌乎声如哈气）、乐（栎与柞蚕丝弦）、荣（油桐与桐油贷款）、"
        "松（公声针叶与松脂）、𣓌（乌桕臼声舂压）、杹（木芙蓉化声三变）、桃（兆声裂皮与桃符）、李（子声宜子与行李）、"
        "梅（某声媒神）、葚（甚声沉溺）、㭘（合欢蠲忿）、榆（俞声舟行与枌榆社）、枸（句声弯曲与枸酱通夜郎）、"
        "橘（矞声枝刺与晏婴）、皂（澡豆与开关之药）、枣（朿声与早文化）、棕（宗声与千刀万剐）、柳（卯本义与左公柳）、"
        "椒（叔声拾豆与椒房）、栗（刺球与战栗、神主、糖炒）。boundary「源自《说物解字》卷二「树木」。」。"
        "留档 `intake/20261021-说物解字-卷二树木.json`。"
    )
    t = t[:j] + block + t[j:]
    hits.append("OK anchor inserted")

io.open(p, "w", encoding="utf-8", newline="\n").write(t)
print("\n".join(hits))
print("changed", t != orig, "len", len(t))
