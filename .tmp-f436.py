from docx import Document
d=Document(r"D:\字谱智能体\卷七十三  釆.docx"); ps=[(p.text or "").strip() for p in d.paragraphs]
for j in range(120,min(len(ps),175)):
    if ps[j] and len(ps[j])>6: print(j, ps[j][:80])