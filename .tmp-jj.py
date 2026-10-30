# -*- coding: utf-8 -*-
import sys,os
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
doc=Document(r"D:\字谱智能体\卷七  斤.docx"); parts=doc.part.related_parts
n=0; os.makedirs(r"D:\系统汉字\.tmp-jj",exist_ok=True)
for el in doc.paragraphs[194]._p.iter():
    if el.tag.split("}")[-1]=="blip":
        rid=[v for a,v in el.attrib.items() if a.endswith("}embed") or a.endswith("}id")]
        n+=1
        if n>=17:
            b=parts[rid[0]].blob
            ext="png" if b[:4]==b"\x89PNG" else "jpg"
            open(r"D:\系统汉字\.tmp-jj\%02d.%s"%(n,ext),"wb").write(b)
print("done")