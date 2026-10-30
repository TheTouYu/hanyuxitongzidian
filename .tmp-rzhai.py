# -*- coding: utf-8 -*-
import json,io,os,shutil,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
P=r"D:\系统汉字\web\public\glyphs\photos"
d=os.path.join(P,"宅")
if os.path.isdir(d): shutil.rmtree(d)
for name,key in (("index.json","photos"),("captions.json","captions")):
    p=os.path.join(P,name); x=json.load(io.open(p,encoding="utf-8")); m=x.get(key) or x
    m.pop("宅",None); json.dump({key:m},io.open(p,"w",encoding="utf-8"),ensure_ascii=False)
pj=r"D:\系统汉字\web\public\photos.js"; s=io.open(pj,encoding="utf-8").read()
s2=re.sub(r'"宅":\s*\[[^\]]*\]\s*,?',"",s)
open(pj,"w",encoding="utf-8",newline="\n").write(s2)
print("removed",s!=s2)