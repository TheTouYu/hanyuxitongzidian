import sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
ps=[p.text.strip() for p in Document(r"D:\字谱智能体\卷三  矢.docx").paragraphs]
for k in (364,365,366,367,368,369,370,392,393,394,395,396,397,398,399):
    print(k,repr(ps[k][:70]))