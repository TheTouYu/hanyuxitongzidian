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

rows = [
 ("𣙻", "zōu", "𣙻从木取聲，《集韻》「草木子聚生」：草木结子成丛。",
  "木、子、叢", "子聚成丛，取「聚集」一面。"),
 ("𧁍", "zǒng", "𧁍即「薻」之古，《字彙補》「作孔切，音總，與薻同，古同藻」。",
  "藻、總、水草", "水藻丛生如束，取「聚」一面。"),
 ("𨎮", "zǎo", "𨎮从車取聲，《集韻》「車飾有華藻也」，苍色饰车。",
  "車、藻、飾", "车饰华藻，文采聚于一车，取「聚」一面。"),
 ("𩋄", "chǒu", "𩋄从韋取聲，《玉篇》「束也」：以皮韦捆束。",
  "韋、束、革", "韦束即收聚，取「束而聚」一面。"),
 ("焣", "chǎo/jù", "焣从火取聲，《篇海》「同炒」；去声读 jù 则同「聚」。",
  "火、炒、聚", "炒者翻聚于锅，取「聚」一面；两读共一形。"),
 ("箃", "zōu", "箃从竹取聲，《集韻》「竹黃也」，《廣韻》「竹柴別名」。",
  "竹、柴、黃", "竹柴聚而成束，取「聚」一面。"),
 ("棷", "zōu", "棷从木取聲，《說文》「木薪也」，砍枝为柴。",
  "木、薪、柴", "枝聚为薪，取「聚」一面。"),
 ("𥪏", "jū", "𥪏从立取聲，《集韻》「佝𥪏，羸也」：瘦弱不能立。",
  "立、羸、弱", "羸弱者身缩而近，取「迫近」一面。"),
 ("𧚥", "cuì", "𧚥从衣取聲，《篇海》「衣遊縫也」：衣上的游缝。",
  "衣、縫、遊", "缝聚而相属，取「聚而属」一面。"),
 ("㻓", "zōu", "㻓从玉取聲，《集韻》「玉文」，《玉篇》「玉名」。",
  "玉、文、名", "玉上纹理聚而成文，取「聚」一面。"),
]

claims, cards = [], []
for i, (ch, py, body, heng, sm) in enumerate(rows, 1):
    secs = [
        {"key": "bengen", "label": "字根本義", "text": "取部部头从耳从又，象手取耳而获；「%s」由「取」之聚义一面分张。" % ch, "cites": [ch]},
        {"key": "zigen", "label": "字根", "text": f"{ch}（{py}）属取部。" + body, "cites": [ch]},
        {"key": "xingpang", "label": "形旁與聲旁",
         "text": "形旁定类，声旁「取」取比喻义——象攫取而聚于一处一样。", "cites": [ch]},
        {"key": "hengxiang", "label": "横向比較",
         "text": f"以「{ch}」为落点：{heng}；形旁别其物类，取声之聚义一贯。", "cites": [ch]},
        {"key": "shengmu", "label": "聲母義", "text": sm, "cites": [ch]},
    ]
    cards.append({"char": ch, "pinyin": py, "bus": ["取部"], "sections": secs,
                  "sources": ["《系統漢語》卷六十三「索」第376部「取部」", "集韻", "玉篇", "廣韻", "篇海"]})
    text = "\n\n".join(f"【{s['label']}】{s['text']}" for s in secs)
    claims.append({"id": f"zk-376c-{i:02d}", "node": "hanzi-yinyuan", "topic_id": "topic-zika-shizi",
                   "title": f"{ch}（{py}）取部字卡：{heng.split('、')[0]}之聚",
                   "statement": text,
                   "boundary": f"字卡释字，第376部「取部」；{ch}依原稿该条训释分属聚集一系。",
                   "permission": "public", "fact_classes": ["evidence_scope"],
                   "duplicate_resolution": "create_distinct_with_boundary"})

for c in cards:
    json.dump(c, open(os.path.join(ROOT, "web", "public", "cards", c["char"] + ".json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
print("cards", len(claims))

draft = {"schema_version": 1, "intent": "字卡376取部聚义10字 2026-10-23", "risk": "medium", "claims": claims}
path = os.path.join(ROOT, "intake", "20261023-字卡376取部丙.json")
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
