import sys,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
ps=[p.text.strip() for p in Document(r"D:\字谱智能体\卷七  斤.docx").paragraphs]
print("total",len(ps))
for k in range(100,286):
    t=ps[k]
    if not t: continue
    if re.match(r"^(本義|轉義|辯證|音源|字族衍義)",t) or re.match(r"^[①-⑦]",t) or t.startswith("（") or re.match(r"^\d{1,3}[.．]",t):
        print(k,t[:60])