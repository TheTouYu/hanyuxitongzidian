from docx import Document
d=Document(r"D:\字谱智能体\卷六十三  索.docx"); ps=[(p.text or "").strip() for p in d.paragraphs]
for i in range(549,580):
    if ps[i]: print(i,ps[i][:120])