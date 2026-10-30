# -*- coding: utf-8 -*-
import json,io,os,hashlib,sys,shutil
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
G=r"D:\系统汉字\web\public\glyphs"; C=r"D:\系统汉字\web\public\cards"
def h(p): return hashlib.sha256(open(p,"rb").read()).hexdigest()
have={h(os.path.join(G,"乇",f)) for f in os.listdir(os.path.join(G,"乇"))}
src=os.path.join(G,"宅")
new=[]
if os.path.isdir(src):
    for f in sorted(os.listdir(src)):
        k=h(os.path.join(src,f))
        if k not in have:
            n="%02d.png"%(len(os.listdir(os.path.join(G,"乇")))+1)
            shutil.copyfile(os.path.join(src,f), os.path.join(G,"乇",n)); have.add(k); new.append(n)
    shutil.rmtree(src)
gi=json.load(io.open(os.path.join(G,"index.json"),encoding="utf-8"))
gi.pop("宅",None)
gi["乇"]={"doc":"卷七 斤","files":sorted(os.listdir(os.path.join(G,"乇")))}
json.dump(gi,io.open(os.path.join(G,"index.json"),"w",encoding="utf-8"),ensure_ascii=False)
p=os.path.join(C,"宅.json"); d=json.load(io.open(p,encoding="utf-8"))
d["sections"]=[s for s in d["sections"] if s.get("key")!="zixing"]
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("appended to 乇:",new,"total",len(os.listdir(os.path.join(G,"乇"))))