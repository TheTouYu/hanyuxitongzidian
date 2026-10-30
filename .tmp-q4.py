import urllib.request,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
for u in ("http://127.0.0.1:8088/glyphs/%E9%9B%81/01.png","http://127.0.0.1:8088/glyphs/%E9%9B%81/02.png"):
    try:
        r=urllib.request.urlopen(u,timeout=8); print(u[-20:],r.status,len(r.read()))
    except Exception as e: print("ERR",e)