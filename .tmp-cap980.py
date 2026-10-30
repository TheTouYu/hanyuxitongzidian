import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
for ch in ("尸","尺"):
    d=json.load(io.open(rf"D:\系统汉字\web\public\cards\{ch}.json",encoding="utf-8"))
    print(ch,"level",d.get("level"),"parent",d.get("parent"))
    for s in d["sections"]:
        if s["key"]=="zizu":
            for g in s.get("groups",[]):
                print("   ",g.get("title"),[r[0] for r in g.get("rows",[])][:8])