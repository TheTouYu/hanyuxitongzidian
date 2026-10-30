# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
G=r"D:\系统汉字\web\public\glyphs"
doc=Document(r"D:\字谱智能体\卷七  斤.docx"); parts=doc.part.related_parts
def kd(b): return "png" if b[:4]==b"\x89PNG" else ("jpg" if b[:2]==b"\xff\xd8" else "emf")
def grab(k):
    out=[]
    for el in doc.paragraphs[k]._p.iter():
        if el.tag.split("}")[-1]=="blip":
            rid=[v for a,v in el.attrib.items() if a.endswith("}embed") or a.endswith("}id")]
            if rid: out.append(parts[rid[0]].blob)
    return out
for ch,k,split in (("乇",286,17),("宅",341,10)):
    d=os.path.join(G,ch); os.makedirs(d,exist_ok=True)
    for f in os.listdir(d): os.remove(os.path.join(d,f))
    for i,b in enumerate(grab(k)[:split],1):
        open(os.path.join(d,"%02d.%s"%(i,kd(b))),"wb").write(b)
    print(ch,len(os.listdir(d)))
ip=os.path.join(G,"index.json"); x=json.load(io.open(ip,encoding="utf-8"))
for ch in ("乇","宅"):
    fs=sorted(os.listdir(os.path.join(G,ch)))
    x.setdefault("chars",{})[ch]={"doc":"卷七 斤","files":[ch+"/"+f for f in fs]}
json.dump(x,io.open(ip,"w",encoding="utf-8"),ensure_ascii=False)
print("index ok")