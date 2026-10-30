# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
C=r"D:\系统汉字\web\public\cards"
ps=[p.text.strip() for p in Document(r"D:\字谱智能体\卷二  㠯.docx").paragraphs]
cands=[(k,t) for k,t in enumerate(ps[745:790],start=745) if t and not t.startswith(("①","②","③","▲","字族","本義","轉義","辯證","音源"))]
n=0
for fn in os.listdir(C):
    if not fn.endswith(".json") or fn=="index.json": continue
    p=os.path.join(C,fn); d=json.load(io.open(p,encoding="utf-8"))
    if d.get("parent")!="斦": continue
    ch=d["char"]; best=None
    for k,t in cands:
        if t.startswith(ch):
            rest=t[len(ch):].lstrip("（")
            if rest[:1] and (rest[:1].isascii() or rest[:1]=="（"): best=t; break
    if not best: print("未找到",ch); continue
    for s in d["sections"]:
        if s["key"]=="shiyi": s["text"]=best
    json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("修正",n)