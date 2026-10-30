import sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
d=Document(r"D:\字谱智能体\卷二  㠯.docx"); ps=[p.text.strip() for p in d.paragraphs]
for k,t in enumerate(ps):
    if t.startswith("野") and len(t)>3 and k>281: print(k,t[:200])