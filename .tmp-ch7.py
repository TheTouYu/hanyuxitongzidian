# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
ps=[p.text.strip() for p in Document(r"D:\字谱智能体\卷五  雁.docx").paragraphs]
paras=[ps[k] for k in (217,218,219,220,221,222)]
txt="\n\n".join(p.replace("辯證：","",1) for p in paras)
p=r"D:\系统汉字\web\public\cards\厂.json"
d=json.load(io.open(p,encoding="utf-8"))
for s in d["sections"]:
    if s.get("key")=="bianzheng": s["text"]=txt
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print(txt[:80])