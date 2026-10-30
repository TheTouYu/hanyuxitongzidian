# -*- coding: utf-8 -*-
import json, subprocess, os, re

ROOT = r"D:\系统汉字"
PY = os.path.join(ROOT, ".runtime", "venv", "Scripts", "python.exe")
PKC = [PY, os.path.join(ROOT, "tools", "pkc_tmpfix.py")]
ENV = os.environ.copy()
ENV["PATH"] = os.path.join(ROOT, ".runtime", "mingit", "cmd") + os.pathsep + ENV.get("PATH", "")

def run(a):
    p = subprocess.run(PKC + a, cwd=ROOT, capture_output=True, text=True, encoding="utf-8", env=ENV)
    return p.returncode, p.stdout + p.stderr

BEN = ("丮部（第375部）部头象两手拾掇、作复杂劳作。本部孰支多指烂熟，埶支多指竖起、举起；"
       "字族中凡从「埶」者，除植立之外，又分出持、抵、烧、私近诸面，形符各定其落点。")

rows = [
 ("𨫔", "zhì", "𨫔从金埶聲，《說文》「羊棰端有鐵，讀若至」，羊车棰端的针；又读 xiè，为治苗杀草的田器、椹。",
  "棰、鍼、椹", "铁端植于棰，取「竖立而刺」一面。"),
 ("𨎌", "zhì", "𨎌从車埶聲，《說文》「抵也」，《玉篇》「前頓曰𨎌，後曰軒」：车前低而顿。",
  "抵、頓、軒", "前低而抵地，取「压而抵」一面，与竖起义相对成势。"),
 ("爇", "ruò", "爇从火蓺聲，《說文》「燒也」，引《春秋傳》「爇僖負覉」；甲骨文象举火把之形。",
  "燒、炳、燎", "举火把即举，取「举起」一面。"),
 ("褻", "xiè", "褻从衣埶聲，《說文》「私服」，又训狎、衣破之余。",
  "私、狎、衣", "贴身而近，取「附而驰纵」一面，竖义已转为近呢。"),
 ("讛", "yì", "讛从言蓺聲，《字彙》「寐語也」，《字彙補》「屛處語也」：梦中或背人处说话。",
  "寐、語、囈", "梦语支离不振，属借声，义不在竖。"),
 ("襼", "yì", "襼从衣蓺聲，《篇海》「袂也」：衣袖。",
  "袂、袖、衣", "袖举手而动，取「举而垂」一面。"),
 ("暬", "xiè", "暬从日埶聲，《說文》「日狎習相慢也」，同「褻」；又读 nié，训晦冥。",
  "狎、慢、晦", "日久而相狎，由近呢再转轻慢，仍从埶声之附近一面出。"),
]

claims, cards = [], []
for i, (ch, py, body, heng, sm) in enumerate(rows, 1):
    secs = [
        {"key": "bengen", "label": "字根本義", "text": BEN, "cites": [ch]},
        {"key": "zigen", "label": "字根", "text": f"{ch}（{py}）属丮部埶声一系。" + body, "cites": [ch]},
        {"key": "xingpang", "label": "形旁與聲旁",
         "text": "形旁定类，声旁取比喻义——象手持物而举、而植一样。", "cites": [ch]},
        {"key": "hengxiang", "label": "横向比較",
         "text": f"同系相邻者：{heng}；形符各定所附，义由「举／植／附」三面分张。", "cites": [ch]},
        {"key": "shengmu", "label": "聲母義", "text": sm, "cites": [ch]},
    ]
    cards.append({"char": ch, "pinyin": py, "bus": ["丮部"], "sections": secs,
                  "sources": ["《系統漢語》卷六十三「索」第375部「丮部」", "說文解字", "集韻", "篇海", "字彙"]})
    text = "\n\n".join(f"【{s['label']}】{s['text']}" for s in secs)
    claims.append({"id": f"zk-375c-{i:02d}", "node": "hanzi-yinyuan", "topic_id": "topic-zika-shizi",
                   "title": f"{ch}（{py}）丮部字卡：{heng.split('、')[0]}之取象",
                   "statement": text,
                   "boundary": f"字卡释字，第375部「丮部」埶声一系；{ch}依原稿该条训释分属。",
                   "permission": "public", "fact_classes": ["evidence_scope"],
                   "duplicate_resolution": "create_distinct_with_boundary"})

for c in cards:
    json.dump(c, open(os.path.join(ROOT, "web", "public", "cards", c["char"] + ".json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
print("cards", len(claims))

draft = {"schema_version": 1, "intent": "字卡375丮部余7字 2026-10-23", "risk": "medium", "claims": claims}
path = os.path.join(ROOT, "intake", "20261023-字卡375丮部丙.json")
json.dump(draft, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

rc, out = run(["knowledge-plan", "capture", "--file", path, "--format", "json"])
print("capture rc", rc)
m = re.search(r'"content_hash":\s*"([0-9a-f]{64})"', out)
b = re.search(r'"bundle_id":\s*"(bnd_[0-9a-f]+)"', out)
if not (m and b):
    print(out[-900:]); raise SystemExit(1)
h, bid = m.group(1), b.group(1)
print("bundle", bid, "hash", h)
for s in (["bundle-approve", bid, "--content-hash", h, "--apply"],
          ["bundle-apply", bid, "--content-hash", h, "--apply"]):
    r, o = run(s); print(s[0], r, '"applied": true' in o)
r, o = run(["rebuild"]); print("rebuild", r)
