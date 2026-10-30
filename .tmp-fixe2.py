# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
ps=[p.text.strip() for p in Document(r"D:\字谱智能体\卷五  雁.docx").paragraphs]
p=r"D:\系统汉字\web\public\cards\戹.json"; d=json.load(io.open(p,encoding="utf-8"))
z1=ps[508].split("轉義：",1)[1]; z2=ps[509]
for s in d["sections"]:
    if s["key"]=="zhuanyi": s["text"]=z1+"\n"+z2
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print(z2)