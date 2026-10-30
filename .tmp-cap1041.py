import sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
for f in (r"D:\字谱智能体\卷三  矢.docx",):
    ps=[p.text for p in Document(f).paragraphs]
    for i,t in enumerate(ps):
        if "䐅" in t or "𡱁" in t: print(i,t[:120])