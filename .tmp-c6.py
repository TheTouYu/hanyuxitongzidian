import json,urllib.request,urllib.parse,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
B="http://127.0.0.1:8091/"
for n in ["第一章士","第二章谷","第十二章老"]:
    d=json.loads(urllib.request.urlopen(B+"cards/"+urllib.parse.quote(n)+".json",timeout=8).read().decode("utf-8"))
    labs=[(s["label"],len(s.get("groups",[]) and s["groups"][0].get("rows",[])) ) for s in d["sections"]]
    print(n,labs)
idx=json.loads(urllib.request.urlopen(B+"cards/index.json",timeout=10).read().decode("utf-8"))
print("chapters in index",[x["c"] for x in idx if x.get("ch")][:13])