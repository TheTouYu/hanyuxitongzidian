# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
D=r"D:\系统汉字\web\public\cards"; M="①②③④⑤⑥⑦⑧⑨⑩"
n=0; files=0
for fn in sorted(os.listdir(D)):
    if not fn.endswith(".json") or fn in ("index.json","variants.json"): continue
    p=os.path.join(D,fn)
    try: d=json.load(io.open(p,encoding="utf-8"))
    except Exception: continue
    ch=False
    for s in d.get("sections") or []:
        gs=s.get("groups") or []
        for i,g in enumerate(gs):
            if g.get("no"): continue
            t=(g.get("title") or g.get("label") or "").strip()
            if not t or re.match(r"^[①②③④⑤⑥⑦⑧⑨⑩]", t): continue
            g["no"]=M[i] if i<len(M) else "(%d)"%(i+1); ch=True; n+=1
    if ch: json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); files+=1
print("added_no",n,"files",files)
# patch renderers
for path,old,new in (
 (r"D:\系统汉字\web\server.mjs","if (g.title) h+='<p><b>'+ext(g.title)+'</b></p>';","if (g.title) h+='<p><b>'+escH(g.no||'')+ext(g.title)+'</b></p>';"),
 (r"D:\系统汉字\web\public\index.html","${g.title?'<h4>'+esc(g.title)+'</h4>':''}","${g.title?'<h4>'+esc(g.no||'')+esc(g.title)+'</h4>':''}"),
):
    t=io.open(path,encoding="utf-8").read()
    if old in t: io.open(path,"w",encoding="utf-8",newline="\n").write(t.replace(old,new,1)); print("patched",path)
    else: print("MISS",path)