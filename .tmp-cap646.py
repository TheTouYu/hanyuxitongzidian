# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
P=r"D:\系统汉字\web\public\glyphs\photos"
doc=Document(r"D:\字谱智能体\卷三  矢.docx"); parts=doc.part.related_parts
b=parts["rId84"].blob
ext=".png" if b[:4]==b"\x89PNG" else ".jpg"
D=os.path.join(P,"医"); os.makedirs(D,exist_ok=True)
fn="01"+ext; open(os.path.join(D,fn),"wb").write(b)
idx=json.load(io.open(os.path.join(P,"index.json"),encoding="utf-8")); ph=idx.get("photos") or idx
ph["医"]=[fn]; json.dump({"photos":ph},io.open(os.path.join(P,"index.json"),"w",encoding="utf-8"),ensure_ascii=False)
print("医",fn,len(b))