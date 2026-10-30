# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\cards\芪.json"
d=json.load(io.open(p,encoding="utf-8"))
d["head"]="芪（荎茋蝭）"; d["aliases"]=["荎","茋","蝭"]
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print(d["head"],d["aliases"])