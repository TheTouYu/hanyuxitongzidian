# -*- coding: utf-8 -*-
import io,json,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
old="""<thead><tr><th>字</th><th>读音</th><th>类属</th><th>取义落点</th></tr></thead>"""
new="""<thead><tr>${(g.header||['字','读音','类属','取义落点']).map(t=>'<th>'+esc(t)+'</th>').join('')}</tr></thead>"""
for f in [r"D:\系统汉字\web\public\test.html",r"D:\系统汉字\web\public\index.html"]:
    h=io.open(f,encoding="utf-8").read()
    if old in h:
        h=h.replace(old,new,1); io.open(f,"w",encoding="utf-8",newline="\n").write(h); print(f.split("\\")[-1],"header ok")
    else: print("MISS",f)
C=r"D:\系统汉字\web\public\cards"; p=rf"{C}\第一章士.json"; d=json.load(io.open(p,encoding="utf-8"))
for s in d["sections"]:
    if s.get("key")=="juan":
        g=s["groups"][0]; g["title"]="卷一至卷七"; g["header"]=["卷","部目","部数"]
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("卷表头恢复三列：卷/部目/部数")