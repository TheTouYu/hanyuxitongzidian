# -*- coding: utf-8 -*-
import json,io,os,shutil,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
G=r"D:\系统汉字\web\public\glyphs"
src=os.path.join(G,"反","17.png"); dst_dir=os.path.join(G,"阪"); os.makedirs(dst_dir,exist_ok=True)
shutil.move(src, os.path.join(dst_dir,"01.png"))
ix=json.load(io.open(os.path.join(G,"index.json"),encoding="utf-8")); ch=ix["chars"]
f=[x for x in ch["反"]["files"] if not x.endswith("反/17.png")]
ch["反"]["files"]=f
h=ch.get("阪") or {"doc":"","variants":[],"files":[]}
h["files"]=["阪/01.png"]
ch["阪"]=h
json.dump({"chars":ch},io.open(os.path.join(G,"index.json"),"w",encoding="utf-8"),ensure_ascii=False)
print("反",len(f),"阪",h["files"])