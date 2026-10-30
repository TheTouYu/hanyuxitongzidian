import io,json,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
for fn in ("卷一雞","卷八虎","卷十六犬"):
    d=json.load(io.open(rf"D:\系统汉字\web\public\cards\{fn}.json",encoding="utf-8"))
    print(fn, "char=",d.get("char"), "secs=",[s.get("key") for s in d["sections"]])
    for s in d["sections"]:
        for g in (s.get("groups") or []):
            print("   ",s.get("key"), g.get("header"), g["rows"][0][:2] if g.get("rows") else None)