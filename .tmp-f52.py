from docx import Document
d=Document(r"D:\字谱智能体\卷六十九  舄.docx"); ps=[(p.text or "").strip() for p in d.paragraphs]
for j in range(52,min(len(ps),100)):
    if ps[j] and len(ps[j])>8: print(j, ps[j][:100])