# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
G={"g":"隔估","k":"口控","h":"豁活","j":"聚决","q":"亲缺","x":"续消","b":"闭剥","p":"拼辟","f":"附分","m":"蒙末","d":"囤动","t":"涂突","n":"纳弄","l":"拢离","r":"柔锐","z":"凿总","zh":"凿总","c":"刺持","ch":"刺持","s":"失收","sh":"失收"}
pat=re.compile(r"^([a-zA-Z]{1,2})取「(.?)」")
n=0
for fn in os.listdir(C):
    if not fn.endswith(".json") or fn=="index.json": continue
    p=os.path.join(C,fn); d=json.load(io.open(p,encoding="utf-8")); ch=False
    for s in d.get("sections",[]):
        if s.get("key")!="shengmu": continue
        t=s.get("text","").strip()
        m=pat.match(t)
        if m and not re.match(r"^[a-zA-Z]{1,2}「",t):
            ini=m.group(1).lower(); g=G.get(ini,"零声母")
            s["text"]=f"{m.group(1)}「{g}」取「{m.group(2)}」"+t[m.end():]; ch=True
    if ch: json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("补组名",n)