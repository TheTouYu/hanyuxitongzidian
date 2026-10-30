# -*- coding: utf-8 -*-
import os,json,io,glob,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
def ini(py):
    py=(py or "").strip().lower()
    m=re.match(r"([a-zāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜü]+)",py)
    if not m: return None
    s=m.group(1)
    for two in ("zh","ch","sh"):
        if s.startswith(two): return two
    return s[0]
n=0; tmpl=[]
for p in glob.glob(os.path.join(C,"*.json")):
    b=os.path.basename(p)
    if b=="index.json": continue
    d=json.load(io.open(p,encoding="utf-8")); ch=d.get("char") or b[:-5]
    if len(ch)>1: continue
    i=ini(d.get("pinyin")); chg=False
    for s in d.get("sections",[]):
        if s.get("key")!="shengmu": continue
        t=(s.get("text") or "").strip()
        if not t: continue
        if i in ("y","w"):
            new="零聲母（今讀 %s），绪论七组未列，不系（照實）。"%(d.get("pinyin") or "")
            if t!=new: s["text"]=new; chg=True
        elif "今讀" in t and "按聲母取緒論擬態義一面" in t:
            tmpl.append(ch)
    if chg:
        json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("y/w 归零声母",n,"模板残句",len(tmpl))
json.dump(tmpl,io.open(r"D:\系统汉字\.tmp-tmpl.json","w",encoding="utf-8"),ensure_ascii=False)