import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
for ch in ("尺","耆","稽","旨"):
    d=json.load(io.open(rf"D:\系统汉字\web\public\cards\{ch}.json",encoding="utf-8"))
    print("==",ch,"lv",d.get("level"),"parent",d.get("parent"))
    for s in d["sections"]:
        g=s.get("groups"); print("  -",s.get("key"),s.get("label"),"groups",len(g) if g else 0,"rows",sum(len(x.get("rows",[])) for x in g) if g else 0,"links",len(s.get("links",[]) or []),"text",(s.get("text") or "")[:22])