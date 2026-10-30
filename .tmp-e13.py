# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
G=r"D:\系统汉字\web\public\glyphs"
doc=Document(r"D:\字谱智能体\卷五  雁.docx"); parts=doc.part.related_parts
blobs=[]
for el in doc.paragraphs[393]._p.iter():
    if el.tag.split("}")[-1]=="blip":
        rid=[v for a,v in el.attrib.items() if a.endswith("}embed") or a.endswith("}id")]
        if rid: blobs.append(parts[rid[0]].blob)
def dump(ch,bs):
    d=os.path.join(G,ch); os.makedirs(d,exist_ok=True)
    for f in os.listdir(d):
        if f.lower().endswith((".png",".jpg")): os.remove(os.path.join(d,f))
    out=[]
    for i,b in enumerate(bs):
        ext="png" if b[:4]==b"\x89PNG" else "jpg"
        fn="%02d.%s"%(i+1,ext); open(os.path.join(d,fn),"wb").write(b); out.append(ch+"/"+fn)
    return out
wo=dump("我",blobs[:12]); e=dump("娥",blobs[12:])
ix=json.load(io.open(os.path.join(G,"index.json"),encoding="utf-8")); ch=ix["chars"]
ch["我"]["files"]=wo; ch["娥"]["files"]=e
json.dump({"chars":ch},io.open(os.path.join(G,"index.json"),"w",encoding="utf-8"),ensure_ascii=False)
print(len(wo),len(e))