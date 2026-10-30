# -*- coding: utf-8 -*-
import json,io,os,shutil,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
P=r"D:\系统汉字\web\public\glyphs\photos"
src=os.path.join(P,"𤷇"); dst=os.path.join(P,"國"); os.makedirs(dst,exist_ok=True)
files=sorted(os.listdir(src)) if os.path.isdir(src) else []
for f in files: shutil.move(os.path.join(src,f), os.path.join(dst,f))
if os.path.isdir(src): os.rmdir(src)
ip=os.path.join(P,"index.json"); ix=json.load(io.open(ip,encoding="utf-8")); m=ix["photos"]
m.pop("𤷇",None); m["國"]=files
json.dump({"photos":m},io.open(ip,"w",encoding="utf-8"),ensure_ascii=False)
cp=os.path.join(P,"captions.json"); cx=json.load(io.open(cp,encoding="utf-8")); c=cx["captions"]
c.pop("𤷇",None); c["國"]=["何尊（西周早期）","何尊銘文「宅茲中國」"]
json.dump({"captions":c},io.open(cp,"w",encoding="utf-8"),ensure_ascii=False)
p2=r"D:\系统汉字\web\public\glyphs\index.json"; g=json.load(io.open(p2,encoding="utf-8")); ch=g["chars"]
ch.setdefault("國",{})["photos"]=[{"file":f,"caption":c["國"][i]} for i,f in enumerate(files)]
json.dump({"chars":ch},io.open(p2,"w",encoding="utf-8"),ensure_ascii=False)
print("moved",files)