import docx
f=r"D:\字谱智能体\卷八十六  良.docx"
ps=[p.text.strip() for p in docx.Document(f).paragraphs if p.text.strip()]
for i,t in enumerate(ps[60:141],60): print(i,t[:85])