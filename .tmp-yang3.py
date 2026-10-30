import docx
f=r"D:\字谱智能体\卷八十七  羊.docx"
ps=[p.text.strip() for p in docx.Document(f).paragraphs if p.text.strip()]
for i,t in enumerate(ps[99:170],99): print(i,t[:78])