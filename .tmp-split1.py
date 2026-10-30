# -*- coding: utf-8 -*-
import json,io,os,shutil,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
G=r"D:\系统汉字\web\public\glyphs"
base=os.path.join(G,"彥")
def put(ch, files):
    d=os.path.join(G,ch); os.makedirs(d,exist_ok=True)
    for f in os.listdir(d): os.remove(os.path.join(d,f))
    for i,f in enumerate(files):
        shutil.copyfile(os.path.join(base,f), os.path.join(d,"%02d.png"%(i+1)))
    return ["%s/%02d.png"%(ch,i+1) for i in range(len(files))]
# keep 01-06 for 彥
keep=["01.png","02.png","03.png","04.png","05.png","06.png"]
y=["%s/%s"%(("彥"),f) for f in keep]
for f in os.listdir(base):
    if f not in keep: os.remove(os.path.join(base,f))
yan_files=put("顏",["07.png","08.png"]) if os.path.exists(os.path.join(base,"07.png")) else None
print("check")