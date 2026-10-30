import docx
f=r"D:\字谱智能体\卷八十四  心.docx"
ps=[p.text.strip() for p in docx.Document(f).paragraphs if p.text.strip()]
for i,t in enumerate(ps[119:],119): print(i,t[:100])