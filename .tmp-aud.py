import json,sys,os
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
cands="发斗谷干后里台系蒙云复只冲征松钟蜡适板范姜"
for ch in cands:
    p=os.path.join(C,ch+".json")
    if not os.path.exists(p):
        print(ch,"—","无卡"); continue
    d=json.load(open(p,encoding="utf-8"))
    b=(d.get("bus") or [{}])[0]; b=b if isinstance(b,dict) else {"name":b}
    t=""
    for s in d.get("sections",[]):
        if isinstance(s,dict) and s.get("text"): t=s["text"][:34]; break
    print(f'{ch} | {d.get("pinyin","")} | 第{b.get("num","?")}部{b.get("name","")} | lv{d.get("level",0)} | {t}')