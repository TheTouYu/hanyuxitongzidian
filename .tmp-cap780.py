# -*- coding: utf-8 -*-
import io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
b=r"D:\系统汉字\.tmp-rel2.py"; t=io.open(b,encoding="utf-8").read()
if "own_cards" not in t:
    t=t.replace("def _alist(c,d):",
"""import os as _os
_OWN=set(_os.path.splitext(f)[0] for f in _os.listdir(r"D:\\系统汉字\\web\\public\\cards") if f.endswith(".json"))
def _alist(c,d):""",1)
    t=t.replace("return sorted(set(out))","return sorted(set(x for x in out if x==c or x not in _OWN))",1)
    io.open(b,"w",encoding="utf-8",newline="\n").write(t); print("alist filtered")