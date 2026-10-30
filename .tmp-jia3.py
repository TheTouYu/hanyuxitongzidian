# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
doc=Document(r"D:\字谱智能体\卷五  雁.docx")
seen=[]; period=False; before=0; after=0
for el in doc.paragraphs[465]._p.iter():
    tg=el.tag.split("}")[-1]
    if tg=="t":
        t=el.text or ""
        if "。" in t: period=True
    elif tg=="blip":
        rid=[v for a,v in el.attrib.items() if a.endswith("}embed") or a.endswith("}id")]
        if rid and rid[0] not in seen:
            seen.append(rid[0])
            if period: after+=1
            else: before+=1
print("before",before,"after",after,"total",len(seen))