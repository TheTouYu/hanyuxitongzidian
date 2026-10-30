# -*- coding: utf-8 -*-
import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
for ch in ("乎","兮"):
    d=json.load(io.open(C+"\\"+ch+".json",encoding="utf-8"))
    print("=== ",ch," keys:",list(d.keys()))
    for s in d["sections"]:
        g=[(x["title"][:20],len(x["rows"])) for x in (s.get("groups") or [])]
        print(" -",s.get("key"),"|",s.get("label"),"| text",len(s.get("text") or ""),"| groups",g,"| gimgs",len(s.get("gimgs") or []),"| gdir",s.get("gdir"))