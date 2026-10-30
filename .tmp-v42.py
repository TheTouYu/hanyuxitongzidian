import io,json,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
for nm in ["卷八虎","卷九十秋","卷一百壽"]:
    d=json.load(io.open(rf"D:\系统汉字\web\public\cards\{nm}.json",encoding="utf-8"))
    for s in d["sections"]:
        if s.get("key")=="zizu":
            print(nm,[ (r[0],r[2]) for r in s["groups"][0]["rows"][:3]])