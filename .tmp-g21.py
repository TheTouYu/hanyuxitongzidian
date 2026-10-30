import docx
d=docx.Document(r"D:\字谱智能体\卷九十一  火.docx")
P=[p.text.strip() for p in d.paragraphs]
idx=[(i,p) for i,p in enumerate(P) if p.startswith("554.") or p.startswith("555.")]
print("heads:",idx)
for i,p in idx:
    for q in P[i:i+18]:
        if q: print(">",q[:200])
    print("-"*20)