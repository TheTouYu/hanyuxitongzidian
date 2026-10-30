from docx import Document
d=Document(r"D:\字谱智能体\卷二  㠯.docx"); ps=[p.text.strip() for p in d.paragraphs]
ks=[k for k,t in enumerate(ps) if t.startswith("野（埜")]
print("idx",ks[:3])
i=ks[0] if ks else 0
for k in range(i,i+10):
    if ps[k]: print(k,ps[k][:170])