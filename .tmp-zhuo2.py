# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
G=r"D:\系统汉字\web\public\glyphs"; C=r"D:\系统汉字\web\public\cards"
doc=Document(r"D:\字谱智能体\卷六  鶴.docx"); parts=doc.part.related_parts
D=os.path.join(G,"inline","篧","shiyi"); os.makedirs(D,exist_ok=True)
for f in os.listdir(D): os.remove(os.path.join(D,f))
buf=[]; n=0
for el in doc.paragraphs[50]._p.iter():
    tag=el.tag.split("}")[-1]
    if tag=="t": buf.append(el.text or "")
    elif tag in ("blip","imagedata"):
        rid=[v for a,v in el.attrib.items() if a.endswith("}embed") or a.endswith("}id")]
        if rid:
            try: b=parts[rid[0]].blob
            except KeyError: continue
            ext="png" if b[:4]==b"\x89PNG" else ("jpg" if b[:2]==b"\xff\xd8" else ("emf" if b[:4]==b"\x01\x00\x00\x00" else "bin"))
            n+=1; fn="%02d.%s"%(n,ext); open(os.path.join(D,fn),"wb").write(b)
            buf.append("{{shiyi/%s}}"%fn)
txt="".join(buf).strip()
p=os.path.join(C,"篧.json"); d=json.load(io.open(p,encoding="utf-8"))
for s in d.get("sections") or []:
    if s.get("key")=="shiyi": s["text"]=txt; s["gdir"]="inline/篧"
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("n",n,"txt",txt[:80])