# -*- coding: utf-8 -*-
import io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\tools\check-head-alias.py"
t=io.open(p,encoding="utf-8").read()
old='    miss=[ch for ch in CJK.findall(m.group(1)) if ch!=me and ch not in al]'
new='    miss=[ch for ch in CJK.findall(m.group(1)) if ch!=me and ch not in al and not os.path.exists(os.path.join(C,ch+".json"))]'
assert old in t
io.open(p,"w",encoding="utf-8",newline="\n").write(t.replace(old,new,1))
print("patched")