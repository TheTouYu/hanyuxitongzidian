from docx import Document
import re
d=Document(r"D:\字谱智能体\卷九十五  離.docx")
ps=[p.text.strip() for p in d.paragraphs]
print("paras",len(ps))
hs=[(k,t) for k,t in enumerate(ps) if re.match(r"^\d{3}[.．]\s*\S+部",t)]
for k,t in hs: print(k,t)
if hs:
    s=hs[0][0]
    for k in range(s,min(s+26,len(ps))):
        if ps[k]: print(k,ps[k][:170])