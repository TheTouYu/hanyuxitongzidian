import sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
ps=[p.text for p in Document(r"D:\字谱智能体\卷廿四  貝.docx").paragraphs]
for i in range(520,540):
    if ps[i].strip(): print(i,ps[i][:150])