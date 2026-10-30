# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
G=r"D:\系统汉字\web\public\glyphs"; C=r"D:\系统汉字\web\public\cards"
ip=os.path.join(G,"index.json"); ix=json.load(io.open(ip,encoding="utf-8")); ch=ix["chars"]
ch["彥"]["files"]=[f for f in ch["彥"]["files"] if f.startswith("彥/")]
json.dump({"chars":ch},io.open(ip,"w",encoding="utf-8"),ensure_ascii=False)
p=os.path.join(C,"彥.json"); d=json.load(io.open(p,encoding="utf-8"))
secs=[s for s in d["sections"] if s.get("key")!="ziatt"]
secs.insert(0,{"key":"ziatt","label":"云","gimgs":["云/01.png"]})
d["sections"]=secs
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print(ch["彥"]["files"],[s.get("label") for s in secs])