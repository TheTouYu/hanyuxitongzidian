# -*- coding: utf-8 -*-
import io,json,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
o1="第${esc(String(b.num||'?'))}部"
n1="${esc(b.num===0?('第'+(d.chapter||'一')+'章'):('第'+String(b.num||'?')+'部'))}"
o2="第${x.b||'?'}部"
n2="${x.ch?('第'+x.ch+'章'):('第'+(x.b||'?')+'部')}"
for f in [r"D:\系统汉字\web\public\test.html", r"D:\系统汉字\web\public\index.html"]:
    h=io.open(f,encoding="utf-8").read(); n=0
    if o1 in h: h=h.replace(o1,n1,1); n+=1
    if o2 in h: h=h.replace(o2,n2,1); n+=1
    io.open(f,"w",encoding="utf-8",newline="\n").write(h); print(f.split("\\")[-1],"replaced",n)
# 卷卡加 chapter，索引加 ch 字段
C=r"D:\系统汉字\web\public\cards"
d=json.load(io.open(C+r"\卷一雞.json",encoding="utf-8")); d["chapter"]="一"
json.dump(d,io.open(C+r"\卷一雞.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
p=r"D:\系统汉字\.tmp-rel2.py"; t=io.open(p,encoding="utf-8").read()
if '"ch":' not in t:
    import re
    t=re.sub(r'(items\.append\(\{)', r'\1"ch":d.get("chapter"),', t, count=1)
    io.open(p,"w",encoding="utf-8",newline="\n").write(t); print("builder ch")