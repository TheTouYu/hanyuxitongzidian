import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
idx=json.load(io.open(r"D:\系统汉字\web\public\cards\index.json",encoding="utf-8"))
for q in ("杘","鳲","㕞","刷","唰","涮","𢯍","㞋","㕧","屎","𥻐","䐅","𡱁"):
    hit=[x["c"] for x in idx if x["c"]==q or q in (x.get("a") or [])]
    print(q,hit)