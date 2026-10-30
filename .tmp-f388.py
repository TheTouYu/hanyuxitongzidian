from docx import Document
d=Document(r"D:\字谱智能体\第八章  子.docx"); ps=[(p.text or "").strip() for p in d.paragraphs]
for j in range(185,214):
    if ps[j]: print(j, ps[j][:120])