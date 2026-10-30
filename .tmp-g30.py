import docx,re
d=docx.Document(r"D:\字谱智能体\卷九十二  辛.docx")
P=[p.text.strip() for p in d.paragraphs]
for i in range(34,137):
    q=P[i]
    if re.match(r"^[\u3400-\u9fff\ue000-\uf8ff]{1,4}[（(][^）]{0,4}",q) and ("《" in q or "从" in q):
        print(i,q[:150])