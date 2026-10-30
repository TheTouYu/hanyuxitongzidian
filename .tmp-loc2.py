import docx,re,glob,os
targets=set("情慍懼憾志忠")
res={}
for f in sorted(glob.glob(r"D:\字谱智能体\*.docx")):
    try: ps=[p.text.strip() for p in docx.Document(f).paragraphs if p.text.strip()]
    except Exception: continue
    cur=None
    for i,t in enumerate(ps):
        h=re.match(r"^(\d{3})\.([^\s：]{1,6})",t)
        if h and "部" in t[:24]: cur=(int(h.group(1)),h.group(2).replace("部",""))
        if t and t[0] in targets and len(t)>6 and cur and t[0] not in res:
            res[t[0]]=(cur[0],cur[1],os.path.basename(f),t[:70])
for c in sorted(targets): print(c,res.get(c))