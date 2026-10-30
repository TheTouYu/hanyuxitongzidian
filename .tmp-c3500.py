import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
for ch in ("曳","弋","式","尗"):
    p=rf"D:\系统汉字\web\public\cards\{ch}.json"; d=json.load(io.open(p,encoding="utf-8"))
    for s in d["sections"]:
        for g in s.get("groups",[]) or []:
            for r in g.get("rows",[]) or []:
                if len(r)>=3 and ("莧" in str(r[0]) or r[2].strip()=="天"):
                    print(ch,"|",r)