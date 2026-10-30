# -*- coding: utf-8 -*-
import json,io,os,shutil,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
G=r"D:\系统汉字\web\public\glyphs"
# restore 反/17
shutil.move(os.path.join(G,"阪","01.png"), os.path.join(G,"反","17.png"))
doc=Document(r"D:\字谱智能体\卷五  雁.docx"); parts=doc.part.related_parts
d=os.path.join(G,"阪"); os.makedirs(d,exist_ok=True)
for f in os.listdir(d): os.remove(os.path.join(d,f))
for i,rid in enumerate(("rId147","rId148")):
    open(os.path.join(d,"%02d.png"%(i+1)),"wb").write(parts[rid].blob)
ix=json.load(io.open(os.path.join(G,"index.json"),encoding="utf-8")); ch=ix["chars"]
ch["反"]["files"]=["反/%02d.png"%(i+1) for i in range(18)]
h=ch.get("阪") or {}; h["files"]=["阪/01.png","阪/02.png"]; ch["阪"]=h
json.dump({"chars":ch},io.open(os.path.join(G,"index.json"),"w",encoding="utf-8"),ensure_ascii=False)
print("反",len(ch["反"]["files"]),"阪",h["files"])