import sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
ps=[p.text.strip() for p in Document(r"D:\字谱智能体\卷五  雁.docx").paragraphs]
for k in range(204,389):
    t=ps[k]
    if not t: continue
    if len(t)<40 or t.startswith(("本義","轉義","辯證","音源","字族")) or t[:1] in "①②③④⑤⑥⑦⑧⑨":
        print(k,t[:60])