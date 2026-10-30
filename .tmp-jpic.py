# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
G=r"D:\系统汉字\web\public\glyphs\photos"
doc=Document(r"D:\字谱智能体\卷六  鶴.docx"); parts=doc.part.related_parts
def take(k,chars):
    for el in doc.paragraphs[k]._p.iter():
        if el.tag.split("}")[-1]=="blip":
            rid=[v for a,v in el.attrib.items() if a.endswith("}embed") or a.endswith("}id")]
            if rid:
                b=parts[rid[0]].blob; ext="png" if b[:4]==b"\x89PNG" else "jpg"
                for ch in chars:
                    d=os.path.join(G,ch); os.makedirs(d,exist_ok=True)
                    for f in os.listdir(d): os.remove(os.path.join(d,f))
                    open(os.path.join(d,"01."+ext),"wb").write(b)
                return ext
print("矍",take(194,["矍"]))
print("貜",take(205,["貜"]))
ix=json.load(io.open(os.path.join(G,"index.json"),encoding="utf-8")); ph=ix["photos"]
for ch,ext in (("矍","png"),("貜","png")):
    pass