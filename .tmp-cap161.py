import json,io,glob,sys,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
for p in glob.glob(r"D:\系统汉字\web\public\cards\卷*.json"):
    t=io.open(p,encoding="utf-8").read()
    if "欠部" in t:
        d=json.load(io.open(p,encoding="utf-8")); print(p)
        for s in d["sections"]:
            for g in (s.get("groups") or []):
                for r in g["rows"][:3]: print("  ",r)
        break