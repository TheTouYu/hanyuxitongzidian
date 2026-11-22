# -*- coding: utf-8 -*-
"""重建 web/public/cards/index.json（不移动文件）。"""
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
C=os.path.join(ROOT,"web","public","cards")
variants={}
vp=os.path.join(C,"variants.json")
if os.path.exists(vp): variants=json.load(io.open(vp,encoding="utf-8"))
rev={}
for simp,tr in variants.items():
    for t in (tr if isinstance(tr,list) else [tr]): rev.setdefault(t,[]).append(simp)
rows=[]
for fn in sorted(os.listdir(C)):
    if not fn.endswith(".json") or fn in ("index.json","variants.json"): continue
    try: d=json.load(io.open(os.path.join(C,fn),encoding="utf-8"))
    except Exception: continue
    if not isinstance(d,dict): continue
    c=d.get("char") or fn[:-5]; bus=d.get("bus") or {}
    b=bus.get("num") if isinstance(bus,dict) else (bus[0] if isinstance(bus,list) and bus else None)
    n=bus.get("name") if isinstance(bus,dict) else ""
    rows.append({"cc":d.get("cc",""),"cn":d.get("cn",""),
        "h":d.get("head") or c,"c":c,"a":d["aliasIndex"] if "aliasIndex" in d else (d.get("aliases") or []),"p":d.get("pinyin") or "",
        "t":[s.get("label","") for s in d.get("sections",[])],
        "b":b,"n":n or "","lv":d.get("level") or 3,"rl":d.get("rootLevel") or 0,
        "pr":d.get("parent") or "","rc":d.get("rootChain") or [],"rlb":d.get("rootLabel") or "","rc2":d.get("rootChain2") or [],"v":rev.get(c,[])})
# 或体路由指定（主人 2026-11-22 定）：或体在本部已有正字卡时，让路线落到正字卡，
# 不让旧落点按文件名序先占。只修 index 的别名数组与 alias-index.json，不动卡。
ALIAS_PIN={"賓":"𡪛","昰":"是","芦":"蘆"}
for r in rows:
    if not isinstance(r.get("a"),list): continue
    r["a"]=[a for a in r["a"] if not (a in ALIAS_PIN and ALIAS_PIN[a]!=r["c"] and os.path.exists(os.path.join(C,ALIAS_PIN[a]+".json")))]
json.dump(rows,io.open(os.path.join(C,"index.json"),"w",encoding="utf-8"),ensure_ascii=False,separators=(",",":"))
print("index",len(rows))
# 别名 → 卡文件名（服务端按别名找卡与字形）
amap={}
for r in rows:
    ch=r["c"]
    for a in (r["a"] or []):
        a=str(a).strip()
        if a and a!=ch: amap.setdefault(a,ch)
json.dump(amap,io.open(os.path.join(C,"alias-index.json"),"w",encoding="utf-8"),ensure_ascii=False,separators=(",",":"))
print("alias",len(amap))
# 简体表单一真源：cards/variants.json → web/public/variants.json（服务端路由用）
rp=os.path.join(os.path.dirname(C),"variants.json")
with io.open(rp,"w",encoding="utf-8",newline="\n") as f:
    json.dump(variants,f,ensure_ascii=False,indent=1); f.write("\n")
print("variants",len(variants))