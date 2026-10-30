import sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
doc=Document(r"D:\字谱智能体\卷六  鶴.docx")
for k in range(193,234):
    p=doc.paragraphs[k]; n=sum(1 for el in p._p.iter() if el.tag.split("}")[-1]=="blip"); t=p.text.strip()
    if n or t.startswith("▲"): print(k,n,t[:60])