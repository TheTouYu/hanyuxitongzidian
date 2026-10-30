from docx import Document
d=Document(r"D:\字谱智能体\卷六十三  索.docx"); ps=[(p.text or "").strip() for p in d.paragraphs]
for i in range(242,272):
    t=ps[i]
    if t: print("p%d %s"%(i,t[:120]))