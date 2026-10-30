# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
BU={"递":"辵","娣":"女","睇":"目","悌":"心","銻":"金","梯":"木","鬀":"髟","涕":"水","綈":"糸","𧋘":"虫","鮷":"魚","蕛":"艸","豑":"豊","第":"竹","祶":"示","焍":"火","俤":"人","珶":"玉","𦯔":"艸","䑯":"舟","挮":"手","罤":"网","䬾":"食","鵜":"鳥"}
p=os.path.join(C,"弟.json"); d=json.load(io.open(p,encoding="utf-8"))
n=0
for s in d["sections"]:
    for g in s.get("groups",[]) or []:
        for r in g.get("rows",[]) or []:
            c=LAT=None
            c=r[0]
            if c in BU and (len(r)<3 or not r[2]):
                r[2]=BU[c]; n+=1
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("类属补",n)