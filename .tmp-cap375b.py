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

BEN = ("丮部（第375部）部头「丮」象两手同时拾掇、作复杂劳作之形。本部内分两支：一为「孰（𦏧）」，从亯（祭坛）从丮，"
       "象在祭坛合手奉献祭品，本义祭祀，引申熟食、烂熟、谁、熟悉（原稿倾向以丮为声，非《說文》所云亯声）；"
       "一为「埶」，从丮从屮木，象种植移栽或竖木测影，引申技能（蓺、藝），字族多指竖起、举起。")

rows = [
 ("塾", "shú", "塾从土孰聲，《說文》「門側堂也，殊六切」，门内东西两侧的堂；崔豹《古今注》「塾之言熟也」，为朝君者门外详熟应对之所，后指民间教读处。",
  "堂、學、門", "熟思而后入，取「烂熟」一面；形符土定其为堂室。"),
 ("熟", "shú", "熟从火孰聲，《玉篇》「爛也」、《廣韻》「成也」；食物煮烂。",
  "爛、成、飪", "煮烂而诸味不分，正是「孰」之祭祀熟食义，故取烂熟一面。"),
 ("䃞", "shú", "䃞从石孰聲，《廣韻》「石聲」，《集韻》「石名」。",
  "石、聲、磬", "石声浑成如物烂熟，属借声，义只记名与声。"),
 ("埶", "yì/niè", "埶从丮从屮木，点者象种子，象意种植移栽；又象竖木测影（读 niè，通「臬」）；引申技能，或作蓺、藝。",
  "蓺、藝、臬", "手植而竖之，取「竖起」一面，本部此支总义。"),
 ("槸", "yì", "槸从木埶聲，《說文》「木相摩也，魚祭切」。",
  "摩、木、枝", "两木相摩如相植而立，取竖而相抵之象。"),
 ("槷", "niè/xiè", "槷从木埶聲，《廣韻》「危槷」不安，《正字通》「植木于地也」；通「臬」（射的）、「闑」（门梱），又为木楔。",
  "臬、闑、楔", "植木于地即竖，取「竖起」一面；通臬闑皆由直立引申。"),
 ("勢", "shì", "勢从力埶聲，《說文》「盛力，權也，經典通用埶」，又指形势、威力，古亦指睾丸（割势）。",
  "力、權、形", "力之竖起者为势，取「举起而盛」一面。"),
 ("熱", "rè", "熱从火埶聲，《說文》「溫也」，《釋名》「𤍽也，如火所燒𤍽」。",
  "火、溫、燒", "火气上腾而举起，取「竖起」一面；热升如势起。"),
 ("蓺", "yì", "蓺从艸埶聲，《玉篇》「種蒔也」；《集韻》「埶，一曰技能，或作蓺、藝、㙯，古作秇」，今简作「艺」。",
  "藝、種、技", "种植为艺之本，技能由种植引申，仍取「植而立」一面。"),
 ("褻", "xiè", "褻从衣埶聲，《說文》「私服」，《廣雅》「狎也」，《篇海》「衣破之餘曰褻」。",
  "衣、狎、私", "燕居之服贴身而近，取「附而驰纵」一面，已离竖起义。"),
]

claims, cards = [], []
for i, (ch, py, body, heng, sm) in enumerate(rows, 1):
    secs = [
        {"key": "bengen", "label": "字根本義", "text": BEN, "cites": [ch]},
        {"key": "zigen", "label": "字根", "text": f"{ch}（{py}）属丮部。" + body, "cites": [ch]},
        {"key": "xingpang", "label": "形旁與聲旁",
         "text": "形旁定类，声旁取比喻义——象以手持物而拾起、竖起一样。", "cites": [ch]},
        {"key": "hengxiang", "label": "横向比較",
         "text": f"同部相邻者：{heng}；形符各定所附，义由「执持／竖立」两面分张。", "cites": [ch]},
        {"key": "shengmu", "label": "聲母義", "text": sm, "cites": [ch]},
    ]
    cards.append({"char": ch, "pinyin": py, "bus": ["丮部"], "sections": secs,
                  "sources": ["《系統漢語》卷六十三「索」第375部「丮部」", "說文解字", "集韻", "玉篇", "廣韻"]})
    text = "\n\n".join(f"【{s['label']}】{s['text']}" for s in secs)
    claims.append({"id": f"zk-375b-{i:02d}", "node": "hanzi-yinyuan", "topic_id": "topic-zika-shizi",
                   "title": f"{ch}（{py}）丮部字卡：{heng.split('、')[0]}一路",
                   "statement": text,
                   "boundary": f"字卡释字，第375部「丮部」；{ch}依原稿该条训释分属。",
                   "permission": "public", "fact_classes": ["evidence_scope"],
                   "duplicate_resolution": "create_distinct_with_boundary"})

for c in cards:
    json.dump(c, open(os.path.join(ROOT, "web", "public", "cards", c["char"] + ".json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
print("cards", len(claims))

draft = {"schema_version": 1, "intent": "字卡375丮部孰埶10字 2026-10-23", "risk": "medium", "claims": claims}
path = os.path.join(ROOT, "intake", "20261023-字卡375丮部乙.json")
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
