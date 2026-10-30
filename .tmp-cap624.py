# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
def S(k,l,t,links=None):
    s={"key":k,"label":l,"text":t,"cites":[]}
    if links: s["links"]=links
    return s
J="suoshujuan"
VOL={"key":J,"label":"所属卷","text":"","cites":[],"links":[{"ch":"卷三矢","label":"卷三 矢"}]}
ER={"key":"erji","label":"本部二级字根","text":"","cites":[],"links":[{"ch":n,"label":n} for n in ("知","智","疾","医","至","到","臺","彘")]}
def build(ch,py_,head,beny,zhuan,sm,groups,grp_notes=None):
    d={"char":ch,"head":head,"pinyin":py_,"level":2,"parent":"矢","bus":[{"num":16,"name":"矢"}],
       "sections":[S("benyi","本义",beny),S("zhuanyi","转义",zhuan),S("shengmu","声母拟态",sm),
        {"key":"zizu","label":"字族衍义","text":"原文字族衍義分下列各組：","cites":[],
         "groups":[{"title":t,"note":"","rows":rows} for t,rows in groups]},ER,VOL]}
    json.dump(d,io.open(os.path.join(C,ch+".json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
SM={"䚐":"j「聚决」取「聚」：目赤而炯，神聚於遠視（推）。",
"𤁰":"zh「凿总」取「凿」：土得水而鑿成泥（推）。",
"䠦":"zh「凿总」取「凿」：躓礙如足被鑿定而頓（推）。",
"𨼓":"zh「凿总」取「总」：縣邑總屬南陽（推）。",
"㑵":"j「聚决」取「聚」：嫉恨聚於心而決（推）。",
"蒺":"j「聚决」取「聚」：蒺藜聚刺成實（推）。",
"槉":"j「聚决」取「聚」：屋枅聚木承重（推）。",
"螏":"j「聚决」取「聚」：蜈蚣聚足而疾行（推）。",
"𨪏":"j「聚决」取「聚」：鐵撾五指聚爪（推）。",
"𠹋":"j「聚决」取「聚」：聲聚而噈（推）。",
"𧪠":"j「聚决」取「聚」：語急而聚言（推）。",
"𧽑":"j「聚决」取「聚」：走遽而聚步（推）。"}
def rows(rs):
    out=[]
    for ch,py_,lei,txt in rs:
        out.append([ch,py_,lei,txt])
        d={"char":ch,"head":ch,"pinyin":py_,"level":3,"parent":"智","bus":[{"num":16,"name":"矢"}],
           "sections":[S("shiyi","释义",txt),S("shengmu","声母拟态",SM.get(ch,"")),VOL],"aliases":[]}
        json.dump(d,io.open(os.path.join(C,ch+".json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    return out
g1=rows([("䚐","jí","見","《說文》：『目赤也。从見，𥏼省聲。』眼睛紅赤。《類篇》：『遙視皃。』"),
 ("𤁰","zhí","水","《說文》：『土得水沮也。从水𥏼聲。讀若䵂。』水土相和成泥。"),
 ("䠦","zhì","足","《篇海》：『陟利切，音智。蹋也，頓也，跲也。』《龍龕》：『躓的俗字。』"),
 ("𨼓","zhí","阜","《集韻》：『酈，縣名，在南陽。或作𨼓。』")])
g2=rows([("㑵","jí","人","《說文》：『妎也。从人疾聲。一曰毒也。』嫉妒。憎惡。"),
 ("蒺","jí","艸","《本草》：『蒺，疾也。其刺傷人甚疾而利也。』蒺藜。有刺如箭。"),
 ("槉","jí","木","《集韻》：『昨悉切，音疾。屋枅也。』房柱上的弓形承重結構，即栱。"),
 ("螏","jí","虫","《集韻》：『昨悉切，音疾。螏䖿，蟲名。』《爾雅·釋蟲》：『蒺藜，蝍蛆。』郭璞注：『似蝗而大腹長角，能食蛇腦。』"),
 ("𨪏","jí","金","《集韻》：『昨悉切，音疾。𨪏鑗，鐵撾。』明茅元儀《武備志》記『雙飛撾』：用淨鐵照樣式打造鷹爪樣，五指攢中。"),
 ("𠹋","jí","口","《集韻》：『噈𠹋，聲也。』"),
 ("𧪠","jí","言","《玉篇》：『毒、苦也。又作愱。』《廣韻》：『語急。』"),
 ("𧽑","jí","走","《集韻》：『走遽也。』")])
for ch,t in (("㑵","嫉"),):
    pass
json.dump(json.load(io.open(os.path.join(C,"疾.json"),encoding="utf-8")) if os.path.exists(os.path.join(C,"疾.json")) else {}, io.open(os.devnull,"w"))
print("智行",len(g1),"疾行",len(g2))