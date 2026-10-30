import re
from docx import Document
d=Document(r"D:\字谱智能体\第八章  子.docx"); ps=[(p.text or "").strip() for p in d.paragraphs]
for i,t in enumerate(ps):
    if re.match(r"^38[89][.．、]",t):
        print("HIT p",i,t[:40])
        for j in range(i+1,min(len(ps),i+16)):
            if ps[j]: print(" p%d %s"%(j,ps[j][:120]))
        break