# -*- coding: utf-8 -*-
import io,json,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
old="""<td class="zc">${(g.links&&g.links[i])?"""
new="""<td class="${g.header?'':'zc'}">${(g.links&&g.links[i])?"""
for f in [r"D:\系统汉字\web\public\test.html",r"D:\系统汉字\web\public\index.html"]:
    h=io.open(f,encoding="utf-8").read()
    if old in h:
        h=h.replace(old,new,1); io.open(f,"w",encoding="utf-8",newline="\n").write(h); print(f.split("\\")[-1],"td class ok")
    else: print("MISS",f)
C=r"D:\系统汉字\web\public\cards"; p=rf"{C}\第一章士.json"; d=json.load(io.open(p,encoding="utf-8"))
for s in d["sections"]:
    if s.get("key")=="juan":
        s["groups"][0]["header"]=["卷目","音源","部属"]
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("表头改为 卷目/音源/部属")