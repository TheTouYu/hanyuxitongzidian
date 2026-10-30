# -*- coding: utf-8 -*-
import io,json,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
old="""g.rows.map(r=>`<tr><td class="zc">${esc(r[0])}</td>"""
new="""g.rows.map((r,i)=>`<tr><td class="zc">${(g.links&&g.links[i])?('<a href="javascript:void(0)" onclick="goCard(\\''+g.links[i]+'\\')">'+esc(r[0])+'</a>'):esc(r[0])}</td>"""
for f in [r"D:\系统汉字\web\public\test.html",r"D:\系统汉字\web\public\index.html"]:
    h=io.open(f,encoding="utf-8").read()
    if old in h:
        h=h.replace(old,new,1); io.open(f,"w",encoding="utf-8",newline="\n").write(h); print(f.split("\\")[-1],"grp links ok")
    else: print("MISS",f)
C=r"D:\系统汉字\web\public\cards"; p=rf"{C}\第一章士.json"; d=json.load(io.open(p,encoding="utf-8"))
d["sections"]=[s for s in d["sections"] if s.get("key")!="lian"]
for s in d["sections"]:
    if s.get("key")=="juan":
        s["groups"][0]["links"]=["卷一雞","卷二㠯","","","","",""]
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("章卡：删链接栏，卷表行加链接")