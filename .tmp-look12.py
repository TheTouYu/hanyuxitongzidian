from docx import Document
d=Document(r"D:\字谱智能体\卷九十六  雀.docx")
ps=[p.text.strip() for p in d.paragraphs]
for k in list(range(520,540))+list(range(597,612)):
    if ps[k]: print(k,ps[k][:165])