import sys,re,glob
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
ps=[p.text.strip() for p in Document(r"D:\字谱智能体\卷一  雞.docx").paragraphs]
for i,t in enumerate(ps):
    m=re.match(r"^(\d{1,2})[.．]\s*(\S{1,2}?)部\s*$",t)
    if m and int(m.group(1))<=8: print(i,t)
i=[k for k,t in enumerate(ps) if re.match(r"^5[.．]",t)][0]
for k in range(i,min(i+16,len(ps))):
    if ps[k]: print(k,ps[k][:150])