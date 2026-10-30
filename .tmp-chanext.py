# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
G=r"D:\系统汉字\web\public\glyphs"; C=r"D:\系统汉字\web\public\cards"
doc=Document(r"D:\字谱智能体\卷五  雁.docx"); parts=doc.part.related_parts
d=os.path.join(G,"產"); os.makedirs(d,exist_ok=True)
for f in os.listdir(d):
    if f.lower().endswith((".png",".jpg",".emf")): os.remove(os.path.join(d,f))
n=0; files=[]
for el in doc.paragraphs[327]._p.iter():
    if el.tag.split("}")[-1]=="blip":
        rid=[v for a,v in el.attrib.items() if a.endswith("}embed") or a.endswith("}id")]
        if rid:
            b=parts[rid[0]].blob; n+=1; ext="png" if b[:4]==b"\x89PNG" else "jpg"
            fn="%02d.%s"%(n,ext); open(os.path.join(d,fn),"wb").write(b); files.append("產/"+fn)
ix=json.load(io.open(os.path.join(G,"index.json"),encoding="utf-8")); ch=ix["chars"]
ch["產"]={"doc":"卷五  雁.docx","variants":["𨹞","産","产"],"files":files}
json.dump({"chars":ch},io.open(os.path.join(G,"index.json"),"w",encoding="utf-8"),ensure_ascii=False)
print("glyphs",len(files))