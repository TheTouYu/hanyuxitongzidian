# -*- coding: utf-8 -*-
import json,io,os,sys,glob,re,html
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
SRC=r"web\public\cards"; OUT=os.path.join(SRC,"html")
miss=set()
for f in glob.glob(os.path.join(OUT,"*.html")):
    if "此字暂无独立词条页" in io.open(f,encoding="utf-8").read(): miss.add(os.path.basename(f)[:-5])
red={}
for fp in glob.glob(os.path.join(SRC,"*.json")):
    b=os.path.basename(fp)
    if b in ("index.json","variants.json","captions.json"): continue
    try: d=json.load(io.open(fp,encoding="utf-8"))
    except Exception: continue
    for s in d.get("sections",[]):
        for g in (s.get("groups") or []):
            for r in (g.get("rows") or []):
                if not r: continue
                t=str(r[0]); m=re.match(r"^([^\s（(]+)\s*[（(](.*?)[）)]",t)
                if not m: continue
                head=m.group(1); ps=[x for x in re.findall(r"[^\s、,，]",m.group(2))]
                ok=lambda c: os.path.exists(os.path.join(OUT,c+".html"))
                if head in miss:
                    for p in ps:
                        if ok(p): red[head]=p; break
                for p in ps:
                    if p in miss and ok(head): red.setdefault(p,head)
n=0
for c,t in red.items():
    s='<!doctype html><meta charset="utf-8"><meta http-equiv="refresh" content="0;url=/cards/html/'+t+'.html">'
    s+='<a href="/cards/html/'+t+'.html">'+html.escape(c)+' → '+html.escape(t)+'</a>'
    io.open(os.path.join(OUT,c+".html"),"w",encoding="utf-8").write(s); n+=1
print("miss",len(miss),"redirect",n)