import docx,re
d=docx.Document(r"D:\字谱智能体\卷八十八  昜.docx")
P=[p.text.strip() for p in d.paragraphs]
i0=[i for i,p in enumerate(P) if p.startswith("529.")][0]
i1=[i for i,p in enumerate(P) if p.startswith("530.")][0]
print("range",i0,i1,"n",i1-i0)
for p in P[i0:i0+16]:
    if p: print(">",p[:200])