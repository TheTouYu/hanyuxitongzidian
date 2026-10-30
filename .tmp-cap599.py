# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
n=0
for f in os.listdir(C):
    if not f.endswith(".json") or f=="index.json": continue
    p=os.path.join(C,f)
    try: d=json.load(io.open(p,encoding="utf-8"))
    except Exception: continue
    if not isinstance(d,dict): continue
    ch=d.get("char","")
    for s in d.get("sections",[]):
        if not isinstance(s,dict) or s.get("key")!="shengmu": continue
        t=s.get("text","")
        m=re.match(r"^([a-z]{1,2})「(.+?)」取「(.)」[：:](?:\1（今讀[^）]*）)?\1「.+?」取「.」[：:](.+)$",t)
        if m:
            s["text"]=f"{m.group(1)}「{m.group(2)}」取「{m.group(3)}」：{m.group(4)}"; n+=1
    json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("去重复前缀",n)