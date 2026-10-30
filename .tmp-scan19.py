# -*- coding: utf-8 -*-
import sys,glob
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
for f in glob.glob(r"D:\字谱智能体\*.docx"):
    try: ps=[p.text.strip() for p in Document(f).paragraphs]
    except Exception: continue
    for i,s in enumerate(ps):
        if s.startswith("豛") or "\u8c9b" in s[:6]:
            print(f.split("\\")[-1], i, s[:170])