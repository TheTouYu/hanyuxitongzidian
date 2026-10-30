# -*- coding: utf-8 -*-
import os,json,io,glob,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
GRP={"b":"闭剥","p":"拼辟","f":"附分","m":"蒙末","d":"囤动","t":"涂突","n":"纳弄","l":"拢离","r":"柔锐",
     "z":"凿总","zh":"凿总","c":"刺持","ch":"刺持","s":"失收","sh":"失收","j":"聚决","q":"亲缺","x":"续消",
     "g":"隔估","k":"口控","h":"豁活"}
pat=re.compile(r"^([a-z]{1,2})\s*取\s*[「\"]?([^」\"：:，,]{1,4})[」\"]?\s*[：:]\s*(.+)$",re.S)
n=0; bad=[]
for p in glob.glob(os.path.join(C,"*.json")):
    b=os.path.basename(p)
    if b=="index.json": continue
    d=json.load(io.open(p,encoding="utf-8")); ch=d.get("char") or b[:-5]
    if len(ch)>1: continue
    chg=False
    for s in d.get("sections",[]):
        if s.get("key")!="shengmu": continue
        t=(s.get("text") or "").strip()
        if not t or "「" in t and "」取「" in t: continue
        if t.startswith("零聲母") or t.startswith("零声母"): continue
        m=pat.match(t)
        if m:
            ini,face,rest=m.group(1),m.group(2).strip(),m.group(3).strip()
            grp=GRP.get(ini)
            if not grp: bad.append((ch,t[:20])); continue
            s["text"]=f"{ini}「{grp}」取「{face}」：{rest}"; chg=True
        else:
            bad.append((ch,t[:20]))
    if chg:
        json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("规范化",n)
print("未识别样例",bad[:8],"共",len(bad))