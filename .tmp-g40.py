import docx
d=docx.Document(r"D:\字谱智能体\卷九十四  七.docx")
P=[p.text.strip() for p in d.paragraphs]
for i in range(120,150):
    if P[i]: print(i,P[i][:200])
print("---")
for i in range(150,200):
    if P[i] and ("本義" in P[i] or "桼" in P[i] or "皂" in P[i] or "甲" in P[i]): print(i,P[i][:260])