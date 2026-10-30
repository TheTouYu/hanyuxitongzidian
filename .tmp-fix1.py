# -*- coding: utf-8 -*-
import io,sys,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\.tmp-huo.py"
t=io.open(p,encoding="utf-8").read()
t=t.replace('(149,"①","指鶴色，表示紅色、青色、白色",164)','(149,"①","指鶴色，表示紅色、青色、白色",154)')
io.open(p,"w",encoding="utf-8",newline="\n").write(t)
print("fixed")