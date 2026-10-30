import docx
f=r"D:\字谱智能体\卷八十五  匚.docx"
ps=[p.text.strip() for p in docx.Document(f).paragraphs if p.text.strip()]
for i,t in enumerate(ps[311:362],311): print(i,t[:85])