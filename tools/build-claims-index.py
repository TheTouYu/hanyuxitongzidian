# -*- coding: utf-8 -*-
"""扫全库「字族」Claim，建立 字 → [{claim, title}] 索引，供字卡在无独立条时兜底（正文由服务端按 id 取）。"""
import glob
import json
import os
import re

ROOT = r"D:\系统汉字"
OUT = os.path.join(ROOT, r"web\public\claims-index.json")
pat = re.compile(
    r"<!-- CLAIM:START (clm_[0-9A-F]+) -->\s*\n### (.+?)\n(.*?)#### 适用边界",
    re.S,
)
HAN = re.compile(r"[\u3400-\u4DBF\u4E00-\u9FFF\uF900-\uFAFF]")

VARIANT = {}
try:
    _v = json.load(open(os.path.join(ROOT, r"web\public\variants.json"), encoding="utf-8"))
    for simp, trad in _v.items():
        VARIANT.setdefault(trad, simp)
except Exception:
    pass

index = {}
count = 0
for path in glob.glob(os.path.join(ROOT, "knowledge", "**", "*.md"), recursive=True):
    text = open(path, encoding="utf-8").read()
    for cid, title, body in pat.findall(text):
        if "字族" not in title:
            continue
        count += 1
        # 只收标题里的字（字族标题已把该族的字列全），避免把正文里偶然提到的字也拉进来
        head = title + body
        chars = set(HAN.findall(head))
        chars |= {VARIANT[c] for c in list(chars) if c in VARIANT}
        for ch in chars:
            index.setdefault(ch, []).append({"claim": cid, "title": title.strip()})

for ch in index:
    index[ch] = index[ch][:2]

json.dump({"generated": "2026-10-21", "claims": count, "byChar": index},
          open(OUT, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
print(OUT, "claims", count, "chars", len(index), "bytes", os.path.getsize(OUT))
