# -*- coding: utf-8 -*-
import io,json,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
for f in [r"D:\系统汉字\web\public\test.html",r"D:\系统汉字\web\public\index.html"]:
    h=io.open(f,encoding="utf-8").read()
    print(f.split("\\")[-1], "has g.header:", "g.header||" in h)
C=r"D:\系统汉字\web\public\cards"; p=rf"{C}\第一章士.json"; d=json.load(io.open(p,encoding="utf-8"))
print("juan keys:", [ (s.get("key"), [g.get("header") for g in s.get("groups",[])]) for s in d["sections"] if s.get("key")=="juan"])