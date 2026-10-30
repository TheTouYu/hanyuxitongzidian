# -*- coding: utf-8 -*-
import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
for ch in ("𢼗","𤵫","𦊎"):
    p=rf"{C}\{ch}.json"; d=json.load(io.open(p,encoding="utf-8"))
    for s in d["sections"]:
        if s["key"]=="ezhi": s["text"]="③形近字“赤、余、不、木”之訛"
    json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("仅留原文组名")