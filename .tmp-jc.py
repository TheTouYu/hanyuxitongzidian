# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
d=json.load(io.open(C+"\\斤.json",encoding="utf-8"))
z=[s for s in d["sections"] if s["key"]=="zizu"][0]
G={"b":"闭剥","p":"拼辟","f":"附分","m":"蒙末","d":"囤动","t":"涂突","n":"纳弄","r":"柔锐","l":"拢离","g":"隔估","k":"口控","h":"豁活","j":"聚决","q":"亲缺","x":"续消","z":"凿总","c":"刺持","s":"失收","zh":"凿总","ch":"刺持","sh":"失收"}
def ini(py):
    py=(py or "").lower()
    for k in ("zh","ch","sh"):
        if py.startswith(k): return k
    return py[:1] if py else ""
made=0;chars=[]
for g in z["groups"]:
    for r in g["rows"]:
        ch=r[0]; chars.append(ch)
        p=os.path.join(C,ch+".json")
        if os.path.exists(p): continue
        i=ini(r[1]); nm=G.get(i,"")
        sm=f"{i}「{nm}」取面隨文（推）。" if nm else f"{i}「零聲母」不系（照實）。"
        card={"char":ch,"head":ch,"pinyin":r[1],"bus":{"num":44,"name":"斤"},"parent":"斤","level":3,"aliases":[],
              "sections":[{"key":"shiyi","label":"释义","text":r[3],"cites":[]},{"key":"shengmu","label":"声母拟态","text":sm,"cites":[]},
                          {"key":"suoshujuan","label":"所属卷","text":"","links":[{"ch":"卷七斤","label":"卷七 斤"}]}]}
        json.dump(card,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); made+=1
print("chars",len(chars),"new",made)
print("".join(chars))