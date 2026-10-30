# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
cjk=re.compile(r"[\u3400-\u9fff\U00020000-\U0002FA1F]")
lat=re.compile(r"[a-zA-Zāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜü]+")
n=0;fix=0
for fn in os.listdir(C):
    if not fn.endswith(".json") or fn=="index.json": continue
    p=os.path.join(C,fn); d=json.load(io.open(p,encoding="utf-8")); dirty=False
    for s in d.get("sections") or []:
        for g in (s.get("groups") or []):
            for r in g.get("rows") or []:
                if not r: continue
                old=r[0]
                letters="".join(cjk.findall(str(old)))
                if letters and letters!=old:
                    r[0]=letters; dirty=True
                if len(r)>1:
                    oldp=r[1]; ps="".join(lat.findall(str(oldp))) or oldp
                    if ps!=oldp: r[1]=ps; dirty=True
    if dirty:
        json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); fix+=1
print("修表行",fix)