# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
names=["知","智","疾","医","至","到","臺","彘"]
sec={"key":"erji","label":"本部二级字根","text":"矢部的二级字根共八个：知、智、疾、医、至、到、臺、彘（本字「知」为其中之一，其下另分報靶往返、靶中矢狀多毛、形近訛字三组）。","cites":[],
     "links":[{"ch":n,"label":n} for n in names]}
for ch in ("知","矢"):
    p=os.path.join(C,ch+".json"); d=json.load(io.open(p,encoding="utf-8"))
    ss=d["sections"]; done=False
    for i,s in enumerate(ss):
        if s.get("key")=="erji": ss[i]=dict(sec); done=True
    if not done: ss.insert(-1,dict(sec))
    json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("ok")