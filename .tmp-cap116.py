# -*- coding: utf-8 -*-
import sys,os
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
from docx.oxml.ns import qn
for f in [r"D:\字谱智能体\单栏\卷二  㠯.docx"]:
    d=Document(f); s=d.sections[0]
    cols=s._sectPr.find(qn("w:cols"))
    print(os.path.basename(f),"cols",cols.get(qn("w:num")),"paras",len(d.paragraphs))
o=Document(r"D:\字谱智能体\卷二  㠯.docx")
print("原稿 paras",len(o.paragraphs))
print("单栏文件数",len(os.listdir(r"D:\字谱智能体\单栏")))