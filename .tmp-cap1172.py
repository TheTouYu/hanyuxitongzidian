# -*- coding: utf-8 -*-
import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\cards\尺.json"; d=json.load(io.open(p,encoding="utf-8"))
order=["benyi","zhuanyi","bianzheng","yinyuan","shengmu","zigen","zizu","suoshujuan"]
secs=[]
for k in order:
    for s in d["sections"]:
        if s.get("key")==k and s not in secs: secs.append(s)
# 所属卷统一为链接版
secs=[s for s in secs if not (s.get("key")=="suoshujuan" and not s.get("links"))]
have=[s for s in secs if s.get("key")=="suoshujuan"]
if not have: secs.append({"key":"suoshujuan","label":"所属卷","text":"","links":[{"ch":"卷三矢","label":"卷三 矢"}]})
d["sections"]=secs
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
for s in secs: print(s.get("key"),s.get("label"),len(s.get("links",[]) or []),(s.get("text") or "")[:16])