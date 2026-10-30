import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
d=json.load(io.open(r"D:\系统汉字\web\public\cards\台.json",encoding="utf-8"))
print("level",d.get("level"),"parent",d.get("parent"),"bus",d.get("bus"))
for s in d["sections"]:
    print("==",s.get("key"),s.get("label"))
    if s.get("groups"):
        for g in s["groups"]:
            print("  G:",g.get("title"),"rows",len(g.get("rows",[])))
    else: print("  ",(s.get("text") or "")[:80])