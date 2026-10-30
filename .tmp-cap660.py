import sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
ps=[p.text.strip() for p in Document(r"D:\字谱智能体\卷三  矢.docx").paragraphs]
for k in range(225,241):
    if ps[k]: print(k,ps[k][:100])
i=[k for k,t in enumerate(ps) if t.startswith("臺") or t.startswith("彘") or t.startswith("到")]
print("idx",i[:6])