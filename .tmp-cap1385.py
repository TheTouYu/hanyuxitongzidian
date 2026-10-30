# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from PIL import Image
G=r"D:\系统汉字\web\public\glyphs"
bad=[]
for root,ds,fs in os.walk(G):
    if "photos" in root.split(os.sep): continue
    for f in fs:
        if not f.lower().endswith((".png",".jpg",".jpeg")): continue
        p=os.path.join(root,f)
        try:
            im=Image.open(p); im.load()
        except Exception as e:
            bad.append((p,type(e).__name__))
print("坏图",len(bad))
for b in bad[:10]: print(b)
if bad:
    for p,_ in bad:
        try: os.remove(p)
        except: pass
    # 清除索引中指向已删文件的条目
    ip=os.path.join(G,"index.json"); d=json.load(io.open(ip,encoding="utf-8")); chars=d.get("chars") or d
    n=0
    for ch,v in list(chars.items()):
        fs=[f for f in (v.get("files") or []) if os.path.exists(os.path.join(G,f))]
        if len(fs)!=len(v.get("files") or []):
            v["files"]=fs; n+=1
        if not fs: chars.pop(ch,None)
    json.dump({"chars":chars},io.open(ip,"w",encoding="utf-8"),ensure_ascii=False); print("索引清理",n)