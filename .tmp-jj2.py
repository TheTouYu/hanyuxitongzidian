# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
G=r"D:\系统汉字\web\public\glyphs"
doc=Document(r"D:\字谱智能体\卷七  斤.docx"); parts=doc.part.related_parts
blobs=[]
for el in doc.paragraphs[194]._p.iter():
    if el.tag.split("}")[-1]=="blip":
        rid=[v for a,v in el.attrib.items() if a.endswith("}embed") or a.endswith("}id")]
        if rid: blobs.append(parts[rid[0]].blob)
print("total",len(blobs))
# 叚: 1-16; 豭: 17-19
d=os.path.join(G,"豭"); os.makedirs(d,exist_ok=True)
for f in os.listdir(d): os.remove(os.path.join(d,f))
tail=blobs[16:]
for i,b in enumerate(tail):
    ext="png" if b[:4]==b"\x89PNG" else "jpg"
    open(os.path.join(d,"%02d.%s"%(i+1,ext)),"wb").write(b)
# 叚 补到 16 形
d2=os.path.join(G,"叚"); os.makedirs(d2,exist_ok=True)
for f in os.listdir(d2): os.remove(os.path.join(d2,f))
for i,b in enumerate(blobs[:16]):
    ext="png" if b[:4]==b"\x89PNG" else "jpg"
    open(os.path.join(d2,"%02d.%s"%(i+1,ext)),"wb").write(b)
p=os.path.join(G,"index.json"); g=json.load(io.open(p,encoding="utf-8")); ch=g["chars"]
ch.setdefault("叚",{})["files"]=["叚/%02d.png"%(i+1) for i in range(16)]
ch.setdefault("豭",{})["files"]=["豭/%02d.png"%(i+1) for i in range(len(tail))]
json.dump({"chars":ch},io.open(p,"w",encoding="utf-8"),ensure_ascii=False)
print("叚",16,"豭",len(tail))