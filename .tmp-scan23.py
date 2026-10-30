import sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
ps=[p.text.strip() for p in Document(r"D:\字谱智能体\卷二  㠯.docx").paragraphs]
for i in (391,392,393,396,397,398,399):
    print(i, ps[i][:420])