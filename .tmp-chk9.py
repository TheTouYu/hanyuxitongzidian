import json,urllib.request,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
for p in ("test.html","index.html"):
    h=urllib.request.urlopen("http://127.0.0.1:8091/"+p,timeout=8).read().decode("utf-8")
    print(p,"200" if h else "?", "norm(x.a)!==q" in h, "((x.a||[]).includes(q))" in h)