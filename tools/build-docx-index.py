# -*- coding: utf-8 -*-
"""建 docx 字头索引：web/public/docx-index.json
扫 D:\\字谱智能体\\*.docx，把含字头读音/《说文》的段落按字头归档。
"""
import glob, json, os, re, sys
from docx import Document

SRC = r"D:\字谱智能体"
OUT = r"D:\系统汉字\web\public\docx-index.json"

HAN = r"\u3400-\u4DBF\u4E00-\u9FFF\uF900-\uFAFF\U00020000-\U0002A6DF"
PY = "a-zA-Züāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜńňǹḿ"
RE_TITLE = re.compile(rf"^([{HAN}]{{1,3}})(?:（([{HAN}]{{1,8}})）)?\s*([{PY}]{{1,12}})")
RE_FAMILY = re.compile(rf"^([{HAN}])(?:（([{HAN}]{{1,8}})）)?\s*[：:]")
RE_HAS = re.compile(r"《(說文|说文|玉篇|廣韻|广韵|集韻|集韵|釋名|释名|爾雅|尔雅|方言|廣雅|广雅)")

def clean(t):
    t = re.sub(r"\s+", " ", t).strip()
    return t[:1400]

def main():
    files = sorted(glob.glob(os.path.join(SRC, "*.docx")))
    chars = {}
    n_para = n_keep = 0
    for path in files:
        base = os.path.basename(path)
        try:
            doc = Document(path)
        except Exception as e:
            print("SKIP", base, e)
            continue
        for i, p in enumerate(doc.paragraphs):
            t = p.text
            n_para += 1
            if not t or len(t) < 8:
                continue
            m = RE_TITLE.match(t) or RE_FAMILY.match(t)
            if not m:
                continue
            keep = bool(RE_HAS.search(t)) or bool(RE_TITLE.match(t))
            if not keep:
                continue
            head = m.group(1)
            body = clean(t)
            for key in {head, head[0]}:
                chars.setdefault(key, []).append({"f": base, "p": i, "t": body})
            n_keep += 1
    data = {"v": 1, "source": "系统汉语原稿 docx", "chars": chars}
    with open(OUT, "w", encoding="utf-8", newline="\n") as f:
        json.dump(data, f, ensure_ascii=False, separators=(",", ":"))
    size = os.path.getsize(OUT) / 1024 / 1024
    print(f"files={len(files)} paras={n_para} kept={n_keep} chars={len(chars)} size={size:.1f}MB")
    for probe in ("感", "羅", "海", "銀", "見"):
        print(probe, len(chars.get(probe, [])))

if __name__ == "__main__":
    main()
