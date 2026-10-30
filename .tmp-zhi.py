# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
C=r"D:\系统汉字\web\public\cards"; G=r"D:\系统汉字\web\public\glyphs"
doc=Document(r"D:\字谱智能体\卷七  斤.docx"); parts=doc.part.related_parts
D=os.path.join(G,"炙"); os.makedirs(D,exist_ok=True)
for f in os.listdir(D): os.remove(os.path.join(D,f))
n=0
for el in doc.paragraphs[376]._p.iter():
    if el.tag.split("}")[-1]=="blip":
        rid=[v for a,v in el.attrib.items() if a.endswith("}embed") or a.endswith("}id")]
        if rid:
            n+=1; open(os.path.join(D,"%02d.png"%n),"wb").write(parts[rid[0]].blob)
files=sorted(os.listdir(D))
BUS={"num":47,"name":"炙"}
BEN=("从肉从火，象意用火燒烤肉。zhì，《說文》：“炮肉也。从肉在火上。凡炙之屬皆从炙。，籀文。之石切。”")
ZY=("由烤肉引申指熱。《廣雅》：“爇也。”")
YY=("音源字，源自烤肉時所發出的聲音。因古燒石炙肉，故義音同“石”。《易·晉》：“晉如鼫鼠。”“鼫”，馬王堆漢墓帛書本作“炙”。")
SM=("zh「凿总」取「凿」：火著肉而炙之，聲隨肉裂（推）。")
G1=[[ "䂹（𨹾）","suǒ","石","《說文》：“碎石磒聲。从石炙聲。所責切。”碎石墜落的聲音。不確，應同“庶”，指燒紅的石頭，先民在沒有發明出陶器之前，用燒紅的石頭煨煮食物。《正字通》：“按䂹訓石隕聲無義。一說讀若炙，燒石炙物也。”"],
     ["𣇧","zhè","日","《集韻》：“日赫。”"],
     ["𣶋","zhè","肉","《類篇》：“𦞦屬。”肉羹類。"]]
G2=[[ "𠶨","xī","口","《海篇》：“音希。和聲。”"],
     ["𨂂（蹠）","zhí","足","《字彙》：“與蹠同。又𨂂盭。”腳掌。《篇海》：“足履踐也。”《直音篇》：“蹠，跳也；𨂂，同上。”xuě，石土自隕。即土石被風化而墜落之意。"]]
def tab(rows):
    out=["| 字 | 讀音 | 類屬 | 取義落點 |","|---|---|---|---|"]
    for r in rows: out.append("| %s | %s | %s | %s |"%tuple(r))
    return "\n".join(out)
FT=("①指炙烤之狀\n\n"+tab(G1)+"\n\n②借聲表音\n\n"+tab(G2))
secs=[{"key":"benyi","label":"本義","text":BEN},
      {"key":"zhuanyi","label":"轉義","text":ZY},
      {"key":"yinyuan","label":"音源","text":YY},
      {"key":"shengmu","label":"聲母擬態","text":SM},
      {"key":"zizu","label":"字族衍義","text":FT}]
card={"char":"炙","head":"炙（熫䑑𦜡𦠁𤐬𤒗𦛧）","pinyin":"zhì","level":1,"parent":None,"bus":BUS,
      "aliases":["熫","䑑","𦜡","𦠁","𤐬","𤒗","𦛧"],"noRoot":False,
      "sections":secs,"卷":"卷七 斤（第47部 炙）","卷key":"17? "}
json.dump(card,io.open(os.path.join(C,"炙.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
# 族字卡
fam=[("䂹","suǒ","石","《說文》：“碎石磒聲。从石炙聲。所責切。”碎石墜落的聲音。不確，應同“庶”，指燒紅的石頭，先民在沒有發明出陶器之前，用燒紅的石頭煨煮食物。《正字通》：“按䂹訓石隕聲無義。一說讀若炙，燒石炙物也。”","sh「失收」取「收」：燒石聚熱以煨煮（推）。"),
     ("𠶨","xī","口","《海篇》：“音希。和聲。”","x「續消」取「續」：和聲相續而應（推）。"),
     ("𣇧","zhè","日","《集韻》：“日赫。”","zh「凿总」取「凿」：日灼如炙而赫烈（推）。"),
     ("𣶋","zhè","肉","《類篇》：“𦞦屬。”肉羹類。","zh「凿总」取「凿」：肉炙而成羹，濃厚（推）。"),
     ("𨂂","zhí","足","《字彙》：“與蹠同。又𨂂盭。”腳掌。《篇海》：“足履踐也。”《直音篇》：“蹠，跳也；𨂂，同上。”xuě，石土自隕。即土石被風化而墜落之意。","zh「凿总」取「凿」：足掌著地如炙之貼（推）。")]
for ch,py,lei,txt,sm in fam:
    c={"char":ch,"head":ch,"pinyin":py,"level":3,"parent":"炙","bus":BUS,"aliases":[],
       "sections":[{"key":"benyi","label":"釋義","text":txt},{"key":"shengmu","label":"聲母擬態","text":sm}],
       "卷":"卷七 斤（第47部 炙）"}
    json.dump(c,io.open(os.path.join(C,ch+".json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
# glyph index
ip=os.path.join(G,"index.json"); gi=json.load(io.open(ip,encoding="utf-8"))
gi["炙"]={"doc":"卷七 斤","files":files}
json.dump(gi,io.open(ip,"w",encoding="utf-8"),ensure_ascii=False)
print("glyphs",files,"cards ok")