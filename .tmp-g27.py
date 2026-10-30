import docx,glob,re
f=glob.glob(r"D:\字谱智能体\卷九十二*.docx")[0]
print("FILE",f)
d=docx.Document(f)
P=[p.text.strip() for p in d.paragraphs]
hs=[(i,p) for i,p in enumerate(P) if re.match(r"^\d{3}\.",p)]
print("heads:",hs[:12])
i0=hs[0][0]
for q in P[i0:i0+10]:
    if q: print(">",q[:230])