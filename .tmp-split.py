# -*- coding: utf-8 -*-
import json,io,os,shutil,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
G=r"D:\系统汉字\web\public\glyphs"
src=os.path.join(G,"䖒"); dst=os.path.join(G,"戲")
os.makedirs(dst,exist_ok=True)
for f in os.listdir(dst): os.remove(os.path.join(dst,f))
files=sorted(os.listdir(src))
keep=[f for f in files if int(os.path.splitext(f)[0])<=4]
move=[f for f in files if int(os.path.splitext(f)[0])>4]
for i,f in enumerate(move,1):
    ext=os.path.splitext(f)[1]; nf="%02d%s"%(i,ext)
    shutil.move(os.path.join(src,f), os.path.join(dst,nf))
gi=json.load(io.open(os.path.join(G,"index.json"),encoding="utf-8"))
gi["chars"]["䖒"]={"doc":"卷八 虎","files":["䖒/"+f for f in sorted(keep)]}
gi["chars"]["戲"]={"doc":"卷八 虎","files":["戲/"+f for f in sorted(os.listdir(dst))]}
json.dump(gi,io.open(os.path.join(G,"index.json"),"w",encoding="utf-8"),ensure_ascii=False)
print("䖒",len(keep),"戲",len(os.listdir(dst)))