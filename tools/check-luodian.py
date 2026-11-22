"""校验「取义落点」破折号后的桥句：短、不复述、不推理。

用法：
    python tools/check-luodian.py             # 全库体检（只报数，不失败）
    python tools/check-luodian.py 兩 㒼       # 指定卡严格校验，有问题 exit 1

判据（见 prompts/exegesis.md §16.1、§19 与 HANDOFF 第八类错误）：
  F1 一行里出现多个「——」
  F2 「——」后为空
  F3 桥句开头是标点
  F4 桥句超过 12 字（一句写不完，多半在作释义）
  F5 桥句含因果/解释连词：故、所以、因此、因而、從而、可見、這是、稱為、表示
  F6 桥句与该族卡「釋義」原文有 >=5 字连续重合（等于复述原文）
  F7 桥句出现「借聲/借音/借其聲/借其音」（音譯字写法除外）
  F8 桥句与组题有 >=5 字连续重合（复述组题）
"""
import glob
import io
import json
import os
import re
import sys

MAXLEN = 12
CONN = re.compile("故|所以|因此|因而|從而|可見|這是|稱為|表示")
BORROW = re.compile("借[其]?[聲音]")
SKIP = {"index.json", "alias-index.json", "variants.json"}


def lcs(a, b):
    if not a or not b:
        return 0
    prev = [0] * (len(b) + 1)
    best = 0
    for i in range(1, len(a) + 1):
        cur = [0] * (len(b) + 1)
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                cur[j] = prev[j - 1] + 1
                if cur[j] > best:
                    best = cur[j]
        prev = cur
    return best


def load(path):
    try:
        d = json.load(io.open(path, encoding="utf-8"))
    except Exception:
        return None
    return d if isinstance(d, dict) else None


def rows_of(d):
    shiyi = ""
    for s in d.get("sections") or []:
        if s.get("key") == "shiyi":
            shiyi = s.get("text") or ""
    out = []
    for s in d.get("sections") or []:
        if s.get("key") != "zizu":
            continue
        for g in s.get("groups") or []:
            title = g.get("title") or ""
            for r in g.get("rows") or []:
                if len(r) >= 4:
                    out.append((r[0], title, r[3], shiyi))
    return out


def check(char, title, text, shiyi):
    bad = []
    if text.count("——") > 1:
        bad.append("F1-多破折号")
    if "——" not in text:
        return bad
    tail = text.split("——", 1)[1].strip()
    if not tail:
        bad.append("F2-空桥句")
        return bad
    if tail[0] in "，。、；：,.;:":
        bad.append("F3-起首标点")
    if len(tail) > MAXLEN:
        bad.append("F4-过长%d" % len(tail))
    m = CONN.search(tail)
    if m:
        bad.append("F5-连词%s" % m.group(0))
    if shiyi and lcs(tail, shiyi) >= 5:
        bad.append("F6-复述释义")
    if BORROW.search(tail) and "音譯" not in tail:
        bad.append("F7-借声")
    if title and lcs(tail, title) >= 5:
        bad.append("F8-复述组题")
    return bad


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    strict = bool(args)
    targets = set(args)
    files = sorted(glob.glob("web/public/cards/*.json"))
    total = 0
    fails = 0
    shown = 0
    for p in files:
        name = os.path.basename(p)[:-5]
        if os.path.basename(p) in SKIP:
            continue
        if targets and name not in targets:
            continue
        d = load(p)
        if not d:
            continue
        for char, title, text, shiyi in rows_of(d):
            if "——" not in text:
                continue
            total += 1
            bad = check(char, title, text, shiyi)
            if not bad:
                continue
            fails += 1
            if strict or shown < 20:
                print("%s %s %s | %s" % (name, char, ",".join(bad), text))
                shown += 1
    print("rows %d bad %d" % (total, fails))
    if strict and fails:
        sys.exit(1)


if __name__ == "__main__":
    main()
