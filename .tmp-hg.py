# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
G=r"D:\系统汉字\web\public\glyphs"
doc=Document(r"D:\字谱智能体\卷六  鶴.docx"); parts=doc.part.related_parts
d=os.path.join(G,"靃"); os.makedirs(d,exist_ok=True)
for f in os.listdir(d): os.remove(os.path.join(d,f))
n=0
for el in doc.paragraphs[114]._p.iter():
    if el.tag.split("}")[-1]=="blip":
        rid=[v for a,v in el.attrib.items() if a.endswith("}embed") or a.endswith("}id")]
        if rid:
            b=parts[rid[0]].blob
            if len(b)<400: continue
            ext="png" if b[:4]==b"\x89PNG" else ("jpg" if b[:2]==b"\xff\xd8" else "bin")
            n+=1; open(os.path.join(d,"%02d.%s"%(n,ext)),"wb").write(b)
ix=json.load(io.open(os.path.join(G,"index.json"),encoding="utf-8")); chrs=ix["chars"]
files=sorted(os.listdir(d)); fl=["靃/"+x for x in files]
chrs["靃"]={"doc":"","variants":[],"files":fl}; chrs["霍"]={"doc":"","variants":[],"files":fl}
json.dump({"chars":chrs},io.open(os.path.join(G,"index.json"),"w",encoding="utf-8"),ensure_ascii=False)
print("extracted",n,files[:4])