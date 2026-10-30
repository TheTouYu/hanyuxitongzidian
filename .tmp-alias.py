# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
add={"濾":"滤","鑢":"铝","櫖":"榈","臚":"胪","廬":"庐","瀘":"泸","鱸":"鲈","爐":"炉","攄":"摅","慮":"虑","驢":"驴","鸕":"鸬","顱":"颅","艫":"舮"}
n=0
for t,s in add.items():
    p=os.path.join(C,t+".json")
    if not os.path.exists(p): continue
    d=json.load(io.open(p,encoding="utf-8"))
    al=set(d.get("aliases") or []); al.add(s); d["aliases"]=sorted(al)
    json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
# variants.json 补映射
vp=r"D:\系统汉字\web\public\cards\variants.json"
v=json.load(io.open(vp,encoding="utf-8"))
for t,s in add.items():
    if s not in v: v[s]=[t]
json.dump(v,io.open(vp,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("aliases added",n)