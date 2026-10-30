# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
doc=Document(r"D:\字谱智能体\卷五  雁.docx")
seq=[]
for el in doc.paragraphs[465]._p.iter():
    tg=el.tag.split("}")[-1]
    if tg=="t" and (el.text or "").strip(): seq.append(("T",el.text))
    elif tg in ("blip","blipFill"): seq.append(("I",""))
    elif tg=="blip":
        pass
print(len([s for s in seq if s[0]=="I"]))
print("".join("■" if t=="I" else x for t,x in seq)[:400])