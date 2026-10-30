# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
C=r"D:\系统汉字\web\public\cards"
ps=[p.text.strip() for p in Document(r"D:\字谱智能体\卷三  矢.docx").paragraphs]
def strip(t):
    for q in ("本義：","轉義：","字族衍義："):
        if t.startswith(q): return t[len(q):].lstrip()
    return t
VOL={"key":"suoshujuan","label":"所属卷","text":"","cites":[],"links":[{"ch":"卷三矢","label":"卷三 矢"}]}
rows=[["𩻼","zhì","魚","《集韻》『直例切，音滯。魚名』；《正字通》『一說俗因河豚臆造𩻼字。非是』；應指河豚"],
["璏","zhì","玉","《說文》『劍鼻玉也。从玉，彘聲。直例切』；劍匣旁穿繫皮帶的有孔玉石"]]
z={"char":"彘","head":"彘（𠅰𢑣𥏉）","pinyin":"zhì","level":2,"parent":"矢","bus":[{"num":16,"name":"矢"}],"rootLevel":2,
"aliases":["𠅰","𢑣","𥏉"],"sections":[
 {"key":"benyi","label":"本义","text":strip(ps[267]),"cites":[]},
 {"key":"zhuanyi","label":"转义","text":strip(ps[268]),"cites":[]},
 {"key":"shengmu","label":"声母拟态","text":"zh「凿总」取「凿」：矢鑿入豕體，貫而制之（推）。","cites":[]},
 {"key":"zizu","label":"字族衍义","text":"原文：指野豬貫矢之狀","cites":[],
  "groups":[{"title":"指野豬貫矢之狀","note":"","rows":rows}]},VOL]}
json.dump(z,io.open(os.path.join(C,"彘.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
M={"𩻼":"zh「凿总」取「凿」：河豚皮刺如貫矢之豬（推）。","璏":"zh「凿总」取「凿」：玉鼻穿帶而鑿孔（推）。"}
for r in rows:
    ch=r[0]
    d={"char":ch,"head":ch,"pinyin":r[1],"level":3,"parent":"彘","bus":[{"num":16,"name":"矢"}],
       "sections":[{"key":"shiyi","label":"释义","text":r[3],"cites":[]},
         {"key":"shengmu","label":"声母拟态","text":M[ch],"cites":[]},VOL]}
    json.dump(d,io.open(os.path.join(C,ch+".json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("彘+族",len(rows))