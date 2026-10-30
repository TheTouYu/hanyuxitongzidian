from docx import Document
d=Document(r"D:\字谱智能体\卷三  矢.docx"); ps=[p.text.strip() for p in d.paragraphs]
for k in range(272,300):
    if ps[k]: print(k,ps[k][:110])