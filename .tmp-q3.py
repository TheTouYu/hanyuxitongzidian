import urllib.request,urllib.parse,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
u="http://127.0.0.1:8088/card/"+urllib.parse.quote("鴈")
c=urllib.request.urlopen(u,timeout=10).read().decode("utf-8","replace")
print("figures",c.count("<figure>"))
for m in re.finditer(r'src="(/glyphs/[^"]+)"',c): print(m.group(1))