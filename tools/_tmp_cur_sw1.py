# -*- coding: utf-8 -*-
"""Patch memory/CURRENT.md for 说物解字 前言 + 卷一 草卉."""
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


rep("5 个节点、132 个主题", "5 个节点、134 个主题", "head-topics")
rep("5 个节点 / 132 个主题 / 7236 条 Claim",
    "5 个节点 / 134 个主题 / 7279 条 Claim", "tail-count")

anchor = "- 2026-10-21 新增 41 条（`bnd_6f928b220ae3a92767571720de`"
i = t.find(anchor)
if i < 0:
    hits.append("MISS anchor-100")
else:
    j = t.find("\n", i)
    block = (

        "\n- 2026-10-21 新增 9 条（`bnd_6a1178123d33feeeff838dbdd7`，hash "
        "`6a1178123d33feeeff838dbdd798a44f2314eaae24a0149f1210e6f791798cae`）：《说物解字》前言 9 条，"
        "主题 `topic-shuowu-qianyan`（`knowledge/hanzi-origin/shuowu-qianyan.md`），节点 `hanzi-origin`；"
        "内容为作者的汉字系统观——形旁只标类别、非真系统，声旁系列才是系统（「兆」九十余字族例），"
        "右文说经梁启超、沈兼士到陈寅恪「只有此一条路可走」，作者十五年探得 510 个表声字根而成《系统汉语》（2018），"
        "本书以「物名与物性相符」为试金石逐字验证（桃取兆之「缝隙」义），原为《衡阳日报》文化周刊谭浩泉约稿，"
        "任继昉「小课题作出了大学问」、周金声「音意系统与形意系统双轨」。boundary「源自《说物解字》前言。」。"
        "\n- 2026-10-21 新增 34 条（`bnd_f95f556ac2f9cfeb68df2cece0`，hash "
        "`f95f556ac2f9cfeb68df2cece0b2e0df47ed2235255636ab6afde5ef0babaab9`）：《说物解字》卷一·草卉 34 条，"
        "主题 `topic-shuowu-caohui`（`knowledge/hanzi-origin/shuowu-caohui.md`）；33 篇草卉之字理，"
        "每篇以物之性状证声旁本义：宁（麻布→贮存）、䓉（甫声宽扁）、莎（沙声、蓑）、藰（劉声秃溜、商陆火守岁）、"
        "萧与艾（冰台取火、萧非艾）、帝（花蒂→创造神）、菉（录＝辘轳）、苏（𩵦鱼声→苏醒）、莪（我声长而倾顶、蓼莪）、"
        "芰（支声多角）、葥（歬声、凡＝洞）、齐（齊象蒺藜子）、葵与五菜（葵韭藿薤葱）、葱（悤声→聪）、"
        "萱（宣＝堂屋、母亲花）、蒉（贵声→溃、臭苋菜梗）、蕺（戢声藏兵、勾践岑草）、蕨（厥声发石机、原蕨苷）、"
        "荆（刑具→刑／型）、茅（矛借形、缩酒、菁茅经济战）、青（井生青苔、华佗蜂毒）、萝（罗声环绕、女萝）、"
        "南（楠竹象形、衡山国经济战）、笋（尹声、孟宗泣笋）、药中三母（知母䓡／益母蓷／贝母莔）、"
        "苇（韦声围绕、一苇杭之、火牛阵）、芣苡（以声、车前／薏苡／莲子）、蓼（翏声草穗、辣蓼、蓼汀惜春）、"
        "蕈与菌（覃声、囷声、白蚁种菌）、薯（署声、陈振龙引番薯）、姜（畺声田界、田塍种姜）、芋（于＝竽形、蹲鸱）、"
        "稻（舀声加工、玉蟾岩 14000–18000 年）。boundary「源自《说物解字》卷一「草卉」。」。"
        "留档 `intake/20261021-说物解字-前言.json`、`intake/20261021-说物解字-卷一草卉.json`。"
    )
    t = t[:j] + block + t[j:]
    hits.append("OK anchor-100 inserted")

h2 = "## 下一步\n"
if h2 in t:
    newline = (
        "\n- 《说物解字》逐卷录入：前言 9 条、卷一 草卉 34 条已入库（134 主题 / 7279 条）；"
        "下一步卷二 树木（21 篇），再卷三虫鱼、卷四鸟兽、卷五山川、卷六器用、卷七人文，"
        "最后附录「主要引用书目」「解字汇总表」。\n"
    )
    t = t.replace(h2, h2 + newline, 1)
    hits.append("OK next-step")
else:
    hits.append("MISS next-step header")

io.open(p, "w", encoding="utf-8", newline="\n").write(t)
print("\n".join(hits))
print("changed", t != orig, "len", len(t))
