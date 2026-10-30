# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
G=r"D:\系统汉字\web\public\glyphs"
ix=json.load(io.open(os.path.join(G,"index.json"),encoding="utf-8")); chrs=ix["chars"]
src=os.path.join(G,"靃"); dst=os.path.join(G,"霍")
if os.path.isdir(src):
    os.makedirs(dst,exist_ok=True)
    for f in sorted(os.listdir(src)):
        os.replace(os.path.join(src,f), os.path.join(dst,f))
    os.rmdir(src)
files=["霍/"+x for x in sorted(os.listdir(dst))] if os.path.isdir(dst) else []
chrs["霍"]={"doc":"","variants":[],"files":files}; chrs.pop("靃",None)
json.dump({"chars":chrs},io.open(os.path.join(G,"index.json"),"w",encoding="utf-8"),ensure_ascii=False)
print("moved",len(files))