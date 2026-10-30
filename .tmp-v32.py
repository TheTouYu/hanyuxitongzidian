import io,json,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
for n in ["卷一雞","第一章士"]:
    d=json.load(io.open(rf"D:\系统汉字\web\public\cards\{n}.json",encoding="utf-8"))
    print("==",n)
    for s in d["sections"]:
        print("  ",s.get("key"),"|",s.get("label"),"|rows",len(s.get("rows",[])),"|groups",[(g.get("title"),len(g.get("rows",[])),tuple(g.get("header") or [])) for g in s.get("groups",[])],"|links",[l.get("label") for l in s.get("links",[])])