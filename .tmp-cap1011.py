import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
idx=json.load(io.open(r"D:\系统汉字\web\public\cards\index.json",encoding="utf-8"))
for q in ("𠃜","𡰣"):
    print(q,[x["c"] for x in idx if q in (x.get("a") or []) or x["c"]==q])