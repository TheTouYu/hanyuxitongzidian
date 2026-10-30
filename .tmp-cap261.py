# -*- coding: utf-8 -*-
import io,sys,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
for p in [r"D:\系统汉字\web\public\test.html", r"D:\系统汉字\web\public\index.html"]:
    h=io.open(p,encoding="utf-8").read()
    if "const gt=" not in h:
        m=re.search(r"function esc\(s\)\{[^\n]*\}", h)
        if m:
            ins=m.group(0)+"\nconst gt=(t,dir)=>esc(t).replace(/\\{\\{([^}]+)\\}\\}/g,(m,f)=>`<img class=\"gin\" src=\"glyphs/${dir}/${f}\">`);"
            h=h.replace(m.group(0),ins,1)
        else:
            print(p,"esc MISS"); continue
    n=h.count("esc(s.text)")
    h=h.replace("esc(s.text)","(s.gdir?gt(s.text,s.gdir):esc(s.text))")
    io.open(p,"w",encoding="utf-8",newline="\n").write(h)
    print(p.split("\\")[-1],"replaced",n)
p=r"D:\系统汉字\web\server.mjs"; h=io.open(p,encoding="utf-8",errors="surrogateescape").read()
old="else if (s.text) { h+='<p>'+ext(s.text)+((s.gimgs||[]).map(f=>'<img class=\"cim\" src=\"/glyphs/'+f+'\">').join(''))+'</p>'; }"
new="else if (s.text) { let tx=String(s.text).replace(/\\{\\{([^}]+)\\}\\}/g,(m,f)=>'\\u0001'+((s.gdir||'')+'/'+f)+'\\u0001'); h+='<p>'+ext(tx).replace(/\\u0001([^\\u0001]+)\\u0001/g,(m,f)=>'<img class=\"cim\" src=\"/glyphs/'+f+'\">')+'</p>'; }"
if old in h:
    h=h.replace(old,new,1); io.open(p,"w",encoding="utf-8",errors="surrogateescape",newline="\n").write(h); print("server patched")
else: print("server MISS")