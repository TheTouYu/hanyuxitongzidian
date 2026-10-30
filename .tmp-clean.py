# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
pat=re.compile(r"^【[^】]{0,30}(?:部部首字|部首字|級字根|级字根)[^】]{0,20}】\s*")
n=0; files=0
for f in os.listdir(C):
    if not f.endswith(".json") or f in ("index.json","variants.json","captions.json"): continue
    p=os.path.join(C,f); d=json.load(io.open(p,encoding="utf-8")); ch=False
    for s in d.get("sections",[]):
        t=s.get("text") or ""
        t2=pat.sub("",t)
        if t2!=t: s["text"]=t2; ch=True; n+=1
    if ch:
        json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); files+=1
print("cleaned sections",n,"files",files)