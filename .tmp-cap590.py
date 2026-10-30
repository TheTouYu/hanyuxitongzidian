import sys,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
ps=[p.text.strip() for p in Document(r"D:\字谱智能体\卷三  矢.docx").paragraphs]
idx=[k for k,t in enumerate(ps) if re.match(r"^16[.．]",t)]
print("heading",idx[:3])
k0=idx[0]
for k in range(k0,k0+42):
    if k<len(ps) and ps[k]: print(k,ps[k][:110])