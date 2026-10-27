# -*- coding: utf-8 -*-
"""Patch memory/CURRENT.md for 《说物解字》卷五 山川."""
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


rep("结构：5 个节点、137 个主题，见 `data/knowledge/registry.json`。",
    "结构：5 个节点、138 个主题，见 `data/knowledge/registry.json`。",
    "head-topics")
rep("5 个节点 / 137 个主题 / 7329 条 Claim",
    "5 个节点 / 138 个主题 / 7337 条 Claim",
    "tail-count")
rep("- 《说物解字》逐卷录入：前言 9 条、卷一 草卉 34 条、卷二 树木 24 条、卷三 虫鱼 14 条、卷四 鸟兽 12 条已入库（137 主题 / 7329 条）；下一步卷五 山川（7 篇），再卷六器用、卷七人文，最后附录「主要引用书目」「解字汇总表」。",
    "- 《说物解字》逐卷录入：前言 9 条、卷一 草卉 34 条、卷二 树木 24 条、卷三 虫鱼 14 条、卷四 鸟兽 12 条、卷五 山川 8 条已入库（138 主题 / 7337 条）；下一步卷六 器用（22 篇），再卷七人文，最后附录「主要引用书目」「解字汇总表」。",
    "next-step")

anchor = "留档 `intake/20261021-说物解字-卷四鸟兽.json`。"
newline = ("- 2026-10-21 新增 8 条（`bnd_3cdc9953b8c1b2ae13318922bf`，hash "
           "`3cdc9953b8c1b2ae13318922bf4e8e3011bd35a9363293383a3ff80697517ba1`）："
           "《说物解字》卷五·山川 8 条，主题 `topic-shuowu-shanchuan`"
           "（`knowledge/hanzi-origin/shuowu-shanchuan.md`）；7 篇山川之字理——"
           "湘（相为相木、相星，《诗经·采蘋》湘通鬺、鬺本昜声，排工排教，湘漓同源，灵渠通岭南）、"
           "汉（堇从口从黑为饥馑唇黑，堇族饉殣槿僅謹熯暵，漢字面为干旱少水，天汉与汉水互名，沔潜夏水，汉广游女）、"
           "泾渭（巠为經之初文取直纵义，泾水季节差千倍、年输沙 3.09 亿吨，郑国渠，胃从肉𡇒声会藏污，胃族猬𢔥𦩝喟謂，清浊随时而变）、"
           "沪（松江枝杈如松，上海浦下海浦，扈即桑扈蜡嘴雀，滬渎之簖与陆龟蒙《渔具诗》，夏原吉开范家浜江浦合流，春申君与申）、"
           "莘（细辛辛辣，辛标志崇高家人言语法权，郭沫若黥额曲刀与吴其昌王倒写，辛为杀伐权，莘为禹母族、汤与莘联姻、太姒，后母戊鼎）、"
           "陕（陕峡同源，夾为两边卡住，荚颊挟，函谷「深险如函」与陕原，「得之者得天下」：前 655 晋假道灭虢、前 318 六国伏尸百万、"
           "前 298 匡章破关、唐哥舒翰失潼关、1944 衡岭之战）、"
           "会（囦为垃圾深坑，会族绘荟桧侩烩嬒，殷法刑弃灰、秦黥弃灰，隋长安水咸卤，唐《唐律疏议》杖六十，裴明礼瓦砾场，"
           "周礼条狼氏，宋街道司，马可·波罗记铺砖石）。"
           "boundary「源自《说物解字》卷五「山川」。」。留档 `intake/20261021-说物解字-卷五山川.json`。")

if anchor in t:
    t = t.replace(anchor, anchor + "\n" + newline, 1)
    print("OK anchor inserted")
else:
    print("MISS anchor")

io.open(P, "w", encoding="utf-8", newline="\n").write(t)
print("changed", t != orig, "len", len(t))
