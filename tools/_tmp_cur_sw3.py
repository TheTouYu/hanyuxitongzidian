# -*- coding: utf-8 -*-
"""Patch memory/CURRENT.md for 说物解字 卷三 虫鱼."""
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


rep("5 个节点、135 个主题", "5 个节点、136 个主题", "head-topics")
rep("5 个节点 / 135 个主题 / 7303 条 Claim",
    "5 个节点 / 136 个主题 / 7317 条 Claim", "tail-count")
rep("前言 9 条、卷一 草卉 34 条、卷二 树木 24 条已入库（135 主题 / 7303 条）；下一步卷三 虫鱼（13 篇），再卷四鸟兽、卷五山川、卷六器用、卷七人文",
    "前言 9 条、卷一 草卉 34 条、卷二 树木 24 条、卷三 虫鱼 14 条已入库（136 主题 / 7317 条）；下一步卷四 鸟兽（11 篇），再卷五山川、卷六器用、卷七人文",
    "next-step")

anchor = "- 2026-10-21 新增 24 条（`bnd_ad739a5172923619e16f564f73`"
i = t.find(anchor)
if i < 0:
    hits.append("MISS anchor-shumu")
else:
    j = t.find("\n", i)
    block = (
        "\n- 2026-10-21 新增 14 条（`bnd_543550cc25b9252f31b7b859b0`，hash "
        "`543550cc25b9252f31b7b859b0e97d8e3726655fb7d2df246b6af09889584aab`）：《说物解字》卷三·虫鱼 14 条，"
        "主题 `topic-shuowu-chongyu`（`knowledge/hanzi-origin/shuowu-chongyu.md`）；13 篇虫鱼之字理——"
        "禹（九声手肘屈伸义＝尺蠖，大禹偏枯之步与禹步）、蛭（至声箭中义与吸血再生、楚惠王吞蛭案）、"
        "秋（蟋蟀象形，「鬮」从鬥从龜而龜本蟋蟀、斗蟋之弊）、良（螵蛸象形与螳螂，良善义夺本义）、"
        "赖（剌省声粗壳义＝牡蛎，籁取插竹养蛎）、萬（蝎形，粗糙/毒烈/众多三系引申）、"
        "辰（蚌蜃伸足形，孕珠故星辰，蚌镰「摩蜃而耨」，祝融为火正官名）、蝓（呙声螺旋壳、俞声行舟，蜗角之争与女娲）、"
        "胥（疋声足形＝蟹，蟹胥、夫婿之胥取多才）、亶（它形㐭声＝鳝，性转与穴居）、鲫（即声相就义，「味珍无辈」）、"
        "萤（声屋内有火＝微光，荧茔荣莺莹营皆取微光，囊萤与放萤）、蝶（胡为牛羊薄皮、枼为薄叶，庄周梦蝶与蝴蝶妈妈）。"
        "boundary「源自《说物解字》卷三「虫鱼」。」。留档 `intake/20261021-说物解字-卷三虫鱼.json`。"
    )
    t = t[:j] + block + t[j:]
    hits.append("OK anchor inserted")

io.open(p, "w", encoding="utf-8", newline="\n").write(t)
print("\n".join(hits))
print("changed", t != orig, "len", len(t))
