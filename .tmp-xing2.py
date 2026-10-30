import docx,glob,re
for f in glob.glob(r"D:\字谱智能体\*.docx"):
    try: ps=[p.text.strip() for p in docx.Document(f).paragraphs if p.text.strip()]
    except: continue
    hit=[i for i,t in enumerate(ps) if "娙" in t or "坙部" in t]
    if hit:
        print("==",f.split("\\")[-1])
        for i in hit[:4]:
            lo=max(0,i-3)
            for j in range(lo,min(len(ps),i+2)):
                print(" ",j,ps[j][:70])