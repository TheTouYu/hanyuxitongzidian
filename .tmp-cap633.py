# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
p=os.path.join(C,"智.json"); d=json.load(io.open(p,encoding="utf-8"))
d["level"]=3; d["parent"]="知"; d["rootLevel"]=3
d["sections"]=[s for s in d["sections"] if s.get("key")!="erji"]
d["sections"].insert(-1,{"key":"shangji","label":"上级字根","text":"一级字根：矢；二级字根：知；本字智为三级字根。","cites":[],
  "links":[{"ch":"矢","label":"矢（一级）"},{"ch":"知","label":"知（二级）"}]})
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("智 level3 parent知")