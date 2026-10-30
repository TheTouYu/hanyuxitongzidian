# -*- coding: utf-8 -*-
import io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\tools\build-card-index.py"
t=io.open(p,encoding="utf-8").read()
old='rows.append({"ch":d.get("char"),'
new='rows.append({'
assert old in t
io.open(p,"w",encoding="utf-8",newline="\n").write(t.replace(old,new,1))
print("patched builder")