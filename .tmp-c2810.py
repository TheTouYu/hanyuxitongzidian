# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
ROOT=r"D:\系统汉字"
from docx import Document
doc=Document(r"D:\字谱智能体\卷四  弋.docx"); ps=doc.paragraphs; parts=doc.part.related_parts
G=os.path.join(ROOT,"web","public","glyphs","叔")
os.makedirs(G,exist_ok=True)
for f in os.listdir(G): os.remove(os.path.join(G,f))
n=0
for el in ps[119]._p.iter():
    for a,v in el.attrib.items():
        if a.endswith("}embed") or a.endswith("}id"):
            try: b=parts[v].blob
            except KeyError: continue
            if len(b)<800: continue
            n+=1; ext=".png" if b[:4]==b"\x89PNG" else ".jpg"
            open(os.path.join(G,f"{n:02d}{ext}"),"wb").write(b)
gi=json.load(io.open(os.path.join(ROOT,"web","public","glyphs","index.json"),encoding="utf-8")); ch=gi.get("chars") or gi
fs=sorted(os.listdir(G))
ch["叔"]={"doc":"卷四  弋.docx","files":[f"叔/{f}" for f in fs],"variants":""}
json.dump({"chars":ch},io.open(os.path.join(ROOT,"web","public","glyphs","index.json"),"w",encoding="utf-8"),ensure_ascii=False)
print("叔 glyphs",len(fs))