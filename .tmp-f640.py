from docx import Document
d=Document(r"D:\字谱智能体\卷六十七  足.docx"); ps=[(p.text or "").strip() for p in d.paragraphs]
for j in range(640,min(len(ps),700)):
    if ps[j] and len(ps[j])>6: print(j, ps[j][:108])