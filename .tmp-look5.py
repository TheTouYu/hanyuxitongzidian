from docx import Document
d=Document(r"D:\字谱智能体\卷九十五  離.docx")
ps=[p.text.strip() for p in d.paragraphs]
for k in range(195,min(214,len(ps))):
    if ps[k]: print(k,ps[k][:190])