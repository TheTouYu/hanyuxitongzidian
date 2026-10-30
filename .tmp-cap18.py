# -*- coding: utf-8 -*-
import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
fix={"𧧘":("兌","說字之訛；說从言兌聲，字根為「兌」"),
     "栬":("巵","疑為梔字之訛；梔从木巵聲，字根為「巵」"),
     "𨋭":("包","王念孫謂軳之譌；軳从車包聲，字根為「包」"),
     "𡜆":("危","㛂字之譌；㛂从女危聲，字根為「危」"),
     "脃":("危","形近危之訛；正字从肉絕省，訛从危形")}
for ch,(par,note) in fix.items():
    p=rf"{C}\{ch}.json"; d=json.load(io.open(p,encoding="utf-8"))
    d["parent"]=par
    for s in d["sections"]:
        if s.get("key")=="bianzheng": s["text"]=note
    json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("fixed",len(fix))