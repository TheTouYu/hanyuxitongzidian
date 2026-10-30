# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
G=r"D:\系统汉字\web\public\glyphs"; C=r"D:\系统汉字\web\public\cards"
doc=Document(r"D:\字谱智能体\卷六  鶴.docx"); parts=doc.part.related_parts
best=None
for k in range(60,114):
    n=sum(1 for el in doc.paragraphs[k]._p.iter() if el.tag.split("}")[-1]=="blip")
    t=doc.paragraphs[k].text.strip()
    if n>=5 and ("霍" in t or "靃" in t): print("cand",k,n,t[:40]); best=k; break
if best:
    d=os.path.join(G,"靃"); os.makedirs(d,exist_ok=True)
    for f in os.listdir(d): os.remove(os.path.join(d,f))
    i=0
    for el in doc.paragraphs[best]._p.iter():
        if el.tag.split("}")[-1]=="blip":
            rid=[v for a,v in el.attrib.items() if a.endswith("}embed") or a.endswith("}id")]
            if rid:
                b=parts[rid[0]].blob
                if len(b)<400: continue
                ext="png" if b[:4]==b"\x89PNG" else ("jpg" if b[:2]==b"\xff\xd8" else "bin")
                i+=1; open(os.path.join(d,"%02d.%s"%(i,ext)),"wb").write(b)
    fl=["靃/"+x for x in sorted(os.listdir(d))]
    ix=json.load(io.open(os.path.join(G,"index.json"),encoding="utf-8")); chrs=ix["chars"]
    chrs["靃"]={"doc":"","variants":[],"files":fl}; chrs["霍"]={"doc":"","variants":[],"files":fl}
    json.dump({"chars":chrs},io.open(os.path.join(G,"index.json"),"w",encoding="utf-8"),ensure_ascii=False)
    p=os.path.join(C,"靃.json"); cd=json.load(io.open(p,encoding="utf-8"))
    cd["level"]=1; cd["bus"]=[{"num":39,"name":"隺"}]
    json.dump(cd,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    print("glyphs",len(fl))
else: print("no cand")