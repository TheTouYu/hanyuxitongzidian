import docx
d=docx.Document(r"D:\字谱智能体\卷八十八  昜.docx")
P=[p.text.strip() for p in d.paragraphs]
i0=[i for i,p in enumerate(P) if p.startswith("531.")][0]
i1=[i for i,p in enumerate(P) if p.startswith("532.")][0]
for p in P[i0:i1]:
    if p.startswith("喪（") or p.startswith("染（") or p.startswith("·") or p.startswith("本義") or p.startswith("轉義"):
        print(">",p[:200])