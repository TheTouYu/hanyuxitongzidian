import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
i=json.load(io.open(r"D:\系统汉字\web\public\cards\index.json",encoding="utf-8"))
for x in i:
    if x.get("c") in ("弔","鈟","䘟","𨑩"): print(x["c"], x.get("a"), x.get("h"))
hit=[x["c"] for x in i if x.get("c")=="吊" or "吊" in (x.get("a") or [])]
print("search 吊 ->",hit)