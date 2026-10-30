import sys,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
ps=[p.text.strip() for p in Document(r"D:\字谱智能体\卷一  雞.docx").paragraphs]
for k in range(320,412):
    t=ps[k]
    if not t: continue
    if re.match(r"^(本義|轉義|辯證|音源|字族衍義)",t) or re.match(r"^[（（]",t):
        print(k,t[:120])