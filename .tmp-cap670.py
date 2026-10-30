import sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
for f in (r"D:\字谱智能体\卷三  矢.docx",):
    for k,p in enumerate(Document(f).paragraphs):
        t=p.text.strip()
        if t.startswith("芪"): print(k,t[:110])