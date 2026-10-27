# -*- coding: utf-8 -*-
"""Patch memory/CURRENT.md for 《说物解字》卷四 鸟兽."""
import io

P = r"memory\CURRENT.md"
t = io.open(P, encoding="utf-8").read()
orig = t

reps = []


def rep(a, b, label):
    reps.append((a, b, label))


rep("结构：5 个节点、136 个主题，见 `data/knowledge/registry.json`。",
    "结构：5 个节点、137 个主题，见 `data/knowledge/registry.json`。",
    "head-topics")
rep("5 个节点 / 136 个主题 / 7317 条 Claim",
    "5 个节点 / 137 个主题 / 7329 条 Claim",
    "tail-count")
rep("- 《说物解字》逐卷录入：前言 9 条、卷一 草卉 34 条、卷二 树木 24 条、卷三 虫鱼 14 条已入库（136 主题 / 7317 条）；下一步卷四 鸟兽（11 篇），再卷五山川、卷六器用、卷七人文，最后附录「主要引用书目」「解字汇总表」。",
    "- 《说物解字》逐卷录入：前言 9 条、卷一 草卉 34 条、卷二 树木 24 条、卷三 虫鱼 14 条、卷四 鸟兽 12 条已入库（137 主题 / 7329 条）；下一步卷五 山川（7 篇），再卷六器用、卷七人文，最后附录「主要引用书目」「解字汇总表」。",
    "next-step")

anchor = "留档 `intake/20261021-说物解字-卷三虫鱼.json`。"
newline = ("- 2026-10-21 新增 12 条（`bnd_52c6b75d5e67ee950f1e07cbc3`，hash "
           "`52c6b75d5e67ee950f1e07cbc326d7eafbc0e00a41cf630cd90ef9df68b78450`）："
           "《说物解字》卷四·鸟兽 12 条，主题 `topic-shuowu-niaoshou`"
           "（`knowledge/hanzi-origin/shuowu-niaoshou.md`）；11 篇鸟兽之字理——"
           "安（甲骨文妟，燕头女身，燕巢檐下故安，安声按鞍頞取高处，简狄吞卵生契，怀集敬燕节）、"
           "鹖（曷从匃，濒死张口求乞之声，褐马鸡鹖冠，《礼记》「鹖旦不鸣」，张敞以鹖折黄霸）、"
           "雚（鹭冠羽象形，《说文》小爵误，雈为总角之鸟，舊从雈臼声非猫头鹰，觀䠰颧歡）、"
           "鸠（九为曲指钩形，勾喙鸟统称，武威鸠杖王杖十简，不噎之鸟，鳲鸠巢寄生）、"
           "家（宀＋豭公猪，走婚制之遗，嫁从家声，摩梭）、"
           "为（象鼻加又，象鼻四万肌纤维之灵活，为声伪譌取不正，《说文》母猴误）、"
           "犮（与亥同源，旱獭直立，《山海经》女魃、《神异经》目在顶上，祓与鼠疫）、"
           "有（肉＋又为里脊，暗红／圆长／暗藏三系，贿絠酭姷，《说文》肉作月误）、"
           "雁（金文雁阵，人字阵空气动力学，五德与奠雁五礼，雁→鹅→赝，苏武雁足书）、"
           "蝠（畐为仰韶尖底瓶，宥卮知足之器，倒挂之象，畐族逼踾煏稫副幅辐，五福纹样）、"
           "猴（侯本箭镞，腮鼓如镞，《埤雅》猴善候，马上封侯、沐猴而冠）。"
           "boundary「源自《说物解字》卷四「鸟兽」。」。留档 `intake/20261021-说物解字-卷四鸟兽.json`。")

for a, b, label in reps:
    if a in t:
        t = t.replace(a, b, 1)
        print("OK", label)
    else:
        print("MISS", label)

if anchor in t:
    t = t.replace(anchor, anchor + "\n" + newline, 1)
    print("OK anchor inserted")
else:
    print("MISS anchor")

io.open(P, "w", encoding="utf-8", newline="\n").write(t)
print("changed", t != orig, "len", len(t))
