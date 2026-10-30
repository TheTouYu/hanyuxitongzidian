# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
PY={"递":"dì","娣":"dì","睇":"dì","悌":"tì","銻":"tí","梯":"tī","鬀":"tì","涕":"tì","綈":"tí","𧋘":"tí","鮷":"tí","蕛":"tí","豑":"zhì","第":"dì","祶":"dì","焍":"dì","俤":"dì","珶":"dì","𦯔":"tí","䑯":"dì","挮":"tǐ","罤":"tí","䬾":"tí","鵜":"tí"}
BU={"递":"辵","娣":"女","睇":"目","悌":"心","銻":"金","梯":"木","鬀":"髟","涕":"水","綈":"糸","𧋘":"虫","鮷":"魚","蕛":"艸","豑":"豊","第":"竹","祶":"示","焍":"火","俤":"人","珶":"玉","𦯔":"艸","䑯":"舟","挮":"手","罤":"网","䬾":"食","鵜":"鳥"}
p=os.path.join(C,"弟.json"); d=json.load(io.open(p,encoding="utf-8")); n=0
for s in d["sections"]:
    for g in s.get("groups",[]) or []:
        for r in g.get("rows",[]) or []:
            bare=re.sub(r"（.*?）","",r[0])
            r[1]=PY.get(bare,r[1]); r[2]=BU.get(bare,r[2] or ""); r[3]=re.sub(r"^["r"a-zA-Zāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜü]+","",r[3] if len(r)>3 else "")
            n+=1
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("rows",n,[ (r[0],r[1],r[2]) for s in d["sections"] for g in (s.get("groups") or []) for r in g["rows"]][:6])