# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
d=Document(r"D:\字谱智能体\卷三  矢.docx"); ps=d.paragraphs; parts=d.part.related_parts
rid=None
for el in ps[303]._p.iter():
    for a,v in el.attrib.items():
        if a.endswith("}embed") or a.endswith("}id"):
            try:
                if len(parts[v].blob)>8000: rid=v
            except KeyError: pass
print("rid",rid)
P=r"D:\系统汉字\web\public\glyphs\photos"; D=os.path.join(P,"尺")
if os.path.isdir(D):
    for f in os.listdir(D): os.remove(os.path.join(D,f))
else: os.makedirs(D)
b=parts[rid].blob; ext=".png" if b[:4]==b"\x89PNG" else ".jpg"
open(os.path.join(D,"01"+ext),"wb").write(b)
cp=json.load(io.open(os.path.join(P,"captions.json"),encoding="utf-8"))["captions"]
cp["尺"]=["骨尺（商）"]
json.dump({"captions":cp},io.open(os.path.join(P,"captions.json"),"w",encoding="utf-8"),ensure_ascii=False)
C=r"D:\系统汉字\web\public\cards\尺.json"; c=json.load(io.open(C,encoding="utf-8"))
c["photos"]=["01"+ext]; c["captions"]=["骨尺（商）"]
json.dump(c,io.open(C,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("尺",len(b),ext)