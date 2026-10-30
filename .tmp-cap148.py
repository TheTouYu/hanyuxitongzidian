import json,io,glob,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
out=[]
for p in glob.glob(r"D:\系统汉字\web\public\cards\*.json"):
    if "index" in p: continue
    try: d=json.load(io.open(p,encoding="utf-8"))
    except: continue
    b=d.get("bus") or []
    if b and isinstance(b,list) and b[0].get("num")==5:
        out.append((d["char"],d.get("pinyin","")))
print(len(out)); print(" ".join(c+"/"+p for c,p in out))