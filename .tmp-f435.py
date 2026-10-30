from docx import Document
d=Document(r"D:\系统汉字\卷七十三  釆.docx") if False else Document(r"D:\字谱智能体\卷七十三  釆.docx")
ps=[(p.text or "").strip() for p in d.paragraphs]
print("total",len(ps))
for j in range(42,min(len(ps),120)):
    if ps[j] and len(ps[j])>6: print(j, ps[j][:78])