"""308 落点回改：把带因果连词、复述释义的桥句改短（一次性脚本，可留档）。

改法：只改 兩.json / 㒼.json 的 zizu.groups[].rows[3]；族卡释义不动。
"""
import io
import json

FIX = {
    "緉（䩫）": "《說文》「履兩枚也。」——履必成雙。",
    "輛": "《漢書注》「車一乗曰一兩」——一輿承雙輪。",
    "倆（𢎏）": "《集韻》「伎倆，巧也。」——一手不能成技。",
    "𨨄（鋃）": "《字海》「同鋃字。」——鏈環相銜而加諸物。",
}


def main():
    n = 0
    for name in ("兩", "㒼"):
        p = "web/public/cards/%s.json" % name
        d = json.load(io.open(p, encoding="utf-8"))
        for s in d["sections"]:
            if s.get("key") != "zizu":
                continue
            for g in s["groups"]:
                for r in g["rows"]:
                    if r[0] in FIX:
                        print(name, r[0], "->", FIX[r[0]])
                        r[3] = FIX[r[0]]
                        n += 1
        with io.open(p, "w", encoding="utf-8", newline="\n") as f:
            f.write(json.dumps(d, ensure_ascii=False, indent=1) + "\n")
    print("fixed", n)


if __name__ == "__main__":
    main()
