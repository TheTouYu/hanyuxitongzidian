from docx import Document
d=Document(r"D:\字谱智能体\卷七十一  聿部.docx"); ps=[(p.text or "").strip() for p in d.paragraphs]
for j in range(104,min(len(ps),150)):
    if ps[j] and len(ps[j])>8: print(j, ps[j][:100])