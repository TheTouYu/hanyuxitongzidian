import docx,re,glob,os
for f in sorted(glob.glob(r"D:\字谱智能体\*.docx")):
    if not re.search(r"八十一|八十二",os.path.basename(f)): continue
    d=docx.Document(f); ps=[p.text.strip() for p in d.paragraphs if p.text.strip()]
    print("### ",os.path.basename(f))
    n=0
    for i,t in enumerate(ps):
        if re.match(r"^49[5-9]\.|^50\d\.",t):
            print(t[:26])
            for j in range(i+1,min(i+3,len(ps))):
                if ps[j].startswith("本義"): print("   ",ps[j][:170]); break
            n+=1
            if n>=6: break