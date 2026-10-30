# -*- coding: utf-8 -*-
import io,json,glob,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"; bad=[]; fixed=0
for f in glob.glob(C+r"\卷*.json"):
    d=json.load(io.open(f,encoding="utf-8")); ch=False
    for s in d["sections"]:
        for g in (s.get("groups") or []):
            if "部目" in (g.get("title") or "") or (g.get("rows") and str(g["rows"][0][0]).endswith("部")):
                if g.get("header")!=["部目","字根","中心义","字族"]:
                    g["header"]=["部目","字根","中心义","字族"]; ch=True
                if g.get("rows") and len(g["rows"][0])!=4:
                    g["rows"]=[(r+["—"]*4)[:4] for r in g["rows"]]; ch=True
    if ch: json.dump(d,io.open(f,"w",encoding="utf-8"),ensure_ascii=False,indent=1); fixed+=1
print("修正",fixed)