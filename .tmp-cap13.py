# -*- coding: utf-8 -*-
import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\cards\色.json"
d=json.load(io.open(p,encoding="utf-8"))
g=[{"title":"①指顏色，表示臉色、水色、美色等","note":"","rows":[
 ["赩","xì","赤","《新附》「大赤也。从赤、色，色亦聲」；大紅色"],
 ["𨠶","yí","酉","《集韻》「酡，飲而赭色著面」；飲酒臉紅"],
 ["𢙚","xī","心","《龍龕》「欺慢之皃」；輕慢之態"],
 ["艷","yàn","豐","《說文》「好而長也」；色彩鮮明、美豔"],
 ["灔","yàn","水","《集韻》「瀲灩，水滿皃」；水光閃動"],
 ["𨛉","jì","邑","《奚韻》「山名」；地名"]]},
 {"title":"②音譯字","note":"","rows":[["銫","sè","金","化學元素 cesium 的音譯；从金色聲，聲旁只記音"]]}]
for s in d["sections"]:
    if s.get("key")=="zizu":
        s["text"]=""; s["groups"]=g
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("ok",sum(len(x["rows"]) for x in g))