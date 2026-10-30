import io,json,glob,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
for f in glob.glob(r"D:\系统汉字\web\public\cards\第*章*.json"):
    d=json.load(io.open(f,encoding="utf-8"))
    hs=[(s.get("key"),[g.get("header") for g in (s.get("groups") or [])]) for s in d["sections"] if s.get("groups")]
    print(f.split("\\")[-1], hs[:3])