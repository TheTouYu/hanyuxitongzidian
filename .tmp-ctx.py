import glob,docx,re,os
T="忠忍恥悉恭悔悚惰想愁憫懲戀"
seen=set()
for f in sorted(glob.glob(r"D:\字谱智能体\*.docx")):
    try: ps=[p.text.strip() for p in docx.Document(f).paragraphs if p.text.strip()]
    except: continue
    cur=None
    for j,t in enumerate(ps):
        h=re.match(r"^(\d{3})[.．、]\s*([^\s：]{1,4})",t)
        if h and len(t)<16: cur=(int(h.group(1)),h.group(2).replace("部","")); continue
        c=t[0] if t else ""
        if c in T and c not in seen and len(t)>10:
            seen.add(c)
            print(f"== {c} [{os.path.basename(f)}] 部={cur}")
            for k in range(max(0,j-4),j+1): print("   ",ps[k][:80])
    if len(seen)==len(T): break