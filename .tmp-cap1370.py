# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
G=r"D:\系统汉字\web\public\glyphs"; C=r"D:\系统汉字\web\public\cards"
p=os.path.join(G,"index.json"); d=json.load(io.open(p,encoding="utf-8")); chars=d.get("chars") or d
n=0
for ch,v in chars.items():
    fs=v.get("files") or []
    for i,f in enumerate(fs):
        if f.lower().endswith((".jpg",".jpeg")):
            cand=os.path.join(G,re.sub(r"\.(jpg|jpeg)$",".png",f,flags=re.I))
            if os.path.exists(cand) and not os.path.exists(os.path.join(G,f)):
                fs[i]=re.sub(r"\.(jpg|jpeg)$",".png",f,flags=re.I); n+=1
json.dump({"chars":chars},io.open(p,"w",encoding="utf-8"),ensure_ascii=False)
print("index 路径改",n)
m=0
for fn in os.listdir(C):
    if not fn.endswith(".json") or fn=="index.json": continue
    fp=os.path.join(C,fn); cd=json.load(io.open(fp,encoding="utf-8")); txt_flag=False
    for s in cd.get("sections",[]):
        t=s.get("text","")
        def rep(mm):
            global m
            rel=mm.group(1)
            cand=os.path.join(G,re.sub(r"\.(jpg|jpeg)$",".png",rel,flags=re.I))
            if os.path.exists(cand) and not os.path.exists(os.path.join(G,rel)):
                m+=1; return mm.group(0).replace(rel,re.sub(r"\.(jpg|jpeg)$",".png",rel,flags=re.I))
            return mm.group(0)
        if "glyphs/" in t:
            nt=re.sub(r'glyphs/([^"\s]+\.(?:jpg|jpeg|png))',rep,t)
            if nt!=t: s["text"]=nt; txt_flag=True
    if txt_flag: json.dump(cd,io.open(fp,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("卡片引用改",m)