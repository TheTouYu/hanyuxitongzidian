import docx
d=docx.Document(r"D:\字谱智能体\卷九十四  七.docx")
P=[p.text.strip() for p in d.paragraphs]
for i in range(296,330):
    if P[i]: print(i,P[i][:230])
print("---")
for i in range(330,445):
    if P[i] and P[i].startswith(("本義","轉義","音源","辯證")): print(i,P[i][:300])