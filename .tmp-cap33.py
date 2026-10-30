# -*- coding: utf-8 -*-
import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
m={"𧧘":"《正字通》：「說字之訛。」所訛之字為「說」（从言兌聲，字根「兌」）。",
   "𨋭":"《正字通》：「譌字。」王念孫疏證：「軳（páo）……各本軳譌作𨋭。」所訛之字為「軳」（从車包聲，字根「包」）。"}
for ch,txt in m.items():
    p=rf"{C}\{ch}.json"; d=json.load(io.open(p,encoding="utf-8"))
    d["parent"]=""
    for s in d["sections"]:
        if s.get("key")=="bianzheng": s["text"]=txt
    json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("ok")