import urllib.request,json,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
h=urllib.request.urlopen("http://127.0.0.1:8091/test.html",timeout=6).read().decode("utf-8","replace")
print("served grp:", "const grp=" in h, "groups-thead:", "g.header" in h, len(h))
c=json.load(urllib.request.urlopen("http://127.0.0.1:8091/cards/%E5%A5%9A.json",timeout=6))
print("served 奚 zizu:",[(g["title"],len(g["rows"])) for s in c["sections"] if s["key"]=="zizu" for g in (s.get("groups") or [])])