# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
d=Document(r"D:\字谱智能体\卷卅八 夬.docx")
ps=[p.text.strip() for p in d.paragraphs]
for k in range(108,124):
    if ps[k]: print(k,ps[k][:300])