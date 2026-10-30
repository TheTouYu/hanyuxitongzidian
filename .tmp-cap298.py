# -*- coding: utf-8 -*-
import os,json,io,glob,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
GRP={"b":("闭","剥"),"p":("拼","辟"),"f":("附","分"),"m":("蒙","末"),"d":("囤","动"),"t":("涂","突"),
     "n":("纳","弄"),"l":("拢","离"),"r":("柔","锐"),"z":("凿","总"),"zh":("凿","总"),"c":("刺","持"),
     "ch":("刺","持"),"s":("失","收"),"sh":("失","收"),"j":("聚","决"),"q":("亲","缺"),"x":("续","消"),
     "g":("隔","估"),"k":("口","控"),"h":("豁","活")}
def ini(py):
    py=(py or "").strip().lower()
    m=re.match(r"([a-zāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜü]+)",py)
    if not m: return None
    s=m.group(1)
    for two in ("zh","ch","sh"):
        if s.startswith(two): return two
    return s[0]
T=re.compile(r"^今[讀读]\s*\S*?\s*[：:]\s*按[聲声]母取[緒绪]論擬態[義义]一面")
n=0; manual=[]
for p in glob.glob(os.path.join(C,"*.json")):
    b=os.path.basename(p)
    if b=="index.json": continue
    d=json.load(io.open(p,encoding="utf-8")); ch=d.get("char") or b[:-5]
    if len(ch)>1: continue
    i=ini(d.get("pinyin")); by=""
    for s in d.get("sections",[]):
        if s.get("key") in ("benyi","bengen","shiyi") and (s.get("text") or ""):
            by=s["text"]; break
    chg=False
    for s in d.get("sections",[]):
        if s.get("key")!="shengmu": continue
        t=(s.get("text") or "").strip()
        if not t: continue
        if t.startswith("零聲母") or t.startswith("零声母"): continue
        if re.match(r"^[a-z]{1,2}「.+?」取「.+?」：",t): continue
        if not T.match(t): manual.append(ch); continue
        if i not in GRP: manual.append(ch); continue
        f1,f2=GRP[i]
        pick=f1 if f1 in by else (f2 if f2 in by else f1)
        head=re.split(r"[。；\n]",by)[0][:40]
        s["text"]=f"{i}「{f1}{f2}」取「{pick}」：{head}，取{pick}一面（推）。"; chg=True
    if chg:
        json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("模板改写",n,"需人工",len(manual))
json.dump(manual,io.open(r"D:\系统汉字\.tmp-manual.json","w",encoding="utf-8"),ensure_ascii=False)