# -*- coding: utf-8 -*-
import sys,os,json,io,glob,shutil
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
ROOT=r"D:\系统汉字"; PH=os.path.join(ROOT,"web","public","glyphs","photos"); TMP=os.path.join(ROOT,".tmp-photos-new")
IDX=json.load(io.open(os.path.join(PH,"index.json"),encoding="utf-8")); OLD=IDX.get("photos") or IDX
n=0; owners=set()
for p in sorted(glob.glob(os.path.join(TMP,"*@@*.png"))):
    base=os.path.basename(p); owner=base.split("@@")[0]
    dst=os.path.join(PH,owner); os.makedirs(dst,exist_ok=True)
    files=OLD.get(owner) or [f for f in sorted(os.listdir(dst))]
    m=len(files)+1; fn=f"{m:02d}.png"
    shutil.copyfile(p,os.path.join(dst,fn)); files.append(fn)
    OLD[owner]=files; owners.add(owner); n+=1
json.dump({"photos":OLD},io.open(os.path.join(PH,"index.json"),"w",encoding="utf-8"),ensure_ascii=False)
print("并入 EMF->PNG",n,"涉及字头",len(owners))
print("有图字头",len([1 for v in OLD.values() if v]))