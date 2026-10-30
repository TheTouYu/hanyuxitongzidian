# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
G=r"D:\系统汉字\web\public\glyphs"; P=os.path.join(G,"photos")
doc=Document(r"D:\字谱智能体\卷七  斤.docx"); parts=doc.part.related_parts
def blobs(k):
    out=[]
    for el in doc.paragraphs[k]._p.iter():
        if el.tag.split("}")[-1]=="blip":
            rid=[v for a,v in el.attrib.items() if a.endswith("}embed") or a.endswith("}id")]
            if rid: out.append(parts[rid[0]].blob)
    return out
for k,tag in ((250,"250"),(277,"277")):
    b=blobs(k)
    print(k,len(b),[len(x) for x in b])
    d=os.path.join(P,"庶"); os.makedirs(d,exist_ok=True)
    for i,x in enumerate(b):
        ext="png" if x[:4]==b"\x89PNG" else "jpg"
        open(os.path.join(d,"%s_%02d.%s"%(tag,i+1,ext)),"wb").write(x)