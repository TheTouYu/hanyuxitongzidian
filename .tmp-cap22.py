import urllib.request,json,urllib.parse,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
for ch in ("𧧘","栬"):
    try:
        d=json.loads(urllib.request.urlopen("http://127.0.0.1:8091/cards/"+urllib.parse.quote(ch)+".json",timeout=6).read().decode("utf-8"))
        print(ch,[s["key"] for s in d["sections"]],d.get("bus"))
    except Exception as e: print(ch,"ERR",e)