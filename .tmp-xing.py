import docx
f=r"D:\字谱智能体\卷八十五  匚.docx"
ps=[p.text.strip() for p in docx.Document(f).paragraphs if p.text.strip()]
for i,t in enumerate(ps[168:241],168): print(i,t[:80])