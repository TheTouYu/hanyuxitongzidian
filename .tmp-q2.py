import urllib.request,urllib.parse,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
for ch in ("雁","鴈","睚"):
    u="http://127.0.0.1:8088/card/"+urllib.parse.quote(ch)
    try:
        r=urllib.request.urlopen(u,timeout=10); c=r.read().decode("utf-8","replace")
        print(ch,r.status,"final",r.geturl(),"figures",c.count("<figure>"))
    except Exception as e: print(ch,"ERR",e)