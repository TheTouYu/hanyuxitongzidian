import sys,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
ps=[p.text.strip() for p in Document(r"D:\字谱智能体\卷三  矢.docx").paragraphs]
for k,t in enumerate(ps):
    if re.match(r"^2[6-9][.．]\s*\S+部$",t): print(k,t)