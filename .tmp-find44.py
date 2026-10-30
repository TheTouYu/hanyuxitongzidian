# -*- coding: utf-8 -*-
import glob,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
pat=re.compile(r"^(\d{1,3})[.．]\s*(\S{1,4})部$")
hits=[]
for f in glob.glob(r"D:\字谱智能体\*.docx"):
    try: ps=[p.text.strip() for p in Document(f).paragraphs]
    except Exception: continue
    for i,t in enumerate(ps):
        m=pat.match(t)
        if m and 44<=int(m.group(1))<=52: hits.append((int(m.group(1)),os.path.basename(f),i,t))
for h in sorted(set(hits))[:12]: print(h)