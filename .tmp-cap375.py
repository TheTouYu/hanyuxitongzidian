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

BEN = ("丮部（第375部）部头：甲骨文象两手同时拾掇之形，与𠬞、共不同者，𠬞共只两手捧提，丮则两手作复杂劳作而不可分开；"
       "《說文》「持也，象手有所丮據之形，讀若𢧢，幾劇切」。音源借音：婴儿之手多拳握，故古丮、兒可通；"
       "又义音同「㐁」，夙从丮从夕，拜月而早作。字族衍义多指操持、劳作。")

rows = [
 ("丮", "jǐ", "本部部首字，本義象两手同时拾掇、作复杂劳作之形，与「共」「𠬞」之简单捧提有别。",
  "共、𠬞、持", "两手合而持之，取「聚而持」一面；此部诸字皆由「持」义分张。"),
 ("𠩀", "jú", "𠩀从反丮，《說文》「拖持也，居玉切」，本义与丮同，不过反写其形。",
  "丮、拖、持", "反写而义不变，可见丮之核心在「持」，不在手势方向。"),
 ("谻", "jí/jué", "谻从𠃨𧮫聲，《說文》「相踦之也」，足相踦貌；《方言》又训「倦也」。",
  "踦、倦、𧮬", "足相踦是用力相持，倦是持之久而力尽，皆由「持」转出。"),
 ("𤜾", "jǐ", "𤜾从犬丮聲，《集韻》「獸名，窮矍也，或作犱」：夔一类捷兽。",
  "夔、矍、犱", "捷兽之持物以爪，故从丮；义落在兽名，是借声兼取持象。"),
 ("𠯎", "jǐ", "𠯎从口丮聲，《字彙》「音吉，聲也」：只记其声，无实义可训。",
  "口、聲、音", "专记声响，属借声之列，不取持义。"),
 ("𨑽", "zhuó", "𨑽从辵丮聲，《篇海類編》「音拙，疾風也」。",
  "風、疾、拙", "疾风之来如手攫取，取「攫持」一面。"),
 ("夙", "sù", "夙从丮从夕，甲骨文象双手拜月之状，义音同「宿」；引申早（《玉篇》「早也，旦也」）、平素，又训敬（《玉篇》「敬也」）。",
  "宿、早、敬", "拜月而夙兴，取「持事不休」一面，故「敬」亦由此出。"),
 ("珟", "sù", "珟从玉夙聲，《廣韻》「朽玉也，又姓」；《集韻》「玊，琢玉工，或作𤥔、璛」。",
  "玉、玊、璛", "朽玉有疵如持之未谨，取「持而失养」一面。"),
 ("洬", "sù/shuò", "洬从水夙聲，《廣韻》「雨聲」，《集韻》「大風雨皃」。",
  "雨、風、霈", "风雨之声急而相持，取「迫持」一面。"),
 ("㑉", "sù", "㑉从人夙聲，《集韻》「傗㑉，不伸也」：身不得伸展。",
  "傗、屈、伸", "不伸者受持而屈，取「被持」一面。"),
]

claims, cards = [], []
for i, (ch, py, body, heng, sm) in enumerate(rows, 1):
    secs = [
        {"key": "bengen", "label": "字根本義", "text": BEN, "cites": [ch]},
        {"key": "zigen", "label": "字根", "text": f"{ch}（{py}）属丮部。" + body, "cites": [ch]},
        {"key": "xingpang", "label": "形旁與聲旁",
         "text": "形旁定类，声旁「丮」取比喻义——象两手合持、把物拾起不放一样。", "cites": [ch]},
        {"key": "hengxiang", "label": "横向比較",
         "text": f"同部相邻者：{heng}；形符各定所附，义则由「持」之某面分张。", "cites": [ch]},
        {"key": "shengmu", "label": "聲母義", "text": sm, "cites": [ch]},
    ]
    cards.append({"char": ch, "pinyin": py, "bus": ["丮部"], "sections": secs,
                  "sources": ["《系統漢語》卷六十三「索」第375部「丮部」", "說文解字", "集韻", "玉篇", "廣韻"]})
    text = "\n\n".join(f"【{s['label']}】{s['text']}" for s in secs)
    claims.append({"id": f"zk-375-{i:02d}", "node": "hanzi-yinyuan", "topic_id": "topic-zika-shizi",
                   "title": f"{ch}（{py}）丮部字卡：{heng.split('、')[0]}之取象",
                   "statement": text,
                   "boundary": f"字卡释字，第375部「丮部」；{ch}依原稿该条训释分属。",
                   "permission": "public", "fact_classes": ["evidence_scope"],
                   "duplicate_resolution": "create_distinct_with_boundary"})

for c in cards:
    json.dump(c, open(os.path.join(ROOT, "web", "public", "cards", c["char"] + ".json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
print("cards", len(claims))

draft = {"schema_version": 1, "intent": "字卡375丮部首10字 2026-10-23", "risk": "medium", "claims": claims}
path = os.path.join(ROOT, "intake", "20261023-字卡375丮部.json")
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
