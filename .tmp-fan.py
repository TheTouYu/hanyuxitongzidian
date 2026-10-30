import urllib.request,urllib.parse,json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
c=urllib.request.urlopen("http://127.0.0.1:8088/card/"+urllib.parse.quote("反"),timeout=10).read().decode("utf-8","replace")
print("len",len(c),"figures",c.count("<figure>"),"rows",c.count("<tr>"))
i=c.find('class="pill"'); print(c[i:i+80] if i>0 else "no pill")
j=c.find('所属卷'); print(c[j-10:j+120] if j>0 else "no 卷")
print("alias:",c.count('a href="/card/'))