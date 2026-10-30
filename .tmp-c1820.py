import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
d=json.load(io.open(r"D:\系统汉字\web\public\cards\肥.json",encoding="utf-8"))
print("head",d.get("head"),"py",d.get("pinyin"),"lv",d.get("level"),"parent",d.get("parent"))
for s in d["sections"]:
    print("==",s["label"])
    print((s.get("text") or "")[:220])
    for g in s.get("groups",[]) or []:
        print("  #",g.get("title"),len(g.get("rows",[])))