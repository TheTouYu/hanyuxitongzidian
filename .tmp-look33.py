import sys; sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
d=Document(r"D:\字谱智能体\卷九十八  銿.docx")
ps=[p.text.strip() for p in d.paragraphs]
for k in range(33,120):
    if ps[k] and (len(ps[k])<60): print(k,ps[k][:60])