# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
ROOT=r"D:\系统汉字"; G=os.path.join(ROOT,"web","public","glyphs")
doc=Document(r"D:\字谱智能体\卷四  弋.docx"); parts=doc.part.related_parts
def kd(b):
    return "png" if b[:4]==b"\x89PNG" else ("emf" if b[:4]==b"\x01\x00\x00\x00" else ("jpg" if b[:2]==b"\xff\xd8" else "bin"))
blobs=[]
for el in doc.paragraphs[264]._p.iter():
    if el.tag.split("}")[-1]=="blip":
        rid=[v for a,v in el.attrib.items() if a.endswith("}embed") or a.endswith("}id")]
        if rid:
            try: blobs.append(parts[rid[0]].blob)
            except KeyError: pass
plan=[("弔",blobs[:20]),("𨑩",blobs[20:22]),("鈟",blobs[22:25])]
idx=json.load(io.open(os.path.join(G,"index.json"),encoding="utf-8")); chars=idx.get("chars") or idx
rep={}
for ch,imgs in plan:
    d=os.path.join(G,ch); os.makedirs(d,exist_ok=True)
    for f in os.listdir(d): os.remove(os.path.join(d,f))
    names=[]
    for i,b in enumerate(imgs,1):
        fn="%02d.%s"%(i,kd(b)); open(os.path.join(d,fn),"wb").write(b); names.append(fn)
    e=chars.get(ch) or {"doc":"","variants":[]}; e["files"]=names; chars[ch]=e; rep[ch]=len(names)
json.dump({"chars":chars},io.open(os.path.join(G,"index.json"),"w",encoding="utf-8"),ensure_ascii=False)
print(len(blobs),rep)