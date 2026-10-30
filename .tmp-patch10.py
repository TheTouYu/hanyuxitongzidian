# -*- coding: utf-8 -*-
import io,json,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\.tmp-chjuan.py"; t=io.open(p,encoding="utf-8").read()
t=t.replace('    if n<100:\n        return CN[n//10]+"十"+(CN[n%10] if n%10 else "")\n    return str(n)',
            '    if n<100:\n        return CN[n//10]+"十"+(CN[n%10] if n%10 else "")\n    return "一百"')
io.open(p,"w",encoding="utf-8",newline="\n").write(t); print("cn patched")