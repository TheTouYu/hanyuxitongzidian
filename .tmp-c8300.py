# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
PY={"递":"dì","娣":"dì","睇":"dì","悌":"tì","銻":"tí","梯":"tī","鬀":"tì","涕":"tì","綈":"tí","𧋘":"tí","鮷":"tí","蕛":"tí","豑":"zhì","第":"dì","祶":"dì","焍":"dì","俤":"dì","珶":"dì","𦯔":"tí","䑯":"dì","挮":"tǐ","罤":"tí","䬾":"tí","鵜":"tí"}
n=0
for fn in list(os.listdir(C)):
    if not fn.endswith(".json") or fn=="index.json": continue
    p=os.path.join(C,fn); d=json.load(io.open(p,encoding="utf-8"))
    ch=d.get("char") or ""
    if not ch: continue
    if ch in PY: d["pinyin"]=PY[ch]
    want=ch+".json"
    if fn!=want:
        json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
        os.replace(p,os.path.join(C,want)); n+=1
    else:
        json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("renamed",n)