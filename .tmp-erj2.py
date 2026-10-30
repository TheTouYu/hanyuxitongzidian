import glob,json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
s=0
for f in glob.glob(r"D:\系统汉字\web\public\cards\*.json"):
    try: d=json.load(io.open(f,encoding="utf-8"))
    except Exception: continue
    if not isinstance(d,dict): continue
    secs=d.get("sections") or []
    if not isinstance(secs,list): continue
    e=[x for x in secs if isinstance(x,dict) and x.get("key")=="erji"]
    if e:
        print(f.split("\\")[-1], json.dumps(e[0],ensure_ascii=False)[:300]); s+=1
    if s>=3: break
print("found",s)