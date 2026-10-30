# -*- coding: utf-8 -*-
import json,io,os,shutil,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
G=r"D:\系统汉字\web\public\glyphs"; ip=os.path.join(G,"index.json")
ix=json.load(io.open(ip,encoding="utf-8")); chs=ix["chars"]
src=os.path.join(G,"厄"); dst=os.path.join(G,"戹")
files=chs.get("戹",{}).get("files") or []
n=len(files)
if os.path.isdir(src):
    for f in sorted(os.listdir(src)):
        if f.lower().endswith((".png",".jpg")):
            n+=1; name="%02d%s"%(n,os.path.splitext(f)[1]); shutil.move(os.path.join(src,f),os.path.join(dst,name))
            files.append("戹/"+name)
    if not os.listdir(src): os.rmdir(src)
chs["戹"]["files"]=files
ix["chars"]=chs
json.dump(ix,io.open(ip,"w",encoding="utf-8"),ensure_ascii=False)
print("戹 files",len(files))