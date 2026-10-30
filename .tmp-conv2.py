import json,glob,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
n=skip=0
for f in glob.glob(C+r"\*.json"):
    if os.path.basename(f) in ("index.json","variants.json"): continue
    d=json.load(open(f,encoding="utf-8"))
    ch=d.get("char",""); lv=d.get("level",0)
    b=(d.get("bus") or [{}])[0]; name=b.get("name","") if isinstance(b,dict) else str(b)
    if lv in (1,2): continue
    if not name: skip+=1; continue
    secs=[s for s in d.get("sections",[]) if isinstance(s,dict)]
    if any(s.get("key")=="shiyi" for s in secs): continue
    txt=""; sm=""
    for s in secs:
        if s.get("key") in ("benyi","bengen","shiyi") and s.get("text"):
            txt=s["text"]; break
    if not txt:
        for s in secs:
            if s.get("text"): txt=s["text"]; break
    for s in secs:
        if s.get("key")=="shengmu" or s.get("label")=="声母义":
            sm=s.get("text",""); break
    if not txt: skip+=1; continue
    d["level"]=3; d["parent"]=name
    d["sections"]=[{"key":"shiyi","label":"释义","text":txt,"cites":[]}]+([{"key":"shengmu","label":"声母拟态","text":sm,"cites":[]}] if sm else [])
    json.dump(d,open(f,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("converted",n,"skipped",skip)