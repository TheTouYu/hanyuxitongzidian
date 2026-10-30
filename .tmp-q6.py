import urllib.request,urllib.parse,json,sys,time
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
c=urllib.request.urlopen("http://127.0.0.1:8088/card/"+urllib.parse.quote("鴈"),timeout=10).read().decode("utf-8","replace")
print("figures",c.count("<figure>"))
print("第35部", "第35部" in c or "35" in c)
u="http://127.0.0.1:8088/glyphs/index.json?v=%d"%int(time.time())
e=json.loads(urllib.request.urlopen(u,timeout=10).read().decode("utf-8")).get("chars")
print("files",len(e["鴈"]["files"]))