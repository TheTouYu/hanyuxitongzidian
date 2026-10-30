# -*- coding: utf-8 -*-
import json,io,os,hashlib,sys,shutil
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
G=r"D:\系统汉字\web\public\glyphs"; C=r"D:\系统汉字\web\public\cards"
def h(p): return hashlib.sha256(open(p,"rb").read()).hexdigest()
# 从 乇 目录取前 9 形的原始字节（与 p286 前九图相同）
tuo=sorted(os.listdir(os.path.join(G,"乇")))
d=os.path.join(G,"宅"); os.makedirs(d,exist_ok=True)
for f in os.listdir(d): os.remove(os.path.join(d,f))
names=[]
for i,f in enumerate(tuo[:9],1):
    n="%02d.png"%i; shutil.copyfile(os.path.join(G,"乇",f),os.path.join(d,n)); names.append(n)
gi=json.load(io.open(os.path.join(G,"index.json"),encoding="utf-8"))
gi["宅"]={"doc":"卷七 斤","files":names}
json.dump(gi,io.open(os.path.join(G,"index.json"),"w",encoding="utf-8"),ensure_ascii=False)
p=os.path.join(C,"宅.json"); c=json.load(io.open(p,encoding="utf-8"))
c["sections"]=[s for s in c["sections"] if s.get("key")!="zixing"]
i=next((k for k,s in enumerate(c["sections"]) if s.get("key")=="zizu"),len(c["sections"]))
c["sections"].insert(i,{"key":"zixing","label":"字形","files":names})
json.dump(c,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("宅 glyphs",names)