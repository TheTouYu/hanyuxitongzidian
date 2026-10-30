from docx import Document
d=Document(r"D:\字谱智能体\卷二  㠯.docx"); ps=[p.text.strip() for p in d.paragraphs]
i=[k for k,t in enumerate(ps) if t.startswith("9.士")][0]
for k in range(i,i+16):
    if ps[k]: print(k,ps[k][:150])