import docx,glob
d=docx.Document(r"D:\字谱智能体\卷九十二  辛.docx")
P=[p.text.strip() for p in d.paragraphs]
for i in range(563,585):
    if P[i]: print(i,P[i][:220])
print("vols:", [f.split("\\")[-1] for f in glob.glob(r"D:\字谱智能体\卷九十三*.docx")+glob.glob(r"D:\字谱智能体\卷九十四*.docx")])