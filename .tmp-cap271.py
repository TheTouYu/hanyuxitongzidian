import json,io,sys,glob,collections
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
d=json.load(io.open(r"D:\系统汉字\web\public\cards\帝.json",encoding="utf-8"))
print("帝",[s["key"] for s in d["sections"]])
cnt=collections.Counter()
for p in glob.glob(r"D:\系统汉字\web\public\cards\*.json"):
    if p.endswith("index.json"): continue
    x=json.load(io.open(p,encoding="utf-8")); lv=x.get("level",3)
    ks=tuple(s["key"] for s in x.get("sections",[]))
    cnt[(lv,ks)]+=1
for k,v in cnt.most_common(4): print(v,k)