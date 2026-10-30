# -*- coding: utf-8 -*-
import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\cards\秭.json"; d=json.load(io.open(p,encoding="utf-8"))
d["aliases"]=["秭"]; json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print(d.get("char"),d.get("head"),d["aliases"])