from docx import Document
d=Document(r"D:\字谱智能体\卷六十九  舄.docx"); ps=[(p.text or "").strip() for p in d.paragraphs]
for j in range(96,min(len(ps),132)):
    if ps[j] and len(ps[j])>6: print(j, ps[j][:105])