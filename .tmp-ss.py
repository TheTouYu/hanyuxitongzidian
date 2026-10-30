import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
for n in ("弟","乎","丂"):
    d=json.load(io.open(r"D:\系统汉字\web\public\cards\%s.json"%n,encoding="utf-8"))
    s=[x for x in d["sections"] if x.get("key") in ("suoshu","suoshuquan","suoshujuan")]
    print(n, json.dumps(s,ensure_ascii=False)[:300])