from docx import Document
d=Document(r"D:\字谱智能体\卷七十  亥.docx"); ps=[(p.text or "").strip() for p in d.paragraphs]
for j in range(190,214):
    if ps[j] and len(ps[j])>8: print(j, ps[j][:72])