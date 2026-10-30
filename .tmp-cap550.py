import sys,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
ps=[p.text.strip() for p in Document(r"D:\字谱智能体\卷二  㠯.docx").paragraphs]
for k,t in enumerate(ps):
    if re.match(r"^1[45][.．]",t) or t.startswith("15."): print(k,t[:40])