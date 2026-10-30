import glob,os,re
from docx import Document
for path in [r"D:\字谱智能体\卷六十三  索.docx"]:
    d=Document(path); ps=[(p.text or "").strip() for p in d.paragraphs]
    for i,t in enumerate(ps):
        m=re.match(r"^(38[3-9]|39[0-9])[.．、]",t)
        if m: print(i,t[:40])