import sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
ps=[p.text.strip() for p in Document(r"D:\字谱智能体\卷七  斤.docx").paragraphs]
for k in range(23,102):
    t=ps[k]
    if not t: continue
    if len(t)<60 or t[:2] in ("本義","轉義","辯證","音源","字族") or t[0] in "①②③④⑤⑥⑦⑧⑨⑩":
        print(k,t[:90])