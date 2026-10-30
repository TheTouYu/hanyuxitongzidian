from docx import Document
d=Document(r"D:\字谱智能体\卷六十六  采.docx"); ps=[(p.text or "").strip() for p in d.paragraphs]
for j in range(150,215):
    if ps[j]: print(j, ps[j][:120])