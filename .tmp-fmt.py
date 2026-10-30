# -*- coding: utf-8 -*-
import json,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
FIX={"旨":{"麂":"𪊨（麂）"},
 "只":{"枳":"枳（䅩）","齞":"齞（𪗛齴）","𧧹":"𧧹（徯蹊𥪦傒）","胑":"胑（肢）"},
 "奚":{"谿":"谿（豀溪）","徯":"徯（蹊傒𥪦）","傒":"傒（𧧹）","縘":"縘（繫）","㨙":"㨙（𢭁）","鞵":"鞵（鞋）","𡰄":"𡰄（𡰖）","雞":"雞（鷄鸡）","𥰥":"𥰥（𦩶）","謑":"謑（䜁）","螇":"螇（𧕉𧋉）","𦫬":"𦫬（䒊）","鸂":"鸂（䳶）","鼷":"鼷"}}
n=0
for name,m in FIX.items():
    p=rf"{C}\{name}.json"; d=json.load(open(p,encoding="utf-8"))
    for s in d["sections"]:
        for g in s.get("groups",[]) or []:
            for r in g["rows"]:
                if r[0] in m and r[0]!=m[r[0]]:
                    r[0]=m[r[0]]; n+=1
    json.dump(d,open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("格式修正",n)