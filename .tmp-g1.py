import sys,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
ps=[p.text.strip() for p in Document(r"D:\字谱智能体\卷六  鶴.docx").paragraphs]
print("total",len(ps))
for k in range(234,len(ps)):
    t=ps[k]
    if re.match(r'^\d{1,3}[.．]\s*\S{1,3}部$',t): print("HEAD",k,t); break
for k in range(234,min(300,len(ps))):
    t=ps[k]
    if not t: continue
    if len(t)<40 or t.startswith(("本義","轉義","辯證","音源","字族")) or re.match(r'^[①-⑨]',t):
        print(k,t[:58])