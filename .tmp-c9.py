import json,urllib.request,urllib.parse,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
d=json.loads(urllib.request.urlopen("http://127.0.0.1:8091/cards/"+urllib.parse.quote("第一章士")+".json",timeout=8).read().decode("utf-8"))
for s in d["sections"]:
    n=len(s.get("text") or "")
    rows=len(s.get("groups",[{}])[0].get("rows",[])) if s.get("groups") else 0
    print(s["label"],"字数",n,"表行",rows)