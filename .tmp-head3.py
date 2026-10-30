import glob,re,docx
for f in sorted(glob.glob(r"D:\修订\x\*.docx")):
    try: d=docx.Document(f)
    except Exception: continue
    ns=[]
    for p in d.paragraphs:
        m=re.match(r"^(\d{2,3})\.[^\s]{1,3}部",p.text.strip())
        if m: ns.append(int(m.group(1)))
    print(f.split("\\")[-1], "部数", len(set(ns)), "范围", (min(ns),max(ns)) if ns else None)