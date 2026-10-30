# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
M={"和":"口","龢":"龠","鉌":"金","訸":"言","惒":"心","啝":"口","柇":"木","姀":"女","盉":"皿","䒩":"艸","蝌":"虫","犐":"牛","䈖":"竹","萪":"艸"}
p=os.path.join(C,"禾.json"); d=json.load(io.open(p,encoding="utf-8"))
for s in d.get("sections",[]):
    if s.get("key")=="zizu":
        for g in s.get("groups",[]):
            for r in g.get("rows",[]):
                b=r[0].split("（")[0]
                if b in M: r[2]=M[b]
        print([(r[0],r[2]) for r in s["groups"][0]["rows"]][:6])
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
# 审计：族表类属全部为同一值（疑似常数填充）的卡
bad=[]
for fn in sorted(os.listdir(C)):
    if not fn.endswith(".json") or fn in ("index.json","variants.json"): continue
    try: dd=json.load(io.open(os.path.join(C,fn),encoding="utf-8"))
    except Exception: continue
    for s in dd.get("sections",[]):
        if s.get("key")=="zizu":
            for g in s.get("groups",[]):
                rows=g.get("rows",[])
                if len(rows)>=3:
                    vals={r[2] for r in rows if len(r)>2}
                    if len(vals)==1 and list(vals)[0]: bad.append((dd.get("char"),list(vals)[0],len(rows)))
print("uniform-class cards:",len(bad))
print(bad[:20])