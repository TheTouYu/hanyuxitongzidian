# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
p=rf"{C}\貍.json"; d=json.load(io.open(p,encoding="utf-8"))
d["pinyin"]="lí（又 mái、yù）"
for s in d["sections"]:
    if s["key"]=="zhuanyi":
        s["text"]="因狸喜歡將獵物埋藏于土中，故引申指埋藏（mái，《集韻》：「薶，《說文》：『瘞也。』或作貍、埋。」）；或引申指腐臭（yù，《集韻》：「臭也。《周禮》：『鳥皫色而沙鳴、貍』」）。"
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
for f in ("狸.json",):
    q=rf"{C}\{f}"
    if os.path.exists(q):
        x=json.load(io.open(q,encoding="utf-8"))
        if x.get("char")=="貍" or x.get("char")=="狸": os.remove(q); print("removed",f)
print("三读已补")