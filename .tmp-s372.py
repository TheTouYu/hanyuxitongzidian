from docx import Document
d=Document(r"D:\字谱智能体\卷六十三  索.docx"); ps=[(p.text or "").strip() for p in d.paragraphs]
for j in range(67,92):
    if ps[j]: print("p%d %s"%(j,ps[j][:100]))