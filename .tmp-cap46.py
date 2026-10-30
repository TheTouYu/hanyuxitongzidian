import json,io,sys,glob,collections
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
d=json.load(io.open(r"D:\系统汉字\web\public\cards\貍.json",encoding="utf-8"))
for s in d["sections"]: print(s["key"],"|",s["label"],"| groups",len(s.get("groups") or []),"| text",repr(s.get("text","")[:20]))
print("---- cards with duplicate keys ----")
n=0
for f in glob.glob(r"D:\系统汉字\web\public\cards\*.json"):
    if f.endswith("index.json"): continue
    c=json.load(io.open(f,encoding="utf-8")); ks=[s["key"] for s in c.get("sections",[])]
    dup=[k for k,v in collections.Counter(ks).items() if v>1]
    if dup: n+=1
print("dup",n)