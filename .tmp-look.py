from docx import Document
import re
d=Document(r"D:\字谱智能体\卷九十四  七.docx")
ps=[p.text.strip() for p in d.paragraphs]
i=[k for k,t in enumerate(ps) if re.match(r"^573[.．]\s*萬部",t)]
print("idx",i)
if i:
    s=i[0]
    for k in range(s,min(s+40,len(ps))):
        t=ps[k]
        if t: print(k,t[:160])