# -*- coding: utf-8 -*-
import json,io,sys,os
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
G=r"D:\系统汉字\web\public\glyphs"
p=G+r"\index.json"; ix=json.load(io.open(p,encoding="utf-8"))
e=ix["chars"].get("䒬")
if e:
    e["files"]=[]; e.pop("alias",None); e["note"]="原稿本字无独立字形段；䒬为古文莫字，字形见莫部"
    json.dump(ix,io.open(p,"w",encoding="utf-8"),ensure_ascii=False)
    print("cleared 䒬 glyphs")
C=r"D:\系统汉字\web\public\cards"
q=C+r"\䒬.json"
if os.path.exists(q):
    d=json.load(io.open(q,encoding="utf-8"))
    d.pop("aliases",None); d["head"]="䒬（莫）"
    d["sections"]=[{"key":"shiyi","label":"释义","text":"䒬（莫）mò。《字彙補》：「古文莫字，見古《孝經》。」","cites":[]},
                   {"key":"zigen","label":"字形","text":"原稿本字无独立字形段（僅作為族行「䒬（莫）」出現）；字形見「莫」部。","cites":[]}]
    json.dump(d,io.open(q,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    print("card updated")