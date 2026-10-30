# -*- coding: utf-8 -*-
import os,sys,glob
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
for ch in ("（原稿未列具體字）",):
    p=C+os.sep+ch+".json"
    if os.path.exists(p): os.remove(p); print("removed bogus",ch)
print("total cards",len(glob.glob(C+r"\*.json"))-1)