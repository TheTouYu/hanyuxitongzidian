import sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
ps=[p.text.strip() for p in Document(r"D:\字谱智能体\卷六  鶴.docx").paragraphs]
for k in range(193,208): print(k,ps[k][:70])