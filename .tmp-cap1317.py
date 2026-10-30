import sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
for k,p in enumerate(Document(r"D:\字谱智能体\卷三  矢.docx").paragraphs):
    t=p.text.strip()
    if t.startswith("措") or (t.startswith("（") and "措" in t):
        print(k,t[:120])