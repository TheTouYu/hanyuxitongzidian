# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
G={"c":"刺持","ch":"刺持","z":"凿总","zh":"凿总","j":"聚决","q":"亲缺","x":"续消","s":"失收","sh":"失收",
   "t":"涂突","h":"豁活","l":"拢离","m":"蒙末","b":"闭剥","p":"拼辟","f":"附分","d":"囤动","n":"纳弄","r":"柔锐","k":"口控","g":"隔估","y":"零声母","w":"零声母"}
n=0
for fn in os.listdir(C):
    if not fn.endswith(".json") or fn=="index.json": continue
    p=os.path.join(C,fn); d=json.load(io.open(p,encoding="utf-8"))
    if d.get("parent")!="次" and d.get("char")!="次": continue
    for s in d["sections"]:
        if s["key"]!="shengmu": continue
        t=s["text"]; m=re.match(r"^([a-zA-Z]{1,2})(取|「)",t)
        if not m: continue
        letter=m.group(1).lower()
        if letter=="y":
            s["text"]="y「零声母」不系：零聲母，緒論七組未列（照實）。"
        else:
            s["text"]=f"{letter}「{G.get(letter,'凿总')}」取「{『' if False else '』'}" if False else f"{letter}「{G.get(letter,'凿总')}」"+t[len(letter):]
        n+=1
    json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("fixed",n)