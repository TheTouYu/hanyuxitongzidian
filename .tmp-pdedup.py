# -*- coding: utf-8 -*-
import io,os,json,glob,hashlib,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
P=r"D:\系统汉字\web\public\glyphs\photos"
idx=json.load(io.open(os.path.join(P,"index.json"),encoding="utf-8")); ph=idx.get("photos") or idx
removed=0; changed=0
for d0 in os.listdir(P):
    dp=os.path.join(P,d0)
    if not os.path.isdir(dp): continue
    seen={}; keep=[]
    for f in sorted(os.listdir(dp)):
        fp=os.path.join(dp,f)
        if not os.path.isfile(fp): continue
        h=hashlib.sha1(open(fp,"rb").read()).hexdigest()
        if h in seen: os.remove(fp); removed+=1; continue
        seen[h]=1; keep.append(f)
    new=[]
    for i,f in enumerate(keep,1):
        ext=os.path.splitext(f)[1]
        tgt="%02d%s"%(i,ext)
        if f!=tgt: os.replace(os.path.join(dp,f),os.path.join(dp,tgt))
        new.append(tgt)
    if new and ph.get(d0)!=new: ph[d0]=new; changed+=1
json.dump({"photos":ph},io.open(os.path.join(P,"index.json"),"w",encoding="utf-8"),ensure_ascii=False)
print("删重复图",removed,"改索引",changed)