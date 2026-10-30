# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
G=r"D:\系统汉字\web\public\glyphs"; P=os.path.join(G,"photos")
doc=Document(r"D:\字谱智能体\卷六  鶴.docx"); parts=doc.part.related_parts
# 1) 插图
for el in doc.paragraphs[247]._p.iter():
    if el.tag.split("}")[-1]=="blip":
        rid=[v for a,v in el.attrib.items() if a.endswith("}embed") or a.endswith("}id")][0]
        b=parts[rid].blob; ext="png" if b[:4]==b"\x89PNG" else "jpg"
        d=os.path.join(P,"戈"); os.makedirs(d,exist_ok=True)
        for f in os.listdir(d): os.remove(os.path.join(d,f))
        open(os.path.join(d,"01."+ext),"wb").write(b); break
for name,key,val in (("index.json","photos",["01."+ext]),("captions.json","captions",["（原稿此圖無▲圖注）"])):
    p=os.path.join(P,name); x=json.load(io.open(p,encoding="utf-8")); m=x.get(key) or x
    m["戈"]=val; json.dump({key:m},io.open(p,"w",encoding="utf-8"),ensure_ascii=False)
# 2) 字形行拆分
seq=[]
for el in doc.paragraphs[245]._p.iter():
    tag=el.tag.split("}")[-1]
    if tag=="t" and el.text: seq.append(("t",el.text))
    elif tag=="blip":
        rid=[v for a,v in el.attrib.items() if a.endswith("}embed") or a.endswith("}id")]
        if rid: seq.append(("i",parts[rid[0]].blob))
last_dot=-1
for i,(t,v) in enumerate(seq):
    if t=="t" and "。" in v: last_dot=i
imgs=[(i,v) for i,(t,v) in enumerate(seq) if t=="i"]
ge=[v for i,v in imgs if i<last_dot]; yue=[v for i,v in imgs if i>last_dot]
def save(ch,arr):
    d=os.path.join(G,ch); os.makedirs(d,exist_ok=True)
    for f in os.listdir(d):
        if f.endswith((".png",".jpg")): os.remove(os.path.join(d,f))
    files=[]
    for j,b in enumerate(arr):
        ext="png" if b[:4]==b"\x89PNG" else "jpg"; fn="%02d.%s"%(j+1,ext)
        open(os.path.join(d,fn),"wb").write(b); files.append(ch+"/"+fn)
    ix=json.load(io.open(os.path.join(G,"index.json"),encoding="utf-8")); h=ix["chars"].get(ch) or {"doc":"","variants":[],"files":[]}
    h["files"]=files; ix["chars"][ch]=h
    json.dump({"chars":ix["chars"]},io.open(os.path.join(G,"index.json"),"w",encoding="utf-8"),ensure_ascii=False)
    return files
print("戈",len(ge),"鳶",len(yue))
save("戈",ge); save("鳶",yue)