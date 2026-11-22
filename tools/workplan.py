# -*- coding: utf-8 -*-
"""workplan.py —— 把一部字族表拆成可并行的工单，再把工人的结果合并回父卡。

用途：部大、族行多时，lead 只做「原稿 → manifest」和「合并 + 验收」，
族卡与桥句分给多个 agent 并行写；合并是确定性的，不靠人手抄。

子命令：
    split  --manifest m.json --batch 6 --out .tmp-plan
    check  --manifest m.json --results .tmp-plan/results
    merge  --manifest m.json --results .tmp-plan/results [--apply]

manifest 结构（lead 负责，来自原稿）：
{
  "bu": {"num": 309, "name": "面", "head": "面"},
  "volume": {"ch": "卷五十四网", "label": "卷五十四网"},
  "groups": [
    {"title": "①指眼瞼的閉合，表示沉迷、羞愧、勉力",
     "parent": "面",
     "rows": [
       {"order": 1, "label": "湎（䤄𨟺𩈳）", "char": "湎",
        "pinyin": "miǎn", "cls": "水",
        "quote": "《說文》「…」", "bridge": "",
        "shiyi": "湎miǎn《說文》：…", "kind": "normal", "notes": ""}
     ]}
  ]
}

worker 结果（每批一个 JSON，可多人各写各的）：
{"items": [{"group": 0, "order": 1, "char": "湎", "bridge": "酒沉而迷"}]}

合并规则：
  - 行文本 = quote + "——" + bridge；若 row["text"] 有值则直接用它（讹字整行、音译等）。
  - 必填覆盖：manifest 每行恰好一次；char/order 对不上即失败。
  - 桥句过 check-luodian 的同一套规则（≤12 字、禁连词、不复述）。
  - 只改父卡 zizu.groups[].rows[3]，其余字段不动；默认 dry-run，--apply 才落盘。
"""
import argparse
import glob
import importlib.util
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CARDS = os.path.join(ROOT, "web", "public", "cards")

KIND_NO_BRIDGE = ("ezi", "translit", "proper", "name")


def load(path):
    with io.open(path, encoding="utf-8") as f:
        return json.load(f)


def dump(path, obj):
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with io.open(path, "w", encoding="utf-8", newline="\n") as f:
        json.dump(obj, f, ensure_ascii=False, indent=1)
        f.write("\n")


def load_luodian():
    p = os.path.join(ROOT, "tools", "check-luodian.py")
    spec = importlib.util.spec_from_file_location("check_luodian", p)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def iter_rows(man):
    for gi, g in enumerate(man.get("groups") or []):
        for row in g.get("rows") or []:
            yield gi, g, row


def row_text(row):
    if row.get("text"):
        return row["text"]
    quote = (row.get("quote") or "").strip()
    bridge = (row.get("bridge") or "").strip()
    if not bridge:
        return quote
    return quote + "——" + bridge


def compose(row, rec):
    """worker 结果 → 整段落点。rec 可给 text（整行）或 bridge（搭桥句）。"""
    if rec.get("text"):
        return rec["text"].strip()
    bridge = (rec.get("bridge") or "").strip()
    if not bridge:
        return ""
    if bridge.startswith("《") or "——" in bridge:
        return bridge
    return row_text(dict(row, bridge=bridge))


# ------------------------------------------------------------------ split
CONTRACT = """# 建卡工单（总则）

你有若干批 `batch-NN.json`，每批一个工人、互不重叠。**只做自己那批 items 里的行**，不要碰其他文件、不要改父卡、不要重建 index。
本批的批号在 `batch-NN.json` 的 `batch` 字段，结果文件对应 `%(results)s/batch-NN.json`（照 `batch-NN.template.json` 填）。

## 你要交什么
1. 每行一个族卡 `%(cards)s/<字>.json`（结构照 `%(skill)s` 第 4 节，参照 308 的族卡）。
2. 一个结果文件 `%(results)s/batch-NN.json`：
   `{"items":[{"group":0,"order":1,"char":"緉","bridge":"履必成雙","evidence":"履兩枚"}]}`
   - `group`/`order` 照工单，`char` 是首格的字（不含括号）。
   - `bridge` 是破折号后的搭桥句，≤12 字，不用因果连词，不复述釋義/组题，不写借声。
   - 音译字把 `bridge` 写成 `音譯字，只取其音`；讹字组/无义理的名物把 `text` 整行给出（见工单 row 的 kind/notes）。
   - `evidence` 写你据以搭桥的原稿词句（几个字即可）。

## 质量闸门（交之前自己跑，有 error 改到 0）
```
$env:PYTHONIOENCODING='utf-8'
.runtime\\python\\python.exe tools\\verify-card.py --file %(cards)s\\<字>.json --cards-dir %(cards)s
```
桥句由 lead 在合并前跑 `workplan.py check` 统一验；你按上面规则自查，别等机器。

## 禁止
- 不改 `index.json`、`alias-index.json`、`variants.json`、`glyphs/index.json`、父卡。
- 不跑 `build-card-index.py`，不重启服务，不 git add。
- 不复制别人的行，不合并工单。
"""


