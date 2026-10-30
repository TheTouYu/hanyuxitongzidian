from docx import Document
d=Document(r"D:\字谱智能体\卷六十二  蛇.docx"); ps=[(p.text or "").strip() for p in d.paragraphs]
for i,t in enumerate(ps):
    if t.startswith("359.") or t.startswith("360."):
        print("==",t,"p",i)
        for j in range(i+1,min(len(ps),i+14)):
            if ps[j]: print(" p%d %s"%(j,ps[j][:130]))