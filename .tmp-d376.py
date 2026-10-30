from docx import Document
d=Document(r"D:\字谱智能体\卷六十三  索.docx"); ps=[(p.text or "").strip() for p in d.paragraphs]
for i in range(243,262):
    if ps[i]: print(i,ps[i][:150])
print("----")
for i in range(300,340):
    if ps[i]: print(i,ps[i][:150])