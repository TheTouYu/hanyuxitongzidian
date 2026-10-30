import docx,re
d=docx.Document(r"D:\字谱智能体\卷八十九  象.docx")
P=[p.text.strip() for p in d.paragraphs]
print("paras",len(P))
for i,p in enumerate(P):
    m=re.match(r"^(\d{3})[\.．]",p)
    if m: print("BU",i,p[:60])
for i,p in enumerate(P):
    if re.match(r"^上（",p) or re.match(r"^上：",p): print("FAM",i,p[:200]); break