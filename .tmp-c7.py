import json,urllib.request,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
idx=json.load(urllib.request.urlopen("http://127.0.0.1:8091/cards/index.json"))
print("第一章士 in idx:",[x for x in idx if "第一章" in x["c"]])
print("count ch0:",sum(1 for x in idx if x.get("b")==0))