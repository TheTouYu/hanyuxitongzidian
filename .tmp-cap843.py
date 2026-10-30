import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
idx=json.load(io.open(r"D:\系统汉字\web\public\cards\index.json",encoding="utf-8"))
for q in ("苔","抬"):
    print(q,"→",[(x.get("c"),x.get("pr")) for x in idx if x.get("c")==q or q in (x.get("a") or [])])