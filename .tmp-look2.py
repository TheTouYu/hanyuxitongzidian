from docx import Document
import re
d=Document(r"D:\字谱智能体\卷九十四  七.docx")
ps=[p.text.strip() for p in d.paragraphs]
for key,rng in (("574",(758,800)),("575",(800,840)),("576",(840,890)),("577",(890,940))):
    idx=[k for k,t in enumerate(ps) if re.match(rf"^{key}[.．]\s*\S+部",t)]
    print("==",key,idx)
    if idx:
        s=idx[0]
        for k in range(s,min(s+18,len(ps))):
            t=ps[k]
            if t: print(k,t[:150])