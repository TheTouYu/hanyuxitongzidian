# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
pat=re.compile(r"^[\u3400-\u9fff\U00020000-\U0002FA1F]+[^\sa-zA-Z]*([a-zA-Zāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜü]{2,})")
n=0
for fn in os.listdir(C):
    if not fn.endswith(".json") or fn=="index.json": continue
    p=os.path.join(C,fn); d=json.load(io.open(p,encoding="utf-8")); dirty=False
    for s in d.get("sections") or []:
        for g in (s.get("groups") or []):
            for r in g.get("rows") or []:
                if len(r)<4: continue
                m=pat.match(r[3] or "")
                if m and m.group(1)!=r[1]:
                    r[1]=m.group(1); dirty=True
    if dirty:
        json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("修拼音",n)