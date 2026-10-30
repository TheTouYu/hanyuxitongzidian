# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
G=r"D:\系统汉字\web\public\glyphs"
ix=json.load(io.open(G+r"\index.json",encoding="utf-8"))
for c in ("䒬","祡","祭"):
    print(c, ix["chars"].get(c))
print("dir:", os.listdir(G+r"\䒬") if os.path.isdir(G+r"\䒬") else None)
from docx import Document
d=Document(r"D:\字谱智能体\卷二  㠯.docx")
ps=[p.text.strip() for p in d.paragraphs]
idx=[i for i,t in enumerate(ps) if "䒬" in t]
print("䒬 段",idx[:6])
for i in idx[:3]:
    print("…",i,ps[i][:80])