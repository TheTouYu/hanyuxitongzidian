import json,io,collections,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
idx=json.load(io.open(r"D:\系统汉字\web\public\cards\index.json",encoding="utf-8"))
c=collections.Counter(x.get("c") for x in idx)
dup={k:v for k,v in c.items() if v>1}
print("总",len(idx),"重复字",len(dup),list(dup.items())[:12])
for ch in ("枝","芰","歧"):
    print(ch,[ (x.get("c"),x.get("p"),x.get("lv")) for x in idx if x.get("c")==ch or ch in (x.get("a") or [])][:5])