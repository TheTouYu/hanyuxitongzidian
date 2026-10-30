# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
G=r"D:\系统汉字\web\public\glyphs"; P=os.path.join(G,"photos")
doc=Document(r"D:\字谱智能体\卷三  矢.docx"); parts=doc.part.related_parts; ps=doc.paragraphs
ni=json.load(io.open(os.path.join(G,"index.json"),encoding="utf-8")); cm=ni.get("chars") or ni
d=os.path.join(G,"射"); os.makedirs(d,exist_ok=True)
for f in os.listdir(d): os.remove(os.path.join(d,f))
n=0
for el in ps[717]._p.iter():
    for a,v in el.attrib.items():
        if a.endswith("}embed") or a.endswith("}id"):
            try: b=parts[v].blob
            except KeyError: continue
            if len(b)<800: continue
            ext=".png" if b[:4]==b"\x89PNG" else ".jpg"
            open(os.path.join(d,f"{n+1:02d}{ext}"),"wb").write(b); n+=1
if n: cm["射"]={"doc":"卷三 矢","files":[f"射/{f}" for f in sorted(os.listdir(d))]}
json.dump({"chars":cm},io.open(os.path.join(G,"index.json"),"w",encoding="utf-8"),ensure_ascii=False)
# 插图
pi=json.load(io.open(os.path.join(P,"index.json"),encoding="utf-8")); ph=pi["photos"]
pm=os.path.join(P,"射"); os.makedirs(pm,exist_ok=True)
got=None
for k in (719,720):
    for el in ps[k]._p.iter():
        for a,v in el.attrib.items():
            if a.endswith("}embed") or a.endswith("}id"):
                try: b=parts[v].blob
                except KeyError: continue
                if len(b)>20000 and not got:
                    ext=".png" if b[:4]==b"\x89PNG" else ".jpg"
                    open(os.path.join(pm,"01"+ext),"wb").write(b); got=(k,ext,len(b))
if got:
    ph["射"]=["01"+got[1]]
    json.dump({"photos":ph},io.open(os.path.join(P,"index.json"),"w",encoding="utf-8"),ensure_ascii=False)
print("glyphs",n,"photo",got)