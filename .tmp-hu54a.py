# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
G=r"D:\系统汉字\web\public\glyphs"; C=r"D:\系统汉字\web\public\cards"; P=os.path.join(G,"photos")
doc=Document(r"D:\字谱智能体\卷八  虎.docx"); parts=doc.part.related_parts
# 字形 p120
d=os.path.join(G,"虖"); os.makedirs(d,exist_ok=True)
for f in os.listdir(d): os.remove(os.path.join(d,f))
fs=[];n=0
for el in doc.paragraphs[120]._p.iter():
    if el.tag.split("}")[-1]=="blip":
        rid=[v for a,v in el.attrib.items() if a.endswith("}embed") or a.endswith("}id")]
        if rid:
            b=parts[rid[0]].blob
            if len(b)>=1200:
                n+=1; fn="%02d.png"%n; open(os.path.join(d,fn),"wb").write(b); fs.append("虖/"+fn)
idx=json.load(io.open(os.path.join(G,"index.json"),encoding="utf-8"))
idx.setdefault("chars",{})["虖"]={"doc":"卷八 虎","files":fs}
json.dump(idx,io.open(os.path.join(G,"index.json"),"w",encoding="utf-8"),ensure_ascii=False)
# 插图 p143 → 㯉
dd=os.path.join(P,"㯉"); os.makedirs(dd,exist_ok=True)
for f in os.listdir(dd): os.remove(os.path.join(dd,f))
for el in doc.paragraphs[142]._p.iter():
    if el.tag.split("}")[-1]=="blip":
        rid=[v for a,v in el.attrib.items() if a.endswith("}embed") or a.endswith("}id")]
        if rid:
            b=parts[rid[0]].blob; ext="png" if b[:4]==b"\x89PNG" else "jpg"
            open(os.path.join(dd,"01."+ext),"wb").write(b); break
for name,key,val in (("index.json","photos",{"㯉":["01.jpg"]}),("captions.json","captions",{"㯉":["表皮開裂的樺樹"]})):
    p=os.path.join(P,name); x=json.load(io.open(p,encoding="utf-8")); m=x.get(key) or x
    m.update(val); json.dump({key:m},io.open(p,"w",encoding="utf-8"),ensure_ascii=False)
gi=json.load(io.open(os.path.join(G,"index.json"),encoding="utf-8"))
gi.setdefault("photos",{})["㯉"]=[{"file":"photos/㯉/01.jpg","caption":"表皮開裂的樺樹"}]
json.dump(gi,io.open(os.path.join(G,"index.json"),"w",encoding="utf-8"),ensure_ascii=False)
print("glyphs",len(fs))