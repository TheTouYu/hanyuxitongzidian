import docx,re
d=docx.Document(r"D:\字谱智能体\卷九十二  辛.docx")
P=[p.text.strip() for p in d.paragraphs]
for i in range(174,197):
    q=P[i]
    if q and ("《" in q or "从" in q):
        print(i,q[:170])