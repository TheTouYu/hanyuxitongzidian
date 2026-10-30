# -*- coding: utf-8 -*-
import sys,glob
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
for f in glob.glob(r"D:\字谱智能体\卷二*.docx"):
    d=Document(f); ps=[p.text.strip() for p in d.paragraphs]
    for i,s in enumerate(ps):
        if s.startswith("貍") or s.startswith("薶") or s.startswith("霾") or "山貓" in s[:40]:
            print(i, s[:150])
    print("----")