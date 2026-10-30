import sys,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
ps=[p.text.strip() for p in Document(r"D:\字谱智能体\卷二  㠯.docx").paragraphs]
line=ps[675]
print("伎 count",line.count("伎"))
for m in re.finditer("伎",line):
    print(line[max(0,m.start()-12):m.start()+12])