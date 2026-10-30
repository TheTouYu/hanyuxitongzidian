import sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
doc=Document(r"D:\字谱智能体\卷四  弋.docx"); ps=[p.text.strip() for p in doc.paragraphs]
for k in range(322,346):
    n=sum(1 for el in doc.paragraphs[k]._p.iter() if el.tag.endswith('}blip'))
    if ps[k] or n: print(k,n,ps[k][:110])