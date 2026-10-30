# -*- coding: utf-8 -*-
import json,io,sys,os
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
P=r"D:\系统汉字\web\public\glyphs\photos"
c=json.load(io.open(os.path.join(P,"captions.json"),encoding="utf-8")); CAP=c.get("captions") or c
CAP["蒂"]=["（帝部）花蒂","辣椒和脫落的蒂"]
CAP["款"]=["雙墩遺址（左）與魏晉（右）陶器底部款識"]
json.dump({"captions":CAP},io.open(os.path.join(P,"captions.json"),"w",encoding="utf-8"),ensure_ascii=False)
ph=json.load(io.open(os.path.join(P,"index.json"),encoding="utf-8"))["photos"]
no=[x for x,v in ph.items() if v and x not in CAP]
print("有图字头",len([1 for v in ph.values() if v]),"无注",len(no))