# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
G=r"D:\系统汉字\web\public\glyphs"; P=os.path.join(G,"photos")
doc=Document(r"D:\字谱智能体\卷八  虎.docx"); parts=doc.part.related_parts
d=os.path.join(P,"虢"); os.makedirs(d,exist_ok=True)
for f in os.listdir(d): os.remove(os.path.join(d,f))
for el in doc.paragraphs[110]._p.iter():
    if el.tag.split("}")[-1]=="blip":
        rid=[v for a,v in el.attrib.items() if a.endswith("}embed") or a.endswith("}id")]
        if rid:
            b=parts[rid[0]].blob
            ext="png" if b[:4]==b"\x89PNG" else "jpg"
            open(os.path.join(d,"01."+ext),"wb").write(b); print("saved",len(b),ext); break
for name,key,val in (("index.json","photos",["01.jpg"]),("captions.json","captions",["二虎相搏，以掌相批"])):
    p=os.path.join(P,name); x=json.load(io.open(p,encoding="utf-8")); m=x.get(key) or x
    m["虢"]=val; json.dump({key:m},io.open(p,"w",encoding="utf-8"),ensure_ascii=False)
gi=json.load(io.open(os.path.join(G,"index.json"),encoding="utf-8"))
gi.setdefault("photos",{})["虢"]=[{"file":"photos/虢/01.jpg","caption":"二虎相搏，以掌相批"}]
json.dump(gi,io.open(os.path.join(G,"index.json"),"w",encoding="utf-8"),ensure_ascii=False)
print("ok")