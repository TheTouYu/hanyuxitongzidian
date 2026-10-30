# -*- coding: utf-8 -*-
import sys,glob
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
for f in glob.glob(r"D:\字谱智能体\*.docx"):
    try: ps=[p.text.strip() for p in Document(f).paragraphs]
    except: continue
    for k,t in enumerate(ps):
        if t.startswith("祟") and "《" in t[:80]:
            print(f.split("\\")[-1],k,t[:160])