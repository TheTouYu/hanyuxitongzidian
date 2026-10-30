# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
raw=open(r"D:\字谱智能体\汉字简体繁体对照表大全资料.doc","rb").read()
txt=raw.decode("utf-16-le","ignore")
i=txt.find("繁简汉字对照表")
seg=txt[i:i+200000] if i>=0 else txt
pairs={}
for m in re.finditer(r"([\u3400-\u9fff\U00020000-\U0002A6DF])([\u3400-\u9fff\U00020000-\U0002A6DF])",seg):
    a,b=m.group(1),m.group(2)
    if a==b: continue
    if a not in pairs: pairs[a]=b
print("解析对",len(pairs))
V=r"D:\系统汉字\web\public\variants.json"
v=json.load(io.open(V,encoding="utf-8")); before=len(v)
for k,val in pairs.items(): v.setdefault(k,val)
json.dump(v,io.open(V,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("variants",before,"→",len(v))