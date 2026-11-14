# -*- coding: utf-8 -*-
"""剥离卡文栏首的标签前缀（本義：/轉義：/辯證：/音源：/字族衍義：/字形：/所属卷：）。
用法: python tools/strip-labels.py [--dry]
"""
import json, io, os, re, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
C = r"D:\系统汉字\web\public\cards"
LAB = re.compile(r"^\s*(本義|本义|轉義|转义|辯證|辩证|音源|字族衍義|字族衍义|聲母擬態|声母拟态|字形|所属卷)[：:]\s*")
dry = "--dry" in sys.argv
n = 0
files = 0
for fn in sorted(os.listdir(C)):
    if not fn.endswith(".json") or fn in ("index.json", "variants.json", "alias-index.json"):
        continue
    p = os.path.join(C, fn)
    try:
        d = json.load(io.open(p, encoding="utf-8"))
    except Exception:
        continue
    ch = False
    for s in d.get("sections", []):
        t = s.get("text")
        if isinstance(t, str):
            t2 = LAB.sub("", t, count=1)
            if t2 != t:
                s["text"] = t2
                ch = True
        ps = s.get("paras")
        if isinstance(ps, list) and ps:
            first = ps[0]
            if isinstance(first, str):
                f2 = LAB.sub("", first, count=1)
                if f2 != first:
                    ps[0] = f2
                    ch = True
        for k in ("rows", "groups"):
            pass
        if isinstance(s.get("groups"), list):
            for g in s["groups"]:
                for row in (g.get("rows") or []):
                    if isinstance(row, list):
                        for j, cell in enumerate(row):
                            if isinstance(cell, str) and LAB.match(cell):
                                row[j] = LAB.sub("", cell, count=1)
                                ch = True
    if ch:
        files += 1
        if not dry:
            json.dump(d, io.open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("strip-labels:", files, "files", "(dry)" if dry else "")
