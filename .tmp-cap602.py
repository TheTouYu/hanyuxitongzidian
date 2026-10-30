# -*- coding: utf-8 -*-
import json,io,os,shutil,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
P=r"D:\系统汉字\web\public\glyphs\photos"
src=os.path.join(P,"𥎭"); dst=os.path.join(P,"知")
os.makedirs(dst,exist_ok=True)
for f in os.listdir(dst): os.remove(os.path.join(dst,f))
moved=[]
for f in os.listdir(src):
    shutil.move(os.path.join(src,f),os.path.join(dst,f)); moved.append(f)
os.rmdir(src)
idx=json.load(io.open(os.path.join(P,"index.json"),encoding="utf-8")); ph=idx.get("photos") or idx
cap=json.load(io.open(os.path.join(P,"captions.json"),encoding="utf-8")); cm=cap.get("captions") or cap
ph.pop("𥎭",None); c=cm.pop("𥎭",["《春園試箭圖》（清 焦秉貞）"])
ph["知"]=moved; cm["知"]=c if isinstance(c,list) else [c]
json.dump({"photos":ph},io.open(os.path.join(P,"index.json"),"w",encoding="utf-8"),ensure_ascii=False)
json.dump({"captions":cm},io.open(os.path.join(P,"captions.json"),"w",encoding="utf-8"),ensure_ascii=False)
print("moved",moved,"cap",cm["知"])