import urllib.request,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
for u in ["http://127.0.0.1:8091/test.html","http://127.0.0.1:8091/cards/index.json"]:
    try:
        r=urllib.request.urlopen(u,timeout=5); print(r.status,len(r.read()),u)
    except Exception as e: print("ERR",getattr(e,"code",e),u)