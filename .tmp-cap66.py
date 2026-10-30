# -*- coding: utf-8 -*-
import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\cards\家.json"; d=json.load(io.open(p,encoding="utf-8"))
rows=[
["𢜿","jià","心","《集韻》：「居迓切，音嫁。心不安也。」若有所失之意。"],
["嫁","jià","女","《說文》：「女適人也。从女家聲。古訝切。」女子結婚；出嫁。《廣韻》：「家也。故婦人謂嫁曰歸。」《爾雅》：「往也。」《正字通》：「推惡于人曰嫁。」"],
["稼","jià","禾","《說文》：「禾之秀實為稼，莖節為禾。从禾家聲。一曰稼，家事也。一曰在野曰稼。古訝切。」禾抽穗的樣子。種植五穀，即移栽之意。田中的作物。"],
["幏","jià","巾","《說文》：「南郡蠻夷賨布。从巾家聲。古訝切。」充當賦稅的布匹。"],
["榢（架枷）","jià","木","《集韻》：「《博雅》：杙也，所以舉物也。或作榢、架。亦書作枷。」"],
["傢","xiàng、jiā","人","《漢典》：「（一）xiàng同『像』。《龍龕·人部》：『傢，舊藏作像。』（二）jiā[傢夥]也作『傢伙』。1、器具；用具。2、指牲畜或人（帶輕視或玩笑意）。」"]]
for s in d["sections"]:
    if s["key"]=="zizu": s["groups"][0]["rows"]=rows
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("verbatim only")