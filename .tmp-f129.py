from docx import Document
d=Document(r"D:\字谱智能体\卷六十九  舄.docx"); ps=[(p.text or "").strip() for p in d.paragraphs]
print("total",len(ps))
for j in range(129,min(len(ps),172)):
    if ps[j] and len(ps[j])>5: print(j, ps[j][:110])