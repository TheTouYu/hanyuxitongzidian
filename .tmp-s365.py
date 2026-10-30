from docx import Document
d=Document(r"D:\字谱智能体\卷六十二  蛇.docx"); ps=[(p.text or "").strip() for p in d.paragraphs]
print("TOTAL",len(ps))
for j in range(438,470):
    if ps[j]: print("p%d %s"%(j,ps[j][:104]))