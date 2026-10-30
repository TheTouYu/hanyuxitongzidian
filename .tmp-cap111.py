# -*- coding: utf-8 -*-
import json,io,os,shutil,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
P=r"D:\系统汉字\web\public\glyphs\photos"
src=os.path.join(P,"𨜿"); dst=os.path.join(P,"款")
os.makedirs(dst,exist_ok=True)
moved=sorted(os.listdir(src))
for f in moved: shutil.move(os.path.join(src,f),os.path.join(dst,f))
os.rmdir(src)
for name in ("index.json","captions.json"):
    p=os.path.join(P,name); d=json.load(io.open(p,encoding="utf-8"))
    key="photos" if "photos" in d else "captions"
    m=d[key]
    if "𨜿" in m:
        m["款"]=m.pop("𨜿")
    json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("moved",moved,"to 款")