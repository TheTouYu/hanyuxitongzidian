# -*- coding: utf-8 -*-
import io,sys,re
p=r"D:\系统汉字\tools\check-bu.py"
s=io.open(p,encoding="utf-8").read()
if "序号重复" not in s:
    anchor="        probs.append("
    add='''        for g in (sec.get("groups") or []):
            if re.match(r"^[\\u2460-\\u2469]", str(g.get("title",""))):
                probs.append(f"{ch}: 字族群标题含序号（渲染会重复）→ {g.get('title')}")
'''
    i=s.find("    for ch,d in cards.items():")
    j=s.find("\n",i)
    s=s[:j+1]+add+s[j+1:]
    io.open(p,"w",encoding="utf-8").write(s)
    print("patched")
else: print("already")