import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
for ch in ("㕞","刷","唰","涮"):
    d=json.load(io.open(rf"D:\系统汉字\web\public\cards\{ch}.json",encoding="utf-8"))
    print(ch,"lv",d.get("level"),"rootLevel",d.get("rootLevel"),"parent",d.get("parent"))