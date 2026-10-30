import docx
f=r"D:\字谱智能体\卷八十八  昜.docx"
ps=[p.text.strip() for p in docx.Document(f).paragraphs if p.text.strip()]
for i,t in enumerate(ps[7:90],7): print(i,t[:64])