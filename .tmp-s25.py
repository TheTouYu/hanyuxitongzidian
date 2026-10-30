import sys,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
ps=[p.text.strip() for p in Document(r"D:\字谱智能体\卷二  㠯.docx").paragraphs]
for i in range(418,472):
    s=ps[i]
    if s and (s.startswith(("轉義","辯證","音源","字族","本義")) or re.match(r"^[①②③④⑤⑥]",s)):
        print(i,s[:150])