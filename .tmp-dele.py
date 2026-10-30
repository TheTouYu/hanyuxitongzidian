# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
G=r"D:\系统汉字\web\public\glyphs"; ip=os.path.join(G,"index.json")
ix=json.load(io.open(ip,encoding="utf-8")); chs=ix["chars"]
print("厄 in index:", "厄" in chs, chs.get("厄",{}).get("files"))
if "厄" in chs:
    del chs["厄"]
json.dump(ix,io.open(ip,"w",encoding="utf-8"),ensure_ascii=False)
print("done")