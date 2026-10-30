# -*- coding: utf-8 -*-
import json,io,os,glob,sys,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
R=r"D:\系统汉字"; C=R+r"\web\public\cards"
m=json.load(io.open(R+r"\.tmp-charmap.json",encoding="utf-8"))
cards={os.path.basename(p)[:-5] for p in glob.glob(C+r"\*.json")}
todo=[c for c in m if c not in cards][:12]
print("取",len(todo),"".join(todo))
made=[]
for ch in todo:
    v=m[ch]; txt=(v.get("text") or "").strip()
    bu=v.get("bu") or {}; num=bu.get("num") if isinstance(bu,dict) else None; name=bu.get("name") if isinstance(bu,dict) else ""
    py_=v.get("py") or ""
    txt=re.sub(r"^[^《]*?》?","",txt) if False else txt
    d={"char":ch,"pinyin":py_,"level":3,"parent":name or "","bus":[{"num":num or 0,"name":name or ""}],"sections":[
      {"key":"benyi","label":"本义","text":txt[:300],"cites":[]},
      {"key":"xingpang","label":"形旁声旁","text":f"屬第{num}部「{name}部」；形旁定類、聲旁取義（詳本部字根卡）。","cites":[]},
      {"key":"shengmu","label":"声母拟态","text":f"{py_[:1]}：今讀 {py_}；按緒論擬態義取一面（推）。","cites":[]}]}
    json.dump(d,io.open(os.path.join(C,ch+".json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1); made.append(ch)
print("建卡",len(made))