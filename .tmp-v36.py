import io,json,collections,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
idx=json.load(io.open(r"D:\系统汉字\web\public\cards\index.json",encoding="utf-8"))
v=[x["c"] for x in idx if x.get("c","").startswith("卷")]
print("vols",len(v),"uniq",len(set(v)))
print([k for k,n in collections.Counter(v).items() if n>1])
print([c for c in v if c.startswith("卷一") or c.startswith("卷二")])