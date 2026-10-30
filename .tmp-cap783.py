# -*- coding: utf-8 -*-
import io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
b=r"D:\系统汉字\.tmp-rel2.py"; t=io.open(b,encoding="utf-8").read()
t=t.replace("return sorted(x for x in s if x)","return sorted(x for x in s if x and (x==c or x not in _OWN))",1)
io.open(b,"w",encoding="utf-8",newline="\n").write(t); print("patched")