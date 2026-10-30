import sys,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
ps=[p.text.strip() for p in Document(r"D:\字谱智能体\卷四  弋.docx").paragraphs]
for k,t in enumerate(ps):
    m=re.match(r"^(\d{1,3})[.．]\s*(\S{1,3})部$",t)
    if m: print(k,t,len(ps))