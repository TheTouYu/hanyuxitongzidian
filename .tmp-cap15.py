# -*- coding: utf-8 -*-
import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\cards\色.json"
d=json.load(io.open(p,encoding="utf-8"))
for s in d["sections"]:
    if s.get("key")=="zizu":
        g=[x for x in s["groups"]]
        g=[x for x in g if not x["title"].startswith("③")]
        g.append({"title":"③形近字「危、巵、兌、包」之訛","note":"","rows":[
         ["脃","cuì","肉","《說文》「小耎易斷也。从肉从絕省」，脆弱；俗作脆（原稿列此组，谓形近危之訛）"],
         ["𡜆","yuē","女","《字彙》「同𡡕」；《玉篇》「𡜴肥皃」，形近包之訛"],
         ["栬","zuì","木","《集韻》「小杙」小木樁；《正字通》疑為「梔」之訛"],
         ["𧧘","shuì","言","《正字通》「說字之訛」"],
         ["𨋭","páo","車","《廣雅》「軫𨋭，轉戾也」；王念孫謂軳之譌"]]})
        s["groups"]=g
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print([x["title"] for x in g],sum(len(x["rows"]) for x in g))