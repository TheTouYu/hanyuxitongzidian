import io,json,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
d=json.load(io.open(r"D:\系统汉字\web\public\cards\第一章士.json",encoding="utf-8"))
for s in d["sections"]:
    print(s.get("key"), "|", s.get("label"), "| rows?", bool(s.get("rows")), "groups?", [ (g.get("title"),len(g.get("rows",[])),g.get("header")) for g in s.get("groups",[]) ], "links?", s.get("links"))