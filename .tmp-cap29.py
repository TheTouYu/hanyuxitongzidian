import urllib.request,urllib.parse,json,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
for ch in ("𧧘","𨋭","栬"):
    try:
        raw=urllib.request.urlopen("http://127.0.0.1:8091/cards/"+urllib.parse.quote(ch)+".json",timeout=6).read().decode("utf-8")
        d=json.loads(raw)
        print(ch,"ok",list(d.keys()),[s["key"] for s in d["sections"]])
    except Exception as e: print(ch,"ERR",repr(e)[:120])