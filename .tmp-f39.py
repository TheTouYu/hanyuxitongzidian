# -*- coding: utf-8 -*-
import sys,re,glob,os
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
for f in glob.glob(r"D:\字谱智能体\*.docx"):
    try: ps=[p.text.strip() for p in Document(f).paragraphs]
    except Exception: continue
    for i,t in enumerate(ps):
        m=re.match(r"^39[.．]\s*(\S{1,3})部$",t)
        if m: print(os.path.basename(f),i,t,len(ps))