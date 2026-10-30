# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
n=0; ex=[]
for f in os.listdir(C):
    if not f.endswith(".json") or f=="index.json": continue
    p=os.path.join(C,f)
    try: d=json.load(io.open(p,encoding="utf-8"))
    except Exception: continue
    if not isinstance(d,dict): continue
    for s in d.get("sections",[]):
        if not isinstance(s,dict) or s.get("key")!="shengmu": continue
        t=s.get("text","")
        if t.count("取「")>=2 and "：" in t:
            m=re.match(r"^([a-z]{1,2})「([^」]+)」取「(.)」",t)
            tail=t.rsplit("：",1)[-1].strip()
            if m and tail and len(tail)>2 and not re.match(r"^([a-z]{1,2})「",tail):
                s["text"]=f"{m.group(1)}「{m.group(2)}」取「{m.group(3)}」：{tail}"; n+=1
                if len(ex)<3: ex.append((d.get("char"),s["text"]))
    json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("修复",n); [print(x) for x in ex]