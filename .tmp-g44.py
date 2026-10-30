import docx
d=docx.Document(r"D:\字谱智能体\卷九十四  七.docx")
P=[p.text.strip() for p in d.paragraphs]
for i in range(445,500):
    if P[i]: print(i,P[i][:200])