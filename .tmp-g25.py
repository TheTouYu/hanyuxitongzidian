import docx,re
d=docx.Document(r"D:\字谱智能体\卷九十一  火.docx")
P=[p.text.strip() for p in d.paragraphs]
for i in list(range(17,40))+list(range(65,92)):
    q=P[i]
    if q and ("《說文》" in q or re.match(r"^[\u3400-\u9fff\ue000-\uf8ff]{1,4}[（(]",q) or q.startswith("▲")):
        print(i,q[:190])