# -*- coding: utf-8 -*-
import json,io,glob,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
MAP={"benyi":("本義","本义"),"zhuanyi":("轉義","转义"),"bianzheng":("辯證","辩证"),
     "yinyuan":("音源",),"zizu":("字族衍義","字族衍义")}
n=0
for p in glob.glob(os.path.join(C,"*.json")):
    if p.endswith("index.json"): continue
    try: d=json.load(io.open(p,encoding="utf-8"))
    except Exception: continue
    if not isinstance(d,dict) or "sections" not in d: continue
    hit=False
    for s in d["sections"]:
        k=s.get("key"); t=s.get("text") or ""
        if not t: continue
        labs=[]
        if k in MAP: labs=list(MAP[k]) if k!="zizu" else ["字族衍義","字族衍义"]
        for L in labs:
            m=re.match(r"^\s*"+re.escape(L)+r"\s*[：:]\s*",t)
            if m:
                s["text"]=t[m.end():].lstrip(); hit=True; break
    if hit:
        json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("去重复标题",n)