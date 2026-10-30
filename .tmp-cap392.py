import sys,os
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
doc=Document(r"D:\字谱智能体\卷二  㠯.docx")
b=doc.part.related_parts["rId434"].blob
p=r"D:\系统汉字\.tmp-chili.emf"
open(p,"wb").write(b); print(p,len(b))