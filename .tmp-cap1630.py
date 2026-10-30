# -*- coding: utf-8 -*-
import json, io, os, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
from docx import Document
G = r"D:\系统汉字\web\public\glyphs"
doc = Document(r"D:\字谱智能体\卷三  矢.docx")
parts = doc.part.related_parts
ps = doc.paragraphs
# 意 的古文字字形行在 p539-541
rids = []
for k in (539, 540, 541):
    for el in ps[k]._p.iter():
        for a, v in el.attrib.items():
            if a.endswith("}embed") or a.endswith("}id"):
                try:
                    b = parts[v].blob
                except KeyError:
                    continue
                if b[:4] == b"\x89PNG" or b[:2] == b"\xff\xd8":
                    rids.append(v)
seen = []
for r in rids:
    if r not in seen:
        seen.append(r)
d = os.path.join(G, "意")
os.makedirs(d, exist_ok=True)
n = 0
for r in seen:
    b = parts[r].blob
    ext = ".png" if b[:4] == b"\x89PNG" else ".jpg"
    open(os.path.join(d, f"{n+1:02d}{ext}"), "wb").write(b)
    n += 1
print("意 glyphs", n)
p = os.path.join(G, "index.json")
j = json.load(io.open(p, encoding="utf-8"))
chars = j.get("chars") or j
files = sorted(os.listdir(d))
chars["意"] = {"doc": "卷三 矢", "files": [f"意/{f}" for f in files]}
json.dump({"chars": chars}, io.open(p, "w", encoding="utf-8"), ensure_ascii=False)
# 意部不许有插图：清掉误挂
P = os.path.join(G, "photos")
ip = os.path.join(P, "index.json")
ph = json.load(io.open(ip, encoding="utf-8"))["photos"]
members = ["意", "噫", "䪰", "癔", "譩", "嬑", "鷾", "䗷", "億", "檍", "𣚍", "澺", "憶", "臆", "繶", "醷", "𢶶", "鐿"]
removed = []
for ch in members:
    if ch in ph:
        removed.append(ch)
        ph.pop(ch, None)
    dd = os.path.join(P, ch)
    if os.path.isdir(dd):
        for f in os.listdir(dd):
            os.remove(os.path.join(dd, f))
        os.rmdir(dd)
json.dump({"photos": ph}, io.open(ip, "w", encoding="utf-8"), ensure_ascii=False)
print("removed photos", removed)
