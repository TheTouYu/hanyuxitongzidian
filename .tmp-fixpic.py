# -*- coding: utf-8 -*-
import json,io,os,shutil,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
P=r"D:\系统汉字\web\public\glyphs\photos"
src=os.path.join(P,"乇","02.jpg"); dst=os.path.join(P,"馲")
os.makedirs(dst,exist_ok=True)
for f in os.listdir(dst): os.remove(os.path.join(dst,f))
shutil.move(src, os.path.join(dst,"01.jpg"))
idx=json.load(io.open(os.path.join(P,"index.json"),encoding="utf-8")); m=idx["photos"]
m["乇"]=[f for f in sorted(os.listdir(os.path.join(P,"乇")))]
m["馲"]=["01.jpg"]
json.dump(idx,io.open(os.path.join(P,"index.json"),"w",encoding="utf-8"),ensure_ascii=False)
cap=json.load(io.open(os.path.join(P,"captions.json"),encoding="utf-8"))["captions"]
cap["乇"]=["三星堆小頂尊銅人（商）"]
cap["馲"]=["沙漠的駱駝隊"]
json.dump({"captions":cap},io.open(os.path.join(P,"captions.json"),"w",encoding="utf-8"),ensure_ascii=False)
pj=r"D:\系统汉字\web\public\photos.js"; s=io.open(pj,encoding="utf-8").read()
s=re.sub(r'"乇":\s*\[[^\]]*\]\s*,?',"",s); s=re.sub(r'"馲":\s*\[[^\]]*\]\s*,?',"",s)
i=s.find("{"); add='"乇": ["01.png"], "馲": ["01.jpg"],'
s=s[:i+1]+add+s[i+1:]
open(pj,"w",encoding="utf-8",newline="\n").write(s)
print("乇",m["乇"],"馲",m["馲"],cap)