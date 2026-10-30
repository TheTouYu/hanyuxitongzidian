from docx import Document
d=Document(r"D:\字谱智能体\卷七十一  聿部.docx"); ps=[(p.text or "").strip() for p in d.paragraphs]
print("total",len(ps))
for j in range(268,min(len(ps),330)):
    if ps[j] and len(ps[j])>6: print(j, ps[j][:85])