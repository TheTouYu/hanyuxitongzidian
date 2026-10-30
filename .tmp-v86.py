import docx,glob
f=glob.glob(r"D:\字谱智能体\卷八十六*.docx")[0]
ps=[p.text.strip() for p in docx.Document(f).paragraphs if p.text.strip()]
print("FILE",f,"TOTAL",len(ps))
for i,t in enumerate(ps[:60]): print(i,t[:80])