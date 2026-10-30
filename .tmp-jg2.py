# -*- coding: utf-8 -*-
import json,io,os,shutil,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
G=r"D:\系统汉字\web\public\glyphs"
doc=Document(r"D:\字谱智能体\卷七  斤.docx"); parts=doc.part.related_parts
blobs=[]
for el in doc.paragraphs[31]._p.iter():
    if el.tag.split("}")[-1]=="blip":
        rid=[v for a,v in el.attrib.items() if a.endswith("}embed") or a.endswith("}id")]
        if rid: blobs.append(parts[rid[0]].blob)
print("blobs",len(blobs))
for d in ("斤","昕"):
    p=os.path.join(G,d)
    if os.path.isdir(p):
        for f in os.listdir(p): os.remove(os.path.join(p,f))
def save(chunk,ch):
    p=os.path.join(G,ch); os.makedirs(p,exist_ok=True); out=[]
    for i,b in enumerate(chunk):
        ext="png" if b[:4]==b"\x89PNG" else "jpg"; fn="%02d.%s"%(i+1,ext)
        open(os.path.join(p,fn),"wb").write(b); out.append(ch+"/"+fn)
    return out
A=save(blobs[:7],"斤"); B=save(blobs[7:],"昕")
ix=json.load(io.open(os.path.join(G,"index.json"),encoding="utf-8")); ch=ix["chars"]
ch["斤"]["files"]=A; ch.setdefault("昕",{})["files"]=B
json.dump({"chars":ch},io.open(os.path.join(G,"index.json"),"w",encoding="utf-8"),ensure_ascii=False)
print(len(A),len(B))