# -*- coding: utf-8 -*-
import sys,os,json,io,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
G=r"D:\系统汉字\web\public\glyphs"; C=r"D:\系统汉字\web\public\cards"
doc=Document(r"D:\字谱智能体\卷五  雁.docx"); parts=doc.part.related_parts
d=os.path.join(G,"彥"); os.makedirs(d,exist_ok=True)
for f in os.listdir(d): os.remove(os.path.join(d,f))
n=0
for el in doc.paragraphs[282]._p.iter():
    if el.tag.split("}")[-1]=="blip":
        rid=[v for a,v in el.attrib.items() if a.endswith("}embed") or a.endswith("}id")]
        if rid:
            b=parts[rid[0]].blob; n+=1
            ext="png" if b[:4]==b"\x89PNG" else "jpg"
            open(os.path.join(d,"%02d.%s"%(n,ext)),"wb").write(b)
print("glyphs",n)