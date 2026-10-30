import urllib.request,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
r=urllib.request.urlopen("http://127.0.0.1:8091/test.html",timeout=5)
print(dict(r.headers))
h=r.read().decode("utf-8","replace")
print("has strip:", "startsWith(ch2+'/')" in h, len(h))