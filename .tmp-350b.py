from docx import Document
d=Document(r"D:\字谱智能体\卷六十  𦟀.docx")
ps=[(p.text or "").strip() for p in d.paragraphs]
for j in range(337,353):
    t=ps[j]
    if t: print(j, t[:150])