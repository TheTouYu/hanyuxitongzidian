import json,urllib.request,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
idx=json.load(urllib.request.urlopen("http://127.0.0.1:8091/cards/index.json"))
print("index",len(idx),"| 㠯 entry:",[x for x in idx if x["c"]=="㠯"][0]["a"])
for q in ["以","似","台","爱","干","发"]:
    hit=[x["c"] for x in idx if x["c"]==q or (isinstance(x.get("a"),list) and q in x["a"])]
    print(q,"->",hit[:4])