# -*- coding: utf-8 -*-
"""Patch memory/CURRENT.md for 《说物解字》卷七 人文."""
import io

P = r"memory\CURRENT.md"
t = io.open(P, encoding="utf-8").read()
orig = t


def rep(a, b, label):
    global t
    if a in t:
        t = t.replace(a, b, 1)
        print("OK", label)
    else:
        print("MISS", label)


rep("结构：5 个节点、139 个主题，见 `data/knowledge/registry.json`。",
    "结构：5 个节点、140 个主题，见 `data/knowledge/registry.json`。",
    "head-topics")
rep("5 个节点 / 139 个主题 / 7360 条 Claim",
    "5 个节点 / 140 个主题 / 7377 条 Claim",
    "tail-count")
rep("- 《说物解字》逐卷录入：前言 9 条、卷一 草卉 34 条、卷二 树木 24 条、卷三 虫鱼 14 条、卷四 鸟兽 12 条、卷五 山川 8 条、卷六 器用 23 条已入库（139 主题 / 7360 条）；下一步卷七 人文（16 篇），最后附录「主要引用书目」「解字汇总表」。",
    "- 《说物解字》逐卷录入：前言 9 条、卷一 草卉 34 条、卷二 树木 24 条、卷三 虫鱼 14 条、卷四 鸟兽 12 条、卷五 山川 8 条、卷六 器用 23 条、卷七 人文 17 条已入库（140 主题 / 7377 条），正文七卷齐；尚余附录「主要引用书目」「解字汇总表」待定。",
    "next-step")

anchor = "留档 `intake/20261021-说物解字-卷六器用.json`。"
newline = ("- 2026-10-21 新增 17 条（`bnd_fd0268278994d88764b36dfec4`，hash "
           "`fd0268278994d88764b36dfec45c08a54edcc2578f3ad398878bb54eb009bd49`）："
           "《说物解字》卷七·人文 17 条，主题 `topic-shuowu-renwen`"
           "（`knowledge/hanzi-origin/shuowu-renwen.md`）；16 篇——"
           "官（宀+𠂤屁股，本即馆，倌棺绾婠，五官，《尚书》百官）、"
           "皇（日+十光芒，极明极旱，煌隍餭，蝗与皇舞）、"
           "国（囗+或从戈，惑阈淢罭，太平天国简化字，孔子均无贫和无寡）、"
           "胡（肉+古，下巴垂肉，猢葫鶘糊，胡服与汉服，五胡乱华）、"
           "静（从争青声，青=井中青苔，靖，《道德经》清静为天下正）、"
           "市（止+示，庙会社日，文天祥《衡州上元记》，衡阳诸庙会）、"
           "约（糸+久，烙印持久，司约，《礼记》约信曰誓，约法三章曾子杀猪）、"
           "豖（豕加一点即阉割，啄琢椓諑㧻，宫刑与司马迁）、"
           "孜（攴+子，小儿持棍嬉戏，乐此不疲，读书为趣味）、"
           "明（日月/目月/囧月/窗月四体，囧为心脏剖面，盟与郑桓公袭郐）、"
           "颐（叩齿咽津搭鹊桥，乾隆十常四勿，另一说𦣞为梳篦、梳头养生）、"
           "休沐（五日一洗，《汉律》五日一休沐，唐 47 天宋 112 天，朱元璋砍旬假）、"
           "毅（野猪冲撞，豙从干从豕，敢=持杈对野猪，彘星北斗）、"
           "义（羊角饰我之仪仗，美善同构，怀忠仗义等成语，梁山聚义厅改忠义堂）、"
           "荤（艸+军，本指葱蒜韭薤，五荤，梁武帝《断酒肉文》）、"
           "贞（贝卦卜问，侦桢帧䡠，龟卜卜声字，商汤祷雨，《尚书·洪范》谋及乃心）。"
           "boundary「源自《说物解字》卷七「人文」。」。留档 `intake/20261021-说物解字-卷七人文.json`。")

if anchor in t:
    t = t.replace(anchor, anchor + "\n" + newline, 1)
    print("OK anchor inserted")
else:
    print("MISS anchor")

io.open(P, "w", encoding="utf-8", newline="\n").write(t)
print("changed", t != orig, "len", len(t))
