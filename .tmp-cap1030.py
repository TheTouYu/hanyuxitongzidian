import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
for ch in ("矢","尸"):
    d=json.load(io.open(rf"D:\系统汉字\web\public\cards\{ch}.json",encoding="utf-8"))
    print(ch,"bus",d.get("bus"),"level",d.get("level"),"rootLevel",d.get("rootLevel"),"keys",sorted(d))