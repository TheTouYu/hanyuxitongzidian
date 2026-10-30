import docx
d=docx.Document(r"D:\字谱智能体\卷八十八  昜.docx")
P=[p.text.strip() for p in d.paragraphs]
for i,p in enumerate(P):
    if p.startswith("當（") or p.startswith("黨（") or p.startswith("掌（"):
        print(i,"|",p[:300])
        for q in P[i+1:i+4]:
            if q.startswith("本義") or q.startswith("轉義"): print("   ",q[:200])