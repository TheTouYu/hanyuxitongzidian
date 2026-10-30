import docx
d=docx.Document(r"D:\字谱智能体\卷九十一  火.docx")
P=[p.text.strip() for p in d.paragraphs]
for i in range(60,80):
    if P[i]: print(i,P[i][:230])