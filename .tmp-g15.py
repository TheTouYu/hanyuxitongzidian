import docx
d=docx.Document(r"D:\字谱智能体\卷八十八  昜.docx")
P=[p.text.strip() for p in d.paragraphs]
i0=[i for i,p in enumerate(P) if p.startswith("529.")][0]; i1=[i for i,p in enumerate(P) if p.startswith("530.")][0]
for p in P[i0:i1]:
    if p.startswith("・") or p[:1] in "𧡮𠷹𤭪𤷼𪂼蘘灀": print(p[:180])
print("=== 530 ===")
i2=[i for i,p in enumerate(P) if p.startswith("531.")][0]
for p in P[i1:i2+2]:
    if p: print(">",p[:200])