# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
def L(ch): return json.load(io.open(os.path.join(C,ch+".json"),encoding="utf-8"))
def S(ch,d): json.dump(d,io.open(os.path.join(C,ch+".json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
d=L("㕞"); d["rootLevel"]=3
d["sections"].append({"key":"erji","label":"本部三级字根","text":"刷、唰、涮皆从㕞省聲，为其实衍之字。","cites":[]})
S("㕞",d)
for ch in ("刷","唰","涮"):
    c=L(ch)
    if c.get("parent")!="㕞": c["parent"]="㕞"; c["rootLevel"]=3 if False else None
    c.pop("rootLevel",None) if c.get("level")==3 else None
    S(ch,c)
p=L("尸")
for s in p["sections"]:
    if s["key"]=="erji":
        s["links"]=[{"ch":"尺","label":"尺"}]
S("尸",p)
print("ok")