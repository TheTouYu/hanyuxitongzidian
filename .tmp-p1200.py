import io
tool = r'''# -*- coding: utf-8 -*-
"""栏文不得以「本義：」等前缀重复开头（页面已有 h3 栏名）。
用法: python tools/check-prefix.py [部名]
"""
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"web","public","cards")
PRE=["本義：","本义：","轉義：","转义：","辯證：","辩证：","音源：","聲母擬態：","声母拟态：","釋義：","释义：","字族衍義："]
bu=sys.argv[1] if len(sys.argv)>1 else None
def inbu(d):
    if not bu: return True
    if d.get("parent")==bu: return True
    for b in (d.get("bus") or []):
        n=b.get("name") if isinstance(b,dict) else b
        if n==bu: return True
    return False
bad=[]
for fn in sorted(os.listdir(C)):
    if not fn.endswith(".json") or fn in ("index.json","variants.json"): continue
    d=json.load(io.open(os.path.join(C,fn),encoding="utf-8"))
    if not inbu(d): continue
    for s in d.get("sections",[]):
        t=(s.get("text") or "").lstrip()
        for p in PRE:
            if t.startswith(p): bad.append((d.get("char") or fn[:-5],s.get("key"),p)); break
print(("部 %s: "%bu if bu else "")+"问题 %d"%len(bad))
for c,k,p in bad[:20]: print("  ",c,k,p)
'''
io.open(r"D:\系统汉字\tools\check-prefix.py","w",encoding="utf-8",newline="\n").write(tool)
print("ok")