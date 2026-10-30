import docx,re
d=docx.Document(r"D:\字谱智能体\卷八十一  釘.docx")
ps=[p.text.strip() for p in d.paragraphs if p.text.strip()]
for i,t in enumerate(ps):
    if re.match(r"^(495|496|497|498)\.",t):
        print("==",t)
        for j in range(i+1,min(i+5,len(ps))):
            print("  ",ps[j][:230])