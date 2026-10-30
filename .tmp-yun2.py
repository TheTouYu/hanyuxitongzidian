# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
G=r"D:\系统汉字\web\public\glyphs"; C=r"D:\系统汉字\web\public\cards"
ip=os.path.join(G,"index.json"); ix=json.load(io.open(ip,encoding="utf-8")); ch=ix["chars"]
files=[f for f in ch["彥"]["files"] if not f.startswith("云/")]
files.append("云/01.png"); ch["彥"]["files"]=files
json.dump({"chars":ch},io.open(ip,"w",encoding="utf-8"),ensure_ascii=False)
p=os.path.join(C,"彥.json"); d=json.load(io.open(p,encoding="utf-8"))
d["sections"]=[s for s in d["sections"] if s.get("key")!="canzheng"]
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print(files,[s.get("label") for s in d["sections"]])