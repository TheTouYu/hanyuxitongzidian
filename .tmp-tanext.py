# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
G=r"D:\系统汉字\web\public\glyphs"; C=r"D:\系统汉字\web\public\cards"
doc=Document(r"D:\字谱智能体\卷五  雁.docx"); parts=doc.part.related_parts
def save(dirn, kmax=None):
    d=os.path.join(G,dirn); os.makedirs(d,exist_ok=True)
    for f in os.listdir(d): os.remove(os.path.join(d,f))
    n=0
    for el in doc.paragraphs[kmax]._p.iter():
        if el.tag.split("}")[-1]=="blip":
            rid=[v for a,v in el.attrib.items() if a.endswith("}embed") or a.endswith("}id")]
            if rid:
                b=parts[rid[0]].blob; n+=1
                open(os.path.join(d,"%02d.%s"%(n,"png" if b[:4]==b"\x89PNG" else "jpg")),"wb").write(b)
    return n
n1=save("炭",311)
# photo p313
pdir=os.path.join(G,"photos","炭"); os.makedirs(pdir,exist_ok=True)
for f in os.listdir(pdir): os.remove(os.path.join(pdir,f))
ph=0
for el in doc.paragraphs[313]._p.iter():
    if el.tag.split("}")[-1]=="blip":
        rid=[v for a,v in el.attrib.items() if a.endswith("}embed") or a.endswith("}id")]
        if rid:
            b=parts[rid[0]].blob; ph+=1
            open(os.path.join(pdir,"01.%s"%("png" if b[:4]==b"\x89PNG" else "jpg")),"wb").write(b)
print("glyphs",n1,"photo",ph)