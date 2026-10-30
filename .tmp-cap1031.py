import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"; n=0
for fn in os.listdir(C):
    if not fn.endswith(".json") or fn=="index.json": continue
    p=os.path.join(C,fn)
    try: d=json.load(io.open(p,encoding="utf-8"))
    except: continue
    if not isinstance(d,dict): continue
    ch=d.get("char") or fn[:-5]; chg=False
    if "parent" not in d: d["parent"]=""; chg=True
    if "rootLevel" not in d: d["rootLevel"]=1 if d.get("level")==1 else 3; chg=True
    if chg:
        json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("规范字段",n)