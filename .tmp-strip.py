# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
HEAD=re.compile(r"^[\u3400-\u9fff\U00020000-\U0002A6DF]+(?:（[^）]*）)?\s*[a-zA-Zāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜü、，,\s]*")
for fn in ("厂.json","反.json"):
    p=os.path.join(C,fn); d=json.load(io.open(p,encoding="utf-8"))
    for s in d["sections"]:
        if s.get("key")!="zizu": continue
        for g in s.get("groups",[]):
            for r in g.get("rows",[]):
                r[3]=HEAD.sub("",r[3]).strip()
    json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    print(fn,"ok")