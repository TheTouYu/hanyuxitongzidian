import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
idx=json.load(io.open(r"D:\系统汉字\web\public\cards\index.json",encoding="utf-8"))
for q in ("讫","说","铁","鸡","车","马","爱"):
    hit=[x.get("c") for x in idx if x.get("c")==q or q in (x.get("a") or [])]
    print(q,hit[:2])