from docx import Document
import sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
ps=[p.text.strip() for p in Document(r"D:\字谱智能体\卷二  㠯.docx").paragraphs]
for k in list(range(145,169))+list(range(106,116)):
    t=ps[k]
    if t: print(k,repr(t[:56]))