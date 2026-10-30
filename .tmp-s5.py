import sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
d=Document(r"D:\字谱智能体\卷二  㠯.docx"); ps=[p.text.strip() for p in d.paragraphs]
for k in range(281,320):
    t=ps[k]
    if t.startswith("野") or "郊野" in t or t.startswith("本義") and k>290: print(k,t[:180])