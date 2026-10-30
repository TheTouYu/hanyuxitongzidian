# -*- coding: utf-8 -*-
import json,io,os,sys,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
d=json.load(io.open(r"D:\系统汉字\web\public\cards\蛤.json",encoding="utf-8"))
print(d.get("head"), d.get("level"), d.get("parent"), d.get("bus"), d.get("aliases"))
print([ (s["key"], s.get("text","")[:80]) for s in d["sections"]][:4])
for f in ("卷七  斤.docx","卷六  鶴.docx"):
    doc=Document(os.path.join(r"D:\字谱智能体",f))
    for k,p in enumerate(doc.paragraphs):
        t=p.text.strip()
        if t.startswith("蛒") or "蛒" in t[:6]:
            print(f,k,t[:90])