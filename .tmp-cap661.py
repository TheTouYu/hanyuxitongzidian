# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
C=r"D:\系统汉字\web\public\cards"
ps=[p.text.strip() for p in Document(r"D:\字谱智能体\卷三  矢.docx").paragraphs]
def strip(t):
    for q in ("本義：","轉義：","辯證：","音源："):
        if t.startswith(q): return t[len(q):].lstrip()
    return t
rows=[["倒","dǎo/dào","人","《新附》「仆也。从人到聲。當老切。」dào，《集韻》「顛倒也」"],
["菿","dào/dǎo","艸","《說文》「艸木倒。从艸到聲。都盜切」"],
["𠕥（𠕭）","dào","冃","《集韻》「𠕭，覆具。或从到」"],
["捯","dǎo/dáo","手","《集韻》引《說文》「手推也。一曰築也」；dáo，兩手不住倒換拉繩"],
["𠴼","dào","口","《字彙補》「音到。𠴼喇者，掐撥數唱，雜劇之名」"],
["𥓫","dào","石","《海篇》「石名」"],
["𧌼（蛭）","zhì","虫","《字彙補》「本蛭字之誤」"],
["𧼤","dào","走","《龍龕》「音到」疑指倒退"]]
z={"char":"到","head":"到（𠀉到）","pinyin":"dào（又 zhì）","level":2,"parent":"矢","bus":[{"num":16,"name":"矢"}],"rootLevel":2,
"aliases":["侄"],"sections":[
 {"key":"benyi","label":"本义","text":strip(ps[228]),"cites":[]},
 {"key":"zhuanyi","label":"转义","text":strip(ps[229]),"cites":[]},
 {"key":"bianzheng","label":"辩证","text":strip(ps[230]),"cites":[]},
 {"key":"yinyuan","label":"音源","text":strip(ps[231]),"cites":[]},
 {"key":"shengmu","label":"声母拟态","text":"d「囤动」取「囤」：行至而囤止其所（推）。","cites":[]},
 {"key":"zizu","label":"字族衍义","text":"原文字族衍義：多指顛倒、仆倒。","cites":[],
  "groups":[{"title":"多指顛倒、仆倒","note":"","rows":[r[:4] for r in rows]}]},
 {"key":"suoshujuan","label":"所属卷","text":"","cites":[],"links":[{"ch":"卷三矢","label":"卷三 矢"}]}]}
json.dump(z,io.open(os.path.join(C,"到.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
M={"倒":"d「囤动」取「囤」：仆倒而囤地（推）。","菿":"d「囤动」取「囤」：艸木倒伏囤地（推）。",
"𠕥":"d「囤动」取「囤」：覆具覆而囤（推）。","捯":"d「囤动」取「囤」：手推而囤聚（推）。",
"𠴼":"d「囤动」取「囤」：掐撥數唱，囤而不散（推）。","𥓫":"d「囤动」取「囤」：石名，借聲（推）。",
"𧌼":"zh「凿总」取「凿」：蛭之誤字，吸盤鑿入（推）。","𧼤":"d「囤动」取「囤」：倒退而囤（推）。"}
n=0
for r in rows:
    ch=r[0]; base=re.sub(r"（.*?）","",ch) if False else ch.split("（")[0]
    par=ch[len(base)+1:-1] if "（" in ch else ""
    d={"char":base,"head":ch,"pinyin":r[1],"level":3,"parent":"到","bus":[{"num":16,"name":"矢"}],"aliases":list(par) if par else [],
       "sections":[{"key":"shiyi","label":"释义","text":f"{r[0]}{r[1]}《原文》「{r[3]}」","cites":[]},
         {"key":"shengmu","label":"声母拟态","text":M[ch],"cites":[]},
         {"key":"suoshujuan","label":"所属卷","text":"","cites":[],"links":[{"ch":"卷三矢","label":"卷三 矢"}]}]}
    json.dump(d,io.open(os.path.join(C,base+".json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("到卡+族",n)