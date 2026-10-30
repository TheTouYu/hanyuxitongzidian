# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
G=r"D:\系统汉字\web\public\glyphs"
doc=Document(r"D:\字谱智能体\卷五  雁.docx"); parts=doc.part.related_parts
blobs=[]
for el in doc.paragraphs[282]._p.iter():
    if el.tag.split("}")[-1]=="blip":
        rid=[v for a,v in el.attrib.items() if a.endswith("}embed") or a.endswith("}id")]
        if rid: blobs.append(parts[rid[0]].blob)
print("blobs",len(blobs))
def dump(ch, idx):
    d=os.path.join(G,ch); os.makedirs(d,exist_ok=True)
    for f in os.listdir(d):
        if f.lower().endswith((".png",".jpg",".emf")): os.remove(os.path.join(d,f))
    out=[]
    for i,k in enumerate(idx):
        b=blobs[k]; ext="png" if b[:4]==b"\x89PNG" else ("jpg" if b[:2]==b"\xff\xd8" else "bin")
        fn="%02d.%s"%(i+1,ext); open(os.path.join(d,fn),"wb").write(b); out.append(ch+"/"+fn)
    return out
F={}
F["彥"]=dump("彥", range(0,6))
F["顏"]=dump("顏", range(6,8))
F["云"]=dump("云", range(8,9))
ip=os.path.join(G,"index.json"); ix=json.load(io.open(ip,encoding="utf-8")); ch=ix["chars"]
for k,v in F.items():
    e=ch.get(k) or {"doc":"卷五  雁.docx","variants":[]}
    e["files"]=v; ch[k]=e
json.dump({"chars":ch},io.open(ip,"w",encoding="utf-8"),ensure_ascii=False)
print(F)