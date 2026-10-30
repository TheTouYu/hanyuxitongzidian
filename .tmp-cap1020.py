import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
d=json.load(io.open(r"D:\系统汉字\web\public\cards\尸.json",encoding="utf-8"))
print("keys",sorted(d.keys()))
for s in d["sections"]:
    print(s["key"],"|label",s.get("label"),"|len(text)",len(s.get("text") or ""),"|groups",len(s.get("groups") or []),"|links",len(s.get("links") or []))
    for g in s.get("groups") or []:
        for r in g.get("rows") or []:
            if len(r)!=4: print("  BADROW",g.get("title"),r)