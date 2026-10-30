from docx import Document
d=Document(r"D:\字谱智能体\卷九十七  殸.docx")
ps=[p.text.strip() for p in d.paragraphs]
for k in range(54,120):
    if ps[k]: print(k,ps[k][:110])