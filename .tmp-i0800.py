# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
IMG=re.compile(r'<img\s+class="gin"\s+src="glyphs/(?:inline/)?([^/"]+)/([^"]+)"[^>]*>')
n=0; caps=0
for fn in sorted(os.listdir(C)):
    if not fn.endswith(".json") or fn in ("index.json","variants.json"): continue
    p=os.path.join(C,fn); d=json.load(io.open(p,encoding="utf-8")); ch=d.get("char") or fn[:-5]; chg=False
    for s in d.get("sections",[]):
        t=s.get("text") or ""
        if not t: continue
        t2=IMG.sub(lambda m:"{{%s/%s}}"%(m.group(2).split("/",1)[-1] if "/" in m.group(2) else m.group(2), m.group(2)), t)
        # 更稳妥：直接重建占位 {{<sec>/<file>}}
        def rep(m):
            return "{{%s/%s}}"%(m.group(2).split("/")[-2] if m.group(2).count("/")>=2 else s.get("key","benyi"), m.group(2).split("/")[-1])
        t2=IMG.sub(rep, t)
        if "{{" in t2 and "inline" in t:
            s["gdir"]="inline/"+ch
        lines=[ln for ln in t2.split("\n") if not ln.lstrip().startswith("▲")]
        if len(lines)!=len(t2.split("\n")): caps+=1
        t2="\n".join(lines)
        if t2!=t: s["text"]=t2; chg=True
    if chg:
        json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("fixed cards",n,"stripped captions",caps)
d=json.load(io.open(os.path.join(C,"弔.json"),encoding="utf-8"))
for s in d["sections"]:
    if s.get("gdir"): print("弔 gdir",s["key"],s["gdir"], s["text"][:120])