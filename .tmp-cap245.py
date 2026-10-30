# -*- coding: utf-8 -*-
import io,sys,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
# 1) 页面渲染
for p in [r"D:\系统汉字\web\public\test.html", r"D:\系统汉字\web\public\index.html"]:
    h=io.open(p,encoding="utf-8").read()
    if "s.gimgs" in h: print(p.split("\\")[-1],"already"); continue
    old="? '':`<p>${esc(s.text)}</p>`}"
    new="? '':`<p>${esc(s.text)}</p>${(s.gimgs||[]).map(f=>`<img class=\"gin\" src=\"glyphs/${f}\">`).join('')}`}"
    if old not in h:
        # 兜底：另一种写法
        old2="<p>${esc(s.text)}</p>`}"
        if old2 in h:
            h=h.replace(old2,"<p>${esc(s.text)}</p>${(s.gimgs||[]).map(f=>`<img class=\"gin\" src=\"glyphs/${f}\">`).join('')}`}",1)
            print(p.split("\\")[-1],"patched(alt)")
        else:
            print(p.split("\\")[-1],"MISS")
    else:
        h=h.replace(old,new,1); print(p.split("\\")[-1],"patched")
    if ".gin{" not in h:
        h=h.replace("</style>",".gin{height:1.6em;vertical-align:-0.4em;margin:0 3px;border:1px solid #eee}</style>",1)
    io.open(p,"w",encoding="utf-8",newline="\n").write(h)
# 2) 服务端
p=r"D:\系统汉字\web\server.mjs"; h=io.open(p,encoding="utf-8",errors="surrogateescape").read()
if "s.gimgs" not in h:
    old="else if (s.text) h+='<p>'+ext(s.text)+'</p>';"
    new="else if (s.text) { h+='<p>'+ext(s.text)+((s.gimgs||[]).map(f=>'<img class=\"cim\" src=\"/glyphs/'+f+'\">').join(''))+'</p>'; }"
    if old in h: h=h.replace(old,new,1); io.open(p,"w",encoding="utf-8",errors="surrogateescape",newline="\n").write(h); print("server patched")
    else: print("server MISS")
else: print("server already")