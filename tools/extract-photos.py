# -*- coding: utf-8 -*-
"""按「图随字条」原则，把原稿 docx 里所有非字形插图抽到 web/public/glyphs/photos/<字>/NN.jpg
判定：图片长边 >= 200px 视为插图（字形小图一般 <= 200px）；
归属：向前找最近的「字头条」（首字 + 拼音），找不到时用最近的「X（异体）：」族名条。
"""
import glob, hashlib, io, json, os, re
from docx import Document
from docx.oxml.ns import qn
from PIL import Image

SRC = r"D:\字谱智能体"
OUT = r"D:\系统汉字\web\public\glyphs\photos"
HAN = r"\u3400-\u4DBF\u4E00-\u9FFF\uF900-\uFAFF\U00020000-\U0002A6DF"
PY = "a-zA-Züāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜńňǹḿ"
RE_TITLE = re.compile(rf"^([{HAN}]{{1,3}})(?:（([{HAN}]{{1,8}})）)?\s*([{PY}]{{1,12}})")
RE_FAMILY = re.compile(rf"^([{HAN}])(?:（([{HAN}]{{1,8}})）)?\s*[：:]")

def main():
    seen = {}
    stats = []
    for path in sorted(glob.glob(os.path.join(SRC, "*.docx"))):
        base = os.path.basename(path)
        try:
            doc = Document(path)
        except Exception:
            continue
        paras = doc.paragraphs
        owners = []  # 每个段落的最近字头
        cur = None
        for p in paras:
            t = (p.text or "").strip()
            m = RE_TITLE.match(t) or RE_FAMILY.match(t)
            if m:
                cur = m.group(1)
            owners.append(cur)
        n = 0
        for i, p in enumerate(paras):
            for b in p._p.findall(".//" + qn("a:blip")):
                rid = b.get(qn("r:embed"))
                part = doc.part.related_parts.get(rid)
                if part is None or not hasattr(part, "blob"):
                    continue
                blob = part.blob
                try:
                    im = Image.open(io.BytesIO(blob))
                    w, h = im.size
                except Exception:
                    continue
                if max(w, h) < 200:
                    continue
                ch = owners[i]
                if not ch:
                    continue
                digest = hashlib.sha1(blob).hexdigest()
                if digest in seen:
                    continue
                seen[digest] = True
                d = os.path.join(OUT, ch)
                os.makedirs(d, exist_ok=True)
                idx = len([f for f in os.listdir(d) if f.endswith((".jpg", ".png"))]) + 1
                fn = os.path.join(d, f"{idx:02d}.jpg")
                im.convert("RGB").save(fn, "JPEG", quality=90)
                n += 1
                stats.append((ch, base, i, w, h))
        if n:
            print(f"{base}: {n}")
    print("total images:", len(stats), "chars:", len({s[0] for s in stats}))
    json.dump([{"char": c, "file": f, "para": p, "w": w, "h": h} for c, f, p, w, h in stats],
              open(r"D:\系统汉字\web\public\photo-index.json", "w", encoding="utf-8"), ensure_ascii=False, indent=0)
    for row in stats[:40]:
        print(row)

if __name__ == "__main__":
    main()
