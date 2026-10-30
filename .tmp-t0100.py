# -*- coding: utf-8 -*-
import io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
tool=r'''# -*- coding: utf-8 -*-
"""每部收尾自检：字头括注里的异体是否都已进 aliases（按字逐个，不整串）。
用法: python tools/check-aliases.py [部名]
"""
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"web","public","cards")
HAN=re.compile(r"[\u3400-\u9fff\U00020000-\U0002A6DF]")
bu=sys.argv[1] if len(sys.argv)>1 else None
bad=[]
for fn in sorted(os.listdir(C)):
    if not fn.endswith(".json") or fn in ("index.json","variants.json"): continue
    d=json.load(io.open(os.path.join(C,fn),encoding="utf-8"))
    if bu and (d.get("parent")!=bu and not (d.get("bus") and d["bus"][0].get("name")==bu)): continue
    ch=d.get("char") or fn[:-5]; h=d.get("head") or ""
    m=re.search(r"（([^）]+)）",h)
    if not m: continue
    need={x for x in HAN.findall(m.group(1)) if x!=ch}
    miss=need-set(d.get("aliases") or [])
    if miss: bad.append((ch,"".join(sorted(miss))))
print(("部 %s: "%bu if bu else "")+"问题 %d"%len(bad))
for c,m in bad[:20]: print("  ",c,"缺",m)
'''
p=os.path.join(r"D:\系统汉字","tools","check-aliases.py")
io.open(p,"w",encoding="utf-8",newline="\n").write(tool)
print("tool written")