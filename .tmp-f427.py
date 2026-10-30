from docx import Document
d=Document(r"D:\字谱智能体\卷七十  亥.docx"); ps=[(p.text or "").strip() for p in d.paragraphs]
print("total",len(ps))
for j in range(452,min(len(ps),500)):
    if ps[j] and len(ps[j])>8: print(j, ps[j][:105])