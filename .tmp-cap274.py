import json,io,glob,sys,collections
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
d=json.load(io.open(r"D:\系统汉字\web\public\cards\帝.json",encoding="utf-8"))
print("帝 level",d.get("level"),"keys",[s["key"] for s in d["sections"]])
C=collections.Counter(); no=0
for p in glob.glob(r"D:\系统汉字\web\public\cards\*.json"):
    if p.endswith("index.json"): continue
    x=json.load(io.open(p,encoding="utf-8"))
    ks=tuple(s["key"] for s in x.get("sections",[]))
    C[(x.get("level",3),ks)]+=1
    if not any(s.get("key") in ("benyi","bengen","shiyi") for s in x["sections"]): no+=1
for k,v in C.most_common(5): print(v,k)
print("无症状形内容栏的卡",no)