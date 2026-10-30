import json,urllib.request,sys,time
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
u="http://127.0.0.1:8088/cards/index.json?v=%d"%int(time.time())
d=json.loads(urllib.request.urlopen(u,timeout=10).read().decode("utf-8"))
items=d if isinstance(d,list) else d.get("items",[])
q="雁"
hit=[x for x in items if x.get("c")==q or q in (x.get("a") or [])]
print("items",len(items))
print("hit",[(x.get("c"),x.get("h"),x.get("a"),x.get("lv")) for x in hit])