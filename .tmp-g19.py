import docx
d=docx.Document(r"D:\字谱智能体\卷八十八  昜.docx")
P=[p.text.strip() for p in d.paragraphs]
i0=[i for i,p in enumerate(P) if p.startswith("532.")][0]
print("532 at",i0,"total",len(P))
for p in P[i0:i0+30]:
    if p: print(">",p[:210])