# -*- coding: utf-8 -*-
import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
YZ={"𧧘":'《正字通》：「說字之訛。」',
     "栬":'《正字通》：「俗字。小杙不名栬。」疑為「梔」字之訛。',
     "𨋭":'《正字通》：「譌字。」王念孫疏證：「軳（páo），曹憲音牛力反。各本軳譌作𨋭，自宋時本已然。」',
     "𡜆":'《正字通》：「㛂字之譌。」',
     "脃":'原稿列於「形近字『危、巵、兌、包』之訛」一組（脃條正文無訛字語）。'}
for ch,txt in YZ.items():
    p=rf"{C}\{ch}.json"; d=json.load(io.open(p,encoding="utf-8"))
    d["sections"]=[s for s in d["sections"] if s.get("key")!="shengmu"]
    for s in d["sections"]:
        if s.get("key")=="bianzheng": s["text"]=txt
    json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("ok")