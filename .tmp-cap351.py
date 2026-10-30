# -*- coding: utf-8 -*-
import json,io,os,sys,shutil
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
P=r"D:\系统汉字\web\public\glyphs\photos"
d=os.path.join(P,"蒂")
if os.path.isdir(d): shutil.rmtree(d)
for name in ("index.json","captions.json"):
    p=os.path.join(P,name); x=json.load(io.open(p,encoding="utf-8"))
    k="photos" if "photos" in x else "captions"
    x[k].pop("蒂",None)
    json.dump(x,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("已删 photos/蒂（花蒂属帝部头 p570，辣椒属啇 p604）")