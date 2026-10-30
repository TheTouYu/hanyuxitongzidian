import sys; sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
d=Document(r"D:\字谱智能体\卷九十七  殸.docx")
ps=[p.text.strip() for p in d.paragraphs]
for k in range(505,545):
    if ps[k]: print(k,ps[k][:75])
print("----docx后续----")
import os
for f in sorted(os.listdir(r"D:\字谱智能体")):
    if f.startswith("卷九十八") or f.startswith("卷九十九"): print(f)