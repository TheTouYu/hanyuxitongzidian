import urllib.request,urllib.parse,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
c=urllib.request.urlopen("http://127.0.0.1:8088/card/"+urllib.parse.quote("鴈"),timeout=10).read().decode("utf-8","replace")
i=c.find('class="pill"')
print("figures",c.count("<figure>"))
print(c[i-10:i+120] if i>0 else "no pill")