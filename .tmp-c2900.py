# -*- coding: utf-8 -*-
import json,io,os,shutil,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
P=r"D:\系统汉字\web\public\glyphs"
src=os.path.join(P,"叔"); fs=sorted(os.listdir(src))
m={"10":["婌"],"11":["惄"],"12":["惄"],"13":["惄"],"14":["督"],"15":["督"],"16":["錖"]}
gi=json.load(io.open(os.path.join(P,"index.json"),encoding="utf-8")); ch=gi.get("chars") or gi
moved={}
for f in fs:
    num=f[:2]
    if num not in m: continue
    tgt=m[num][0]; D=os.path.join(P,tgt); os.makedirs(D,exist_ok=True)
    n=len(os.listdir(D))+1; ext=os.path.splitext(f)[1]
    shutil.move(os.path.join(src,f),os.path.join(D,f"{n:02d}{ext}"))
    moved.setdefault(tgt,[]).append(f"{n:02d}{ext}")
for tgt,files in moved.items():
    ch[tgt]={"doc":"卷四  弋.docx","files":[f"{tgt}/{x}" for x in sorted(files)],"variants":""}
left=sorted(os.listdir(src))
ch["叔"]={"doc":"卷四  弋.docx","files":[f"叔/{f}" for f in left],"variants":""}
json.dump({"chars":ch},io.open(os.path.join(P,"index.json"),"w",encoding="utf-8"),ensure_ascii=False)
print("叔余",len(left),"分出",{k:len(v) for k,v in moved.items()})