def cmd_split(args):
    man = load(args.manifest)
    out = args.out
    cards = os.path.abspath(args.cards_dir)
    results = os.path.join(out, "results")
    os.makedirs(results, exist_ok=True)
    rows = list(iter_rows(man))
    if not rows:
        sys.exit("manifest 没有行")
    batch = max(1, args.batch)
    chunks = [rows[i:i + batch] for i in range(0, len(rows), batch)]
    for bi, chunk in enumerate(chunks, 1):
        items = []
        for gi, g, row in chunk:
            items.append({
                "group": gi, "group_title": g.get("title"),
                "order": row.get("order"), "char": row.get("char"),
                "label": row.get("label"), "pinyin": row.get("pinyin"),
                "cls": row.get("cls"), "kind": row.get("kind") or "normal",
                "quote": row.get("quote") or "", "shiyi": row.get("shiyi") or "",
                "notes": row.get("notes") or "",
            })
        payload = {
            "batch": bi, "bu": man.get("bu"), "volume": man.get("volume"),
            "cards_dir": cards,
            "instructions": "只做本批 items；卡写 %s\\<字>.json，结果写 %s\\batch-%02d.json；自检见 README.md"
                            % (cards, results, bi),
            "items": items,
        }
        dump(os.path.join(out, "batch-%02d.json" % bi), payload)
        dump(os.path.join(out, "results", "batch-%02d.template.json" % bi),
             {"items": [{"group": x["group"], "order": x["order"],
                         "char": x["char"], "bridge": ""} for x in items]})
    with io.open(os.path.join(out, "README.md"), "w", encoding="utf-8", newline="\n") as f:
        f.write(CONTRACT % {"cards": cards, "results": results,
                            "skill": ".dsh/skills/hanzi-card/SKILL.md"})
    dump(os.path.join(out, "plan.json"), {
        "manifest": os.path.abspath(args.manifest),
        "bu": man.get("bu"), "volume": man.get("volume"),
        "batches": [{"file": "batch-%02d.json" % i, "rows": len(c),
                     "chars": [r[2].get("char") for r in c]}
                    for i, c in enumerate(chunks, 1)],
    })
    print("split: %d 行 → %d 批（每批 ≤%d），输出 %s" % (len(rows), len(chunks), batch, out))
    for i, c in enumerate(chunks, 1):
        print("  batch-%02d: %s" % (i, " ".join(str(r[2].get("char")) for r in c)))


# ------------------------------------------------------------------ check
def collect_results(results_dir):
    """返回 {(group, order, char): {"bridge":…, "text":…}}，并收集重复/格式错误。"""
    got = {}
    problems = []
    for fp in sorted(glob.glob(os.path.join(results_dir, "*.json"))):
        if fp.endswith(".template.json"):
            continue
        try:
            data = load(fp)
        except Exception as e:
            problems.append("%s 读不了：%s" % (os.path.basename(fp), e))
            continue
        for it in data.get("items") or []:
            key = (it.get("group"), it.get("order"), it.get("char"))
            if key in got:
                problems.append("%s 重复：group=%s order=%s char=%s"
                                % (os.path.basename(fp), key[0], key[1], key[2]))
            got[key] = {"bridge": (it.get("bridge") or "").strip(),
                        "text": (it.get("text") or "").strip()}
    return got, problems


def card_shiyi(path):
    try:
        d = load(path)
    except Exception:
        return None
    for s in d.get("sections") or []:
        if s.get("key") == "shiyi":
            return s.get("text") or ""
    return None


