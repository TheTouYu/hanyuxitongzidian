# -*- coding: utf-8 -*-
"""部级一致性检查：python tools/check-bu.py 朿"""
import json, io, os, re, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
C = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "web", "public", "cards")
PREFIX = re.compile(r'^(本義|本义|轉義|转义|辯證|辩证|音源)[：:]')
SM = re.compile(r"^([a-zA-Z]{1,2}「[^」]+」(取「[^」]」：|不系：)|不取義：)")
bu = sys.argv[1] if len(sys.argv) > 1 else "朿"
err = []
head = json.load(io.open(os.path.join(C, bu + ".json"), encoding="utf-8"))
if head.get("level") != 1:
    err.append(f"{bu}: 部头 level≠1")
keys = [s.get("key") for s in head.get("sections", [])]
for need in ("benyi", "zizu"):
    if need not in keys:
        err.append(f"{bu}: 部头缺 {need} 栏")
erji = [s for s in head.get("sections", []) if s.get("key") == "erji"]
links = []
for s in erji:
    links += [x.get("ch") for x in s.get("links", [])]
members = {}
for s in head.get("sections", []):
    if s.get("key") == "zizu":
        for g in s.get("groups", []):
            for r in g.get("rows", []):
                if not r or not r[0]:
                    err.append(f"{bu}: 字族表有空行")
                    continue
                ch = r[0].split("（")[0].split("(")[0]
                members[ch] = bu
for e in links:
    p = os.path.join(C, e + ".json")
    if not os.path.exists(p):
        err.append(f"{bu}: 二级字根 {e} 无卡")
        continue
    d = json.load(io.open(p, encoding="utf-8"))
    if d.get("level") != 2:
        err.append(f"{e}: 二级字根 level≠2")
    for s in d.get("sections", []):
        if s.get("key") == "zizu":
            for g in s.get("groups", []):
                for r in g.get("rows", []):
                    ch = r[0].split("（")[0].split("(")[0]
                    members[ch] = e
for ch, parent in members.items():
    p = os.path.join(C, ch + ".json")
    if not os.path.exists(p):
        err.append(f"缺卡: {ch}（{parent} 族）")
        continue
    d = json.load(io.open(p, encoding="utf-8"))
    if d.get("parent") != parent and parent not in (d.get("parents") or []):
        err.append(f"{ch}: parent={d.get('parent')} 应为 {parent}")
    if d.get("level") != 3:
        err.append(f"{ch}: level={d.get('level')} 应为 3")
    if d.get("rootLevel"):
        err.append(f"{ch}: 谐声字不应有 rootLevel")
    ks = [s.get("key") for s in d.get("sections", [])]
    if not ks or ks[0] != "shiyi":
        err.append(f"{ch}: 首栏应为 shiyi，实为 {ks}")
    sm = [s for s in d.get("sections", []) if s.get("key") == "shengmu"]
    if not sm:
        err.append(f"{ch}: 缺声母拟态")
    elif not SM.match(sm[0].get("text", "").strip()):
        err.append(f"{ch}: 声母拟态格式不合规 → {sm[0].get('text','')[:30]}")
print(f"部 {bu}: 成员 {len(members)}，二级 {len(links)}，问题 {len(err)}")
for e in err:
    print(" -", e)
