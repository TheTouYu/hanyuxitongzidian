# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
ps=[p.text.strip() for p in Document(r"D:\字谱智能体\卷六  鶴.docx").paragraphs]
def sl(t,lab): return re.sub(r'^%s[：:]'%lab,'',t.strip()).strip()
parts=[]
for k in range(262,267):
    t=ps[k]
    if not t or t.startswith("▲"): continue
    parts.append(sl(t,"本義"))
txt="\n".join(parts)
p=r"D:\系统汉字\web\public\cards\或.json"; d=json.load(io.open(p,encoding="utf-8"))
for s in d["sections"]:
    if s["key"]=="benyi": s["text"]=txt
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print(len(txt),parts.__len__())