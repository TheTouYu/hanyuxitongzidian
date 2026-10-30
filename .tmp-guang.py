import docx
f=r"D:\字谱智能体\卷八十五  匚.docx"
ps=[p.text.strip() for p in docx.Document(f).paragraphs if p.text.strip()]
for i,t in enumerate(ps[361:396],361): print(i,t[:90])