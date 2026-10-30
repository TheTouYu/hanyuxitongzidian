import docx,re
ps=[p.text.strip() for p in docx.Document(r"D:\字谱智能体\卷八十三  鼎.docx").paragraphs if p.text.strip()]
for i,t in enumerate(ps):
    if re.match(r"^(51[0-5])\.",t):
        print("==",t[:20])
        for j in range(i+1,min(i+7,len(ps))):
            print("  ",ps[j][:260])