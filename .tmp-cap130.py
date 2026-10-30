import urllib.request,sys,json
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
for u in ["http://127.0.0.1:8091/test.html","http://127.0.0.1:8091/cards/index.json","http://127.0.0.1:8091/cards/%E7%A4%BA.json"]:
    try:
        r=urllib.request.urlopen(u,timeout=5); print(r.status,len(r.read()),u)
    except Exception as e: print("ERR",getattr(e,"code",e),u)