import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
for f in ("匃","曷"):
    d=json.load(io.open(rf"D:\系统汉字\web\public\cards\{f}.json",encoding="utf-8"))
    print("###",f)
    for s in d["sections"]:
        if s.get("key") in ("zizu",):
            for g in (s.get("groups") or []):
                print("==",g["title"][:24], len(g["rows"]))
                print("  ", " ".join(str(r[0])+"/"+str(r[1]) for r in g["rows"])[:400])
        if s.get("key")=="shengmu": print("  SM:",s["text"][:120])