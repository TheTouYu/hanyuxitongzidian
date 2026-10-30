# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
G=r"D:\系统汉字\web\public\glyphs"; C=r"D:\系统汉字\web\public\cards"
doc=Document(r"D:\字谱智能体\卷六  鶴.docx"); parts=doc.part.related_parts
p=os.path.join(C,"篧.json")
d=json.load(io.open(p,encoding="utf-8")) if os.path.exists(p) else {"char":"篧","level":3,"parent":"霍","bus":[{"num":39,"name":"隺"}],"sections":[]}
D=os.path.join(G,"inline","篧","shiyi"); os.makedirs(D,exist_ok=True)
for f in os.listdir(D): os.remove(os.path.join(D,f))
buf=[]; n=0
for el in doc.paragraphs[50]._p.iter():
    tag=el.tag.split("}")[-1]
    if tag=="t": buf.append(el.text or "")
    elif tag=="blip":
        rid=[v for a,v in el.attrib.items() if a.endswith("}embed") or a.endswith("}id")]
        if rid:
            b=parts[rid[0]].blob
            ext="png" if b[:4]==b"\x89PNG" else ("jpg" if b[:2]==b"\xff\xd8" else "bin")
            n+=1; open(os.path.join(D,"%02d.%s"%(n,ext)),"wb").write(b)
            buf.append("{{shiyi/%02d.%s}}"%(n,ext))
txt="".join(buf).strip()
if txt.startswith("篧"): pass
secs=d.get("sections") or []
hit=False
for s in secs:
    if s.get("key")=="shiyi": s["text"]=txt; s["gdir"]="inline/篧"; hit=True
if not hit: secs.insert(0,{"key":"shiyi","label":"释义","text":txt,"gdir":"inline/篧"})
d["sections"]=secs
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("imgs",n,"txt",txt[:60])