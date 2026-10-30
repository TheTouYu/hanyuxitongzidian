import docx
d=docx.Document(r"D:\字谱智能体\卷九十一  火.docx")
P=[p.text.strip() for p in d.paragraphs]
i0=[i for i,p in enumerate(P) if p.startswith("550.")][0]
i1=[i for i,p in enumerate(P) if p.startswith("551.")][0]
print("550 section",i0,i1)
for q in P[i0:i0+14]:
    if q: print(">",q[:230])
print("... 字族衍義 headings ...")
for i in range(i0,i1):
    if P[i].startswith("字族衍義") or (len(P[i])<24 and "：" in P[i] and P[i].endswith("：")):
        print(i,P[i][:60])