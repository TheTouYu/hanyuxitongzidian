# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
q=r"D:\系统汉字\web\public\cards\䒬.json"
if os.path.exists(q):
    d=json.load(io.open(q,encoding="utf-8"))
    d.pop("aliases",None); d["head"]="䒬（莫）"
    d["sections"]=[{"key":"shiyi","label":"释义","text":"䒬（莫）mò。《字彙補》：「古文莫字，見古《孝經》。」","cites":[]},
                   {"key":"zigen","label":"字形","text":"原稿本字无独立字形段（僅見於族行「䒬（莫）」）；字形見「莫」部。","cites":[]}]
    json.dump(d,io.open(q,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    print("card ok")
else: print("no card")