# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
HAN=re.compile(r"^([\u3400-\u9fff\U00020000-\U0002A6DF]+)")
PY={"販":"fàn","版":"bǎn","厓":"yá","崖":"yá","涯":"yá","睚":"yá","屵":"è","娾":"ǎi","厊":"yǎ","广":"yǎn","𠆲":"yǎn","𢇘":"yǎn","㚧":"yǎn","𢞞":"hàn","㷳":"yàn","贗":"yàn","鴈":"yàn"}
for fn in ("厂.json","反.json"):
    p=os.path.join(C,fn); d=json.load(io.open(p,encoding="utf-8"))
    for s in d["sections"]:
        if s.get("key")!="zizu": continue
        for g in s.get("groups",[]):
            for r in g.get("rows",[]):
                t=r[3]; m=HAN.match(t)
                if m: r[0]=m.group(1)
                if r[0] in PY: r[1]=PY[r[0]]
    json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("ok")