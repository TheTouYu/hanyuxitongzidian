import sys,glob,re,json
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
for f in glob.glob(r"D:\字谱智能体\*.docx"):
    try: ps=[p.text for p in Document(f).paragraphs]
    except: continue
    for i,t in enumerate(ps):
        if t.strip().startswith("爾部"):
            print(f.split("\\")[-1], i, t[:40])