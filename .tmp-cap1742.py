# -*- coding: utf-8 -*-
import json, io, os, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
from docx import Document
G = r"D:\系统汉字\web\public\glyphs"
doc = Document(r"D:\字谱智能体\卷三  矢.docx")
parts = doc.part.related_parts
ps = doc.paragraphs
def grab(k, ch):
    d = os.path.join(G, ch)
    os.makedirs(d, exist_ok=True)
    for f in os.listdir(d):
        os.remove(os.path.join(d, f))
    n = 0
    for el in ps[k]._p.iter():
        for a, v in el.attrib.items():
            if a.endswith("}embed") or a.endswith("}id"):
                try:
                    b = parts[v].blob
                except KeyError:
                    continue
                if len(b) < 800:
                    continue
                ext = ".png" if b[:4] == b"\x89PNG" else ".jpg"
                open(os.path.join(d, f"{n+1:02d}{ext}"), "wb").write(b)
                n += 1
    return n
n1 = grab(584, "ㄗ")
n2 = grab(596, "卽")
p = os.path.join(G, "index.json")
j = json.load(io.open(p, encoding="utf-8"))
ch = j.get("chars") or j
for k, name in ((584, "ㄗ"), (596, "卽")):
    fs = sorted(os.listdir(os.path.join(G, name)))
    ch[name] = {"doc": "卷三 矢", "files": [f"{name}/{f}" for f in fs]}
json.dump({"chars": ch}, io.open(p, "w", encoding="utf-8"), ensure_ascii=False)
print("ㄗ", n1, "卽", n2)
