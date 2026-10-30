# -*- coding: utf-8 -*-
import io,glob,json,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
old="<table class=\"ct\"><thead><tr><th>字</th><th>读音</th><th>类属</th><th>取义落点</th></tr></thead><tbody>"
new="<table class=\"ct\"><thead><tr>${((g.title||'').indexOf('部目')>=0?['部目','字根','中心义','字族']:(g.header||['字','读音','类属','取义落点'])).map(t=>'<th>'+esc(t)+'</th>').join('')}</tr></thead><tbody>"
for f in [r"D:\系统汉字\web\public\test.html",r"D:\系统汉字\web\public\index.html"]:
    h=io.open(f,encoding="utf-8").read(); n=h.count(old); h=h.replace(old,new)
    io.open(f,"w",encoding="utf-8",newline="\n").write(h); print(f.split("\\")[-1],"tbl",n)
C=r"D:\系统汉字\web\public\cards"
for f in glob.glob(C+r"\卷*.json"):
    d=json.load(io.open(f,encoding="utf-8")); ch=False
    for s in d["sections"]:
        if s.get("text") in ("（原稿本卷卷首无此项。）","原稿本卷无卷首导言，直接列部目。","本卷总说见原稿卷首。","音系即本卷所属诸部（下表）。","（原稿本卷卷首无此项）"):
            s["text"]=""; ch=True
    d["sections"]=[s for s in d["sections"] if (s.get("text") or s.get("groups"))]
    if ch: json.dump(d,io.open(f,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("清占位")