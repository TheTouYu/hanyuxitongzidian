import docx,re,glob,os
fs=[f for f in glob.glob(r"D:\字谱智能体\*.docx") if re.search(r"八十三",os.path.basename(f))]
for f in fs:
    print("##",os.path.basename(f))
    ps=[p.text.strip() for p in docx.Document(f).paragraphs if p.text.strip()]
    n=0
    for i,t in enumerate(ps):
        if re.match(r"^5(0[6-9]|1\d)\.",t):
            print(t[:22])
            for j in range(i+1,min(i+6,len(ps))):
                if ps[j].startswith("本義"):
                    print("   ",ps[j][:230]); n+=1; break
            if n>=8: break