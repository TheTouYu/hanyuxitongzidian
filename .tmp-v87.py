import docx,glob
fs=sorted(glob.glob(r"D:\字谱智能体\卷八十七*.docx"))
print([f.split("\\")[-1] for f in fs])
f=fs[0]
ps=[p.text.strip() for p in docx.Document(f).paragraphs if p.text.strip()]
print("TOTAL",len(ps))
for i,t in enumerate(ps[:40]): print(i,t[:80])