import glob,docx,re,os
hits=[]
for f in sorted(glob.glob(r"D:\字谱智能体\*.docx")):
    try: ps=[p.text.strip() for p in docx.Document(f).paragraphs if p.text.strip()]
    except: continue
    for j,t in enumerate(ps):
        if "昷" in t and len(t)<24:
            hits.append((os.path.basename(f),j,t,ps[j-1][:30] if j else ""))
for h in hits[:12]: print(h)