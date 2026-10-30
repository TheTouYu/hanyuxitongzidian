import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"; n=0; names=[]
for f in os.listdir(C):
    if not f.endswith(".json") or f in ("index.json","variants.json"): continue
    p=os.path.join(C,f)
    try: d=json.load(io.open(p,encoding="utf-8"))
    except Exception: continue
    if isinstance(d,dict) and "glyphs" in d:
        del d["glyphs"]; json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1; names.append(f)
print("dropped glyphs field:",n,names[:5])