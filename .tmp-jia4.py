# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
G=r"D:\系统汉字\web\public\glyphs"
doc=Document(r"D:\字谱智能体\卷五  雁.docx"); parts=doc.part.related_parts
seq=[]; period=False
for el in doc.paragraphs[465]._p.iter():
    tg=el.tag.split("}")[-1]
    if tg=="t" and "。" in (el.text or ""): period=True
    elif tg=="blip":
        rid=[v for a,v in el.attrib.items() if a.endswith("}embed") or a.endswith("}id")]
        if rid and all(rid[0]!=s[0] for s in seq): seq.append((rid[0],period))
a=[parts[r].blob for r,p in seq if not p]; b=[parts[r].blob for r,p in seq if p]
def dump(ch,bs):
    d=os.path.join(G,ch); os.makedirs(d,exist_ok=True)
    for f in os.listdir(d):
        if f.lower().endswith((".png",".jpg")): os.remove(os.path.join(d,f))
    o=[]
    for i,x in enumerate(bs):
        ext="png" if x[:4]==b"\x89PNG" else "jpg"; fn="%02d.%s"%(i+1,ext)
        open(os.path.join(d,fn),"wb").write(x); o.append(ch+"/"+fn)
    return o
ja=dump("加",a); jb=dump("嘉",b)
ip=os.path.join(G,"index.json"); ix=json.load(io.open(ip,encoding="utf-8")); chs=ix["chars"]
chs["加"]["files"]=ja; chs.setdefault("嘉",{"doc":"","variants":"","files":[]})["files"]=jb
json.dump(ix,io.open(ip,"w",encoding="utf-8"),ensure_ascii=False)
print("加",len(ja),"嘉",len(jb))