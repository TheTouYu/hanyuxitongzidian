import json,io,glob,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
out=[]
for p in glob.glob(r"D:\系统汉字\web\public\cards\*.json"):
    if "index" in p or "variants" in p: continue
    try: d=json.load(io.open(p,encoding="utf-8"))
    except: continue
    b=d.get("bus") or []
    num=None
    if isinstance(b,list) and b and isinstance(b[0],dict): num=b[0].get("num")
    if num==5: out.append((d["char"],d.get("pinyin","")))
print(len(out)); print(" ".join(c+"/"+p for c,p in out))