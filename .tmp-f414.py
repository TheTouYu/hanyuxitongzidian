from docx import Document
d=Document(r"D:\字谱智能体\第八章  子.docx"); ps=[(p.text or "").strip() for p in d.paragraphs]
print("total",len(ps))
for j in range(max(0,len(ps)-30),len(ps)):
    if ps[j]: print(j, ps[j][:110])
print("---398---")
for j,t in enumerate(ps):
    if t.startswith("398."): print(j,t[:60])