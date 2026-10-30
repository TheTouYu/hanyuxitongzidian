import sys,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
ps=[p.text.strip() for p in Document(r"D:\字谱智能体\卷六  鶴.docx").paragraphs]
for k in range(299,399):
    t=ps[k]
    if not t: continue
    if t.startswith(("本義","轉義","辯證","音源","字族")) or re.match(r'^[①-⑨]',t) or re.match(r'^\d{1,3}[.．]\s*\S{1,3}部$',t):
        print(k,t[:50])