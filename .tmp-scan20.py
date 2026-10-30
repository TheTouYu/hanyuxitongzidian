# -*- coding: utf-8 -*-
import sys,glob
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
for f in glob.glob(r"D:\字谱智能体\卷二*.docx"):
    ps=[p.text.strip() for p in Document(f).paragraphs]
    for i,s in enumerate(ps):
        if s.startswith("𢑓") or s.startswith("家（") or s.startswith("家 ") or s.startswith("家\u3000"):
            print(i, s[:220])