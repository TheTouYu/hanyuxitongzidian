import docx
for f in [r"D:\字谱智能体\卷八十五  匚.docx"]:
    ps=[p.text.strip() for p in docx.Document(f).paragraphs if p.text.strip()]
    print("TOTAL",len(ps))
    for i,t in enumerate(ps[396:440],396): print(i,t[:80])