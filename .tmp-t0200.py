# -*- coding: utf-8 -*-
import io
tool = r'''# -*- coding: utf-8 -*-
"""每部收尾自检：字头括注里的异体是否都已进 aliases（按字逐个，不整串）。
用法: python tools/check-aliases.py [部名]
"""
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"web","public","cards")
HAN=re.compile(r"[\u3400-\u9fff\U00020000-\U0002A6DF]")
bu=sys.argv[1] if len(sys.argv)>1 else None
def inbu(d):
    if not bu: return True
    if d.get("parent")==bu: return True
    for b in (d.get("bus") or []):
        name=b.get("name") if isinstance(b,dict) else b
        if name==bu: return True
    return False
bad=[]
for fn in sorted(os.listdir(C)):
    if not fn.endswith(".json") or fn in ("index.json","variants.json"): continue
    d=json.load(io.open(os.path.join(C,fn),encoding="utf-8"))
    if not inbu(d): continue
    ch=d.get("char") or fn[:-5]; h=d.get("head") or ""
    m=re.search(r"（([^）]+)）",h)
    if not m: continue
    need={x for x in HAN.findall(m.group(1)) if x!=ch}
    miss=need-set(d.get("aliases") or [])
    if miss: bad.append((ch,"".join(sorted(miss))))
print(("部 %s: "%bu if bu else "")+"问题 %d"%len(bad))
for c,m in bad[:20]: print("  ",c,"缺",m)
'''
io.open(r"D:\系统汉字\tools\check-aliases.py","w",encoding="utf-8",newline="\n").write(tool)
print("ok")