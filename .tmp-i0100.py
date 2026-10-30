# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
doc=Document(r"D:\字谱智能体\卷四  弋.docx"); ps=[p.text.strip() for p in doc.paragraphs]; parts=doc.part.related_parts
def kind(b):
    if b[:4]==b"\x89PNG": return "png"
    if b[:4]==b"\x01\x00\x00\x00": return "emf"
    if b[:2]==b"\xff\xd8": return "jpg"
    if b[:2]==b"BM": return "bmp"
    return "bin"
for k in range(260,270):
    imgs=[]
    for el in doc.paragraphs[k]._p.iter():
        for a,v in el.attrib.items():
            if a.endswith("}embed") or a.endswith("}id"):
                try: b=parts[v].blob
                except KeyError: continue
                imgs.append((kind(b),len(b)))
    if imgs: print(k,ps[k][:40],"->",imgs)