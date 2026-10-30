# -*- coding: utf-8 -*-
import json,io,os,sys
from PIL import Image
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
P=r"D:\系统汉字\web\public\glyphs\photos"; G=r"D:\系统汉字\web\public\glyphs"
print("dirs",[d for d in os.listdir(P) if d in ("虖","㯉")])
# 1) 删除虖的图
d=os.path.join(P,"虖")
if os.path.isdir(d):
    import shutil; shutil.rmtree(d); print("rm 虖 dir")
for name,key in (("index.json","photos"),("captions.json","captions")):
    p=os.path.join(P,name); x=json.load(io.open(p,encoding="utf-8")); m=x.get(key) or x
    if "虖" in m: m.pop("虖"); json.dump({key:m},io.open(p,"w",encoding="utf-8"),ensure_ascii=False); print("cleaned",name)
gi=json.load(io.open(os.path.join(G,"index.json"),encoding="utf-8"))
if "虖" in gi.get("photos",{}): gi["photos"].pop("虖"); json.dump(gi,io.open(os.path.join(G,"index.json"),"w",encoding="utf-8"),ensure_ascii=False); print("cleaned glyph index 虖")
# 2) 裁掉 㯉 图底部水印
p=os.path.join(P,"㯉","01.jpg"); im=Image.open(p); w,h=im.size
im.crop((0,0,w,int(h*0.93))).save(p,quality=92); print("cropped",im.size,"->",(w,int(h*0.93)))