def cmd_check(args):
    man = load(args.manifest)
    got, problems = collect_results(args.results)
    luo = load_luodian()
    missing, bad = [], []
    for gi, g, row in iter_rows(man):
        key = (gi, row.get("order"), row.get("char"))
        rec = got.get(key)
        if not rec:
            missing.append(key)
            continue
        text = compose(row, rec)
        kind = row.get("kind") or "normal"
        if not text:
            bad.append((key, "空桥句"))
            continue
        if args.cards_dir:
            p = os.path.join(args.cards_dir, str(row.get("char")) + ".json")
            if not os.path.exists(p):
                bad.append((key, "缺族卡 %s" % os.path.basename(p)))
            else:
                shi = card_shiyi(p)
                if shi is None:
                    bad.append((key, "卡无 shiyi 栏"))
                elif shi.strip() != (row.get("shiyi") or "").strip():
                    bad.append((key, "釋義与工单不一致"))
        if kind in ("ezi", "translit"):
            continue
        for code in luo.check(row.get("char"), g.get("title"), text, row.get("shiyi") or ""):
            bad.append((key, code))
    for p in problems:
        print("PROBLEM", p)
    for k in missing:
        print("MISSING group=%s order=%s %s" % k)
    for (k, code) in bad:
        print("BAD group=%s order=%s %s → %s" % (k[0], k[1], k[2], code))
    print("check: rows %d，收到 %d，缺 %d，问题 %d"
          % (sum(1 for _ in iter_rows(man)), len(got), len(missing), len(bad) + len(problems)))
    sys.exit(0 if not missing and not bad and not problems else 1)


# ------------------------------------------------------------------ merge
def find_row(card, title, order):
    z = None
    for s in card.get("sections") or []:
        if s.get("key") == "zizu":
            z = s
            break
    if not z:
        return None
    for g in z.get("groups") or []:
        if g.get("title") != title:
            continue
        rs = g.get("rows") or []
        if 1 <= order <= len(rs):
            return rs[order - 1]
    return None


def cmd_merge(args):
    man = load(args.manifest)
    got, problems = collect_results(args.results)
    luo = load_luodian()
    cards = {}
    changes, errors = [], list(problems)
    for gi, g, row in iter_rows(man):
        key = (gi, row.get("order"), row.get("char"))
        card_ch = g.get("parent") or man.get("bu", {}).get("head")
        if card_ch not in cards:
            p = os.path.join(args.cards_dir, card_ch + ".json")
            if not os.path.exists(p):
                errors.append("父卡不存在：%s" % p)
                cards[card_ch] = None
            else:
                cards[card_ch] = load(p)
        card = cards[card_ch]
        if card is None:
            continue
        target = find_row(card, g.get("title"), row.get("order"))
        if target is None:
            errors.append("父卡 %s 找不到 组「%s」第 %s 行" % (card_ch, g.get("title"), row.get("order")))
            continue
        if key not in got:
            errors.append("缺结果 group=%s order=%s %s" % key)
            continue
        text = compose(row, got[key])
        kind = row.get("kind") or "normal"
        if not text:
            errors.append("%s 空桥句" % (key,))
            continue
        if kind not in ("ezi", "translit"):
            for code in luo.check(row.get("char"), g.get("title"), text, row.get("shiyi") or ""):
                errors.append("%s %s" % (key, code))
        if isinstance(target, list) and len(target) >= 4:
            if target[3] == text:
                continue
            changes.append((card_ch, g.get("title"), row.get("order"), target[3], text))
            target[3] = text
        else:
            errors.append("%s 目标行不是四格：%r" % (key, target))
    print("merge: 变更 %d 行，错误 %d" % (len(changes), len(errors)))
    for (cc, title, order, old, new) in changes[:args.max]:
        print("  [%s] %s #%s\n    - %s\n    + %s" % (cc, title[:14], order, old, new))
    if len(changes) > args.max:
        print("  … 还有 %d 行" % (len(changes) - args.max))
    for e in errors[:args.max]:
        print("  ERROR", e)
    if errors:
        sys.exit(1)
    if args.apply:
        for ch, card in cards.items():
            if card is not None:
                p = os.path.join(args.cards_dir, ch + ".json")
                dump(p, card)
        print("已写回：%s" % ", ".join(sorted(k for k, v in cards.items() if v)))
    else:
        print("（dry-run；加 --apply 写回）")


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)

    sp = sub.add_parser("split")
    sp.add_argument("--manifest", required=True)
    sp.add_argument("--batch", type=int, default=6)
    sp.add_argument("--out", required=True)
    sp.add_argument("--cards-dir", default=CARDS)
    sp.set_defaults(func=cmd_split)

    cp = sub.add_parser("check")
    cp.add_argument("--manifest", required=True)
    cp.add_argument("--results", required=True)
    cp.add_argument("--cards-dir", help="给了就顺带核对族卡釋義与工单逐字一致、卡是否存在")
    cp.set_defaults(func=cmd_check)

    mp = sub.add_parser("merge")
    mp.add_argument("--manifest", required=True)
    mp.add_argument("--results", required=True)
    mp.add_argument("--cards-dir", default=CARDS)
    mp.add_argument("--apply", action="store_true")
    mp.add_argument("--max", type=int, default=30)
    mp.set_defaults(func=cmd_merge)

    args = ap.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
