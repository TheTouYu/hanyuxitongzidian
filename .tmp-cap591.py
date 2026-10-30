import sys,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
ps=[p.text.strip() for p in Document(r"D:\字谱智能体\卷三  矢.docx").paragraphs]
for k in range(63,130):
    t=ps[k]
    if not t: continue
    if re.match(r"^1[6-9][.．]",t): print("END",k,t); break
    print(k,t[:80])