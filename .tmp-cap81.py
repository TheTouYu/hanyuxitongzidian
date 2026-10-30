import urllib.request,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
for u in ["http://127.0.0.1:8091/glyphs/%E7%A5%A1/01.png","http://127.0.0.1:8091/glyphs/%E7%A5%A1/%E7%A5%A1/01.png","http://127.0.0.1:8091/glyphs/index.json"]:
    try:
        r=urllib.request.urlopen(u,timeout=5); print(r.status,len(r.read()),u)
    except Exception as e: print("ERR",getattr(e,"code",""),u)