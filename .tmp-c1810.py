import json,io,sys,os
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
for ch in ("配","邑","嶏","悒"):
    d=json.load(io.open(os.path.join(C,ch+".json"),encoding="utf-8"))
    print(ch,"parent",d.get("parent"),"lv",d.get("level"),[s["label"] for s in d["sections"]])