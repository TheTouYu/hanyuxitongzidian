import glob,re,docx
res={}
for f in sorted(glob.glob(r"D:\字谱智能体\*.docx")):
    try: d=docx.Document(f)
    except Exception: continue
    ns=[]
    for p in d.paragraphs:
        m=re.match(r"^(\d{2,3})\.[^\s]{1,3}部",p.text.strip())
        if m: ns.append(int(m.group(1)))
    if ns: res[f.split("\\")[-1]]=(min(ns),max(ns),len(set(ns)))
for k,v in sorted(res.items(),key=lambda x:x[1][0])[-8:]: print(k,v)