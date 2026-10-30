from docx import Document
d=Document(r"D:\字谱智能体\卷六十七  足.docx"); ps=[(p.text or "").strip() for p in d.paragraphs]
print("total",len(ps))
for j in range(661,min(len(ps),720)):
    if ps[j] and len(ps[j])>6: print(j, ps[j][:105])