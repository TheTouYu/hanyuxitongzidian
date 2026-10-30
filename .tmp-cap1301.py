# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
pairs=[("隔","估"),("口","控"),("豁","活"),("聚","决"),("亲","缺"),("续","消"),("闭","剥"),("拼","辟"),("附","分"),("蒙","末"),("囤","动"),("涂","突"),("纳","弄"),("柔","锐"),("拢","离"),("凿","总"),("总","凿"),("刺","持"),("持","刺"),("失","收"),("收","失")]
bad=[]
for fn in os.listdir(C):
    if not fn.endswith(".json") or fn=="index.json": continue
    d=json.load(io.open(os.path.join(C,fn),encoding="utf-8"))
    for s in d.get("sections",[]):
        if s.get("key")!="shengmu": continue
        t=s.get("text","")
        m=re.search(r"取「(.)」",t)
        if not m: continue
        q=m.group(1); rest=t[m.end():]
        for a,b in pairs:
            if q==a and b in rest:
                bad.append((d.get("char"),q,b,t[:60])); break
print(len(bad))
for x in bad[:12]: print(x[0],x[1],"→含",x[2],"|",x[3])