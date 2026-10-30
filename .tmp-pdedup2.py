# -*- coding: utf-8 -*-
import io,os,json,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from PIL import Image
P=r"D:\系统汉字\web\public\glyphs\photos"
idx=json.load(io.open(os.path.join(P,"index.json"),encoding="utf-8")); ph=idx.get("photos") or idx
def ah(fp):
    try:
        im=Image.open(fp).convert("L").resize((8,8))
        px=list(im.getdata()); avg=sum(px)/64
        return "".join("1" if p>avg else "0" for p in px)
    except Exception: return None
rem=0; ch=0
for d0 in os.listdir(P):
    dp=os.path.join(P,d0)
    if not os.path.isdir(dp): continue
    seen={}; keep=[]
    for f in sorted(os.listdir(dp)):
        fp=os.path.join(dp,f)
        if not os.path.isfile(fp): continue
        h=ah(fp)
        if h and h in seen: os.remove(fp); rem+=1; continue
        if h: seen[h]=1
        keep.append(f)
    new=[]
    for i,f in enumerate(keep,1):
        ext=os.path.splitext(f)[1]; tgt="%02d%s"%(i,ext)
        if f!=tgt: os.replace(os.path.join(dp,f),os.path.join(dp,tgt))
        new.append(tgt)
    if new!=ph.get(d0): ph[d0]=new; ch+=1
json.dump({"photos":ph},io.open(os.path.join(P,"index.json"),"w",encoding="utf-8"),ensure_ascii=False)
print("感知去重删",rem,"改索引",ch)