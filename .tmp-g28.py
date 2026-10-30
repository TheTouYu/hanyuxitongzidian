import docx
d=docx.Document(r"D:\字谱智能体\卷九十二  辛.docx")
P=[p.text.strip() for p in d.paragraphs]
for i in range(12,34):
    if P[i]: print(i,P[i][:240])