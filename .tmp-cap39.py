import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
idx=json.load(io.open(r"D:\系统汉字\web\public\cards\index.json",encoding="utf-8"))
for x in idx:
    if x.get("c") in ("灔","艷"):
        print(x.get("c"),"aliases",x.get("a"))
print("search 艳:",[x.get("c") for x in idx if "艳" in (x.get("a") or [])])