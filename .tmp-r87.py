import docx,re,glob,os
for f in sorted(glob.glob(r"D:\字谱智能体\*.docx")):
    try: ps=[p.text.strip() for p in docx.Document(f).paragraphs if p.text.strip()]
    except Exception: continue
    for i,t in enumerate(ps):
        if re.match(r"^51[1-9]\.|^52\d\.",t):
            print("##",os.path.basename(f)); print(" ",t[:20],"|",ps[i+1][:150],"|",ps[i+2][:150])
            break