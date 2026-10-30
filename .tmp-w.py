import re
from docx import Document
d=Document(r"D:\字谱智能体\卷六十  𦟀.docx")
ps=[(p.text or "").strip() for p in d.paragraphs]
want=("咼","渦","禍","剮","骷","骾")
for i,t in enumerate(ps):
    if not t: continue
    if t[0] in want and len(t)>5:
        print(f"p{i} {t[:200]}")