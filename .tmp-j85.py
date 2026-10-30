import glob,os,docx,re
fs=[f for f in glob.glob(r"D:\字谱智能体\卷八十五*.docx")]
print(fs)
for f in fs[:1]:
    ps=[p.text.strip() for p in docx.Document(f).paragraphs if p.text.strip()]
    print("paras",len(ps))
    for i,t in enumerate(ps[:40]): print(i,t[:90])