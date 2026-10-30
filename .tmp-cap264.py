import sys,json
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
d=Document(r"D:\字谱智能体\卷二  㠯.docx")
ps=[p.text.strip() for p in d.paragraphs]
for k in (540,543,544,545,546,547,548,549,551,552,553,554,555,556,557,558,559,560,561,562,563,564):
    print(k,"|",ps[k])