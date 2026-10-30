import urllib.request,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
for p in ("/index.html","/test.html"):
    r=urllib.request.urlopen("http://127.0.0.1:8091"+p,timeout=5); h=r.read().decode("utf-8","replace")
    print(p,"strip:", "startsWith(ch2+'/')" in h, "photoBlock:", "const photoBlock" in h, "CAPS:", "window.CAPS" in h)