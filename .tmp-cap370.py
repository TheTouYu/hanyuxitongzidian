import re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
ps=[p.text.strip() for p in Document(r"D:\字谱智能体\卷二  㠯.docx").paragraphs]
for k,t in enumerate(ps):
    if 550<k<700 and re.match(r"^\d{1,3}[.．]\s*\S{1,3}部$",t): print("H",k,t)
for k in range(598,626):
    if ps[k]: print(k,ps[k][:105])