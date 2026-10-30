# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
doc=Document(r"D:\字谱智能体\卷三  矢.docx"); parts=doc.part.related_parts
P=r"D:\系统汉字\web\public\glyphs\photos"
rid=None
for k in range(243,249):
    for el in doc.paragraphs[k]._p.iter():
        for a,v in el.attrib.items():
            if a.endswith("}embed") or a.endswith("}id"):
                try:
                    n=len(parts[v].blob)
                    print("cand",k,v,n)
                    if n>30000: rid=v
                except KeyError: pass
if rid:
    b=parts[rid].blob; ext=".png" if b[:4]==b"\x89PNG" else ".jpg"
    D=os.path.join(P,"臺"); os.makedirs(D,exist_ok=True); fn="01"+ext
    open(os.path.join(D,fn),"wb").write(b)
    idx=json.load(io.open(os.path.join(P,"index.json"),encoding="utf-8")); ph=idx.get("photos") or idx
    ph["臺"]=[fn]; json.dump({"photos":ph},io.open(os.path.join(P,"index.json"),"w",encoding="utf-8"),ensure_ascii=False)
    cap=json.load(io.open(os.path.join(P,"captions.json"),encoding="utf-8")); cm=cap.get("captions") or cap
    cm["臺"]=["河南登封的觀星臺（元）"]; json.dump({"captions":cm},io.open(os.path.join(P,"captions.json"),"w",encoding="utf-8"),ensure_ascii=False)
    print("saved",fn,len(b))