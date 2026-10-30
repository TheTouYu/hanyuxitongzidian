# -*- coding: utf-8 -*-
import os,json,io,glob,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
B=re.compile(r"^(?:[^a-zA-Z「]*?)?(?:[一-龥]{1,3}母)?[^a-zA-Z]{0,12}?([a-z]{1,2})\s*(?:[/／]\s*[a-z]{1,2})?\s*[，,]\s*[「\"]?(.+?)[」\"]?\s*取\s*[「\"](.+?)[」\"]\s*(?:一面)?\s*[：:]\s*(.*)$",re.S)
n=0; left=[]
for p in glob.glob(os.path.join(C,"*.json")):
    b=os.path.basename(p)
    if b=="index.json": continue
    d=json.load(io.open(p,encoding="utf-8")); ch=d.get("char") or b[:-5]
    if len(ch)>1: continue
    chg=False
    for s in d.get("sections",[]):
        if s.get("key")!="shengmu": continue
        t=(s.get("text") or "").strip()
        if not t or t.startswith("零聲母") or t.startswith("零声母"): continue
        if re.match(r"^[a-z]{1,2}「.+?」取「.+?」：",t): continue
        m=B.match(t)
        if m and m.group(2) and m.group(3):
            s["text"]=f"{m.group(1)}「{m.group(2).strip('「」')}」取「{m.group(3)}」：{m.group(4).strip()}"; chg=True
        else:
            left.append(ch)
    if chg:
        json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("三遍规范",n,"剩余",len(left))
json.dump(left,io.open(r"D:\系统汉字\.tmp-left.json","w",encoding="utf-8"),ensure_ascii=False)