from docx import Document
d=Document(r"D:\字谱智能体\卷六十七  足.docx"); ps=[(p.text or "").strip() for p in d.paragraphs]
for j in range(300,320):
    if ps[j]: print(j, ps[j][:110])
print("---- 此支")
for j in range(400,430):
    if j<len(ps) and ps[j] and len(ps[j])>10: print(j, ps[j][:100])