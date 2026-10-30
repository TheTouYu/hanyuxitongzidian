import docx
d=docx.Document(r"D:\字谱智能体\卷九十二  辛.docx")
P=[p.text.strip() for p in d.paragraphs]
for i in list(range(371,388))+list(range(401,417)):
    if P[i]: print(i,P[i][:220])