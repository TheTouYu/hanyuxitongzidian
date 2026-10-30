# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
M={"苊":"艸","𧠞":"目","𩒒":"頁","砨":"石","𥑽":"石","豟":"豕","㛂":"女","𠈊":"人","𦛐":"肉",
"駕":"馬","嘉":"壴","枷":"木","痂":"疒","𦙺":"肉","賀":"貝","妿":"女","珈":"玉","鴐":"鳥","跏":"足","笳":"竹","㵑":"水","𧝂":"衣","茄":"艸","䴥":"鹿","𨔣":"辵","迦":"辵","泇":"水","𢉤":"广","架":"木","𧉪":"虫","袈":"衣","伽":"人","鉫":"金",
"䳘":"鳥","餓":"食","哦":"口","誐":"言","𧒎":"虫","莪":"艸","涐":"水","蛾":"虫","峨":"山","硪":"石","娥":"女","騀":"馬","睋":"目","䄉":"示","俄":"人","𩒰":"頁"}
n=0
for name,lei in M.items():
    p=os.path.join(C,name+".json")
    if not os.path.exists(p): continue
    d=json.load(io.open(p,encoding="utf-8")); ch=False
    for s in d.get("sections",[]):
        if s.get("key")=="zizu":
            for g in s.get("groups",[]):
                for r in g["rows"]:
                    if r[0].split("（")[0]==name and not r[2]: r[2]=lei; ch=True
    if ch: json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("cards touched",n)