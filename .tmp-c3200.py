import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"; n=0
for fn in os.listdir(C):
    if not fn.endswith(".json") or fn=="index.json": continue
    p=os.path.join(C,fn); d=json.load(io.open(p,encoding="utf-8"))
    ch=False
    for s in d.get("sections",[]):
        for g in s.get("groups",[]) or []:
            for r in g.get("rows",[]) or []:
                if isinstance(r,list) and len(r)>=3 and r[0].startswith("莧") and r[2].strip()=="天":
                    r[2]=""; ch=True
    if ch:
        json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1; print("改",fn)
print("共",n)