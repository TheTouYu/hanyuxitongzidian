# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
G=r"D:\系统汉字\web\public\glyphs"
def write(d,files):
    for f in os.listdir(d): os.remove(os.path.join(d,f))
d1=os.path.join(G,"叚"); d2=os.path.join(G,"豭")
# 取回当前 叚 的 1-8（已是前 8）；豭 = 叚 的 09-16（原属豭）+ 现豭 3
move=[f for f in sorted(os.listdir(d1)) if os.path.basename(f)[:2] in ("09","10","11","12","13","14","15","16")]
n=len([f for f in os.listdir(d2)])
for i,m in enumerate(move):
    os.rename(os.path.join(d1,m), os.path.join(d2,"%02d.png"%(n+i+1)))
p=os.path.join(G,"index.json"); g=json.load(io.open(p,encoding="utf-8")); ch=g["chars"]
ch["叚"]["files"]=["叚/%02d.png"%(i+1) for i in range(8)]
cnt=len([f for f in os.listdir(d2)])
ch["豭"]["files"]=["豭/%02d.png"%(i+1) for i in range(cnt)]
json.dump({"chars":ch},io.open(p,"w",encoding="utf-8"),ensure_ascii=False)
print("叚",8,"豭",cnt)