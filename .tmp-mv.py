# -*- coding: utf-8 -*-
import json,io,os,shutil,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
P=r"D:\系统汉字\web\public\glyphs\photos"
src=os.path.join(P,"何"); dst=os.path.join(P,"河"); os.makedirs(dst,exist_ok=True)
f=os.listdir(src)[0] if os.path.isdir(src) else None
if f:
    shutil.move(os.path.join(src,f), os.path.join(dst,f))
    os.rmdir(src)
ip=os.path.join(P,"index.json"); ix=json.load(io.open(ip,encoding="utf-8")); m=ix.get("photos") or ix
m.pop("何",None); m["河"]=[f]
json.dump({"photos":m},io.open(ip,"w",encoding="utf-8"),ensure_ascii=False)
cp=os.path.join(P,"captions.json"); cx=json.load(io.open(cp,encoding="utf-8")); cm=cx.get("captions") or cx
cm.pop("何",None); cm["河"]=["開封地段的黃河懸河"]
json.dump({"captions":cm},io.open(cp,"w",encoding="utf-8"),ensure_ascii=False)
print("moved",f)