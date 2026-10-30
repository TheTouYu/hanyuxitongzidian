# -*- coding: utf-8 -*-
import json,io,os,sys,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
chang=json.load(io.open(r"D:\系统汉字\.tmp-changrows.json",encoding="utf-8"))
fan=json.load(io.open(r"D:\系统汉字\.tmp-fanrows.json",encoding="utf-8"))
def ch_py(txt):
    m=re.match(r"^([^\s（(]+)(?:（[^）]*）)?\s*([a-zA-Zāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜü]+)",txt)
    if m: return m.group(1),m.group(2)
    m=re.match(r"^([^\s（(]+)",txt); return (m.group(1) if m else txt),""

# 厂
p=os.path.join(C,"厂.json"); d=json.load(io.open(p,encoding="utf-8"))
d["bus"]=[{"num":35,"name":"厂"}]
g1=[("228","厂"),("229","山"),("230","水"),("231","目"),("232","山"),("233","女"),("234","厂"),("235","广"),("236",""),("237","广"),("238","女"),("239","")]
g2=[("241","火"),("242","貝"),("243","鳥")]
groups=[]
for title,items in (("①指“石”，表示懸崖或懸崖狀",g1),("②同“丂”，表示大雁",g2)):
    rs=[]
    for k,cat in items:
        t=chang[k]; ch,py=ch_py(t)
        rs.append([ch,py,cat,t])
    groups.append({"title":title,"note":"","rows":rs})
for s in d["sections"]:
    if s.get("key")=="zizu":
        s["text"]=""; s["groups"]=groups
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
# 反
p=os.path.join(C,"反.json"); d=json.load(io.open(p,encoding="utf-8"))
d["bus"]=[{"num":35,"name":"厂"}]
gA=["飯","返","䡊","阪","昄","汳","叛","眅","瓪","㽹","㤆","𡞟","扳","舨"]
gB=["板","蝂","魬","畈","仮","粄","販","版"]
cats={"飯":"食","返":"辵","䡊":"車","阪":"阜","昄":"日","汳":"水","叛":"半","眅":"目","瓪":"瓦","㽹":"疒","㤆":"心","𡞟":"女","扳":"手","舨":"舟",
"板":"木","蝂":"虫","魬":"魚","畈":"田","仮":"人","粄":"米","販":"貝","版":"片"}
groups=[]
for title,cs in (("①指翻轉、回返",gA),("②指反復",gB)):
    rs=[]
    for c in cs:
        t=fan[c]; ch,py=ch_py(t); rs.append([ch,py,cats[c],t])
    groups.append({"title":title,"note":"","rows":rs})
for s in d["sections"]:
    if s.get("key")=="zizu":
        s["text"]=""; s["groups"]=groups
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("rewritten")