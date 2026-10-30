import json,urllib.request,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
idx=json.load(urllib.request.urlopen("http://127.0.0.1:8091/cards/index.json"))
for q in ["似","佀","以","台"]:
    hit=[x["c"] for x in idx if x["c"]==q or (isinstance(x.get("a"),list) and q in x["a"])]
    print(q,"->",hit[:4])