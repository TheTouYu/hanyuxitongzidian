# -*- coding: utf-8 -*-
import sys,os,json,io
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
doc=Document(r"D:\字谱智能体\卷三  矢.docx"); ps=doc.paragraphs; parts=doc.part.related_parts
D=r"D:\系统汉字\web\public\glyphs\智"
for f in os.listdir(D): os.remove(os.path.join(D,f))
n=0; seen=set()
for el in ps[109]._p.iter():
    for a,v in el.attrib.items():
        if a.endswith("}embed") or a.endswith("}id"):
            if v in seen: continue
            try: b=parts[v].blob
            except KeyError: continue
            if len(b)<1500: continue
            seen.add(v); n+=1
            ext=".png" if b[:4]==b"\x89PNG" else ".jpg"
            open(os.path.join(D,f"{n:02d}{ext}"),"wb").write(b)
g=json.load(io.open(r"D:\系统汉字\web\public\glyphs\index.json",encoding="utf-8"))
ch=g.get("chars",g)
files=sorted(os.listdir(D))
ch["智"]["files"]=[f"智/{x}" for x in files]
json.dump(g,io.open(r"D:\系统汉字\web\public\glyphs\index.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("智字形",len(files),files[:3])