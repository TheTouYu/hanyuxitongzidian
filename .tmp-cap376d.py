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

BEN = "取部部头从耳从又，象手取耳而获；一字兼抓耳、获取、贴耳三象意，故其字族分三条衍义。"

rows = [
 ("聚", "jù", "聚从乑从取（乑为人之三叠），象众人会集，村落也（《說文》「會也……邑落云聚，才句切」）。",
  "乑、人、集", "众人相贴而会，取「贴近相聚」一面。"),
 ("撮", "cuō", "撮从手最聲，取「割耳取一點點」之象意（《說文》「四圭也。一曰兩指撮也」），以两指撮取。",
  "手、圭、量", "以指撮取，取「抓取」一面。"),
 ("冣", "jù/zuì", "冣从宀从取，象将零星之物收聚于屋中（《說文》「積也，才句切」）；《玉篇》「齊也、聚也」。",
  "宀、屋、積", "收聚于屋，取「聚集」一面。"),
 ("驟", "zhòu", "驟从馬聚聲（《說文》「馬疾步也，鉏又切」），马飞驰；《廣雅》「數也」，屡次。",
  "馬、疾、屢", "众人贴近则行促，取「迫近而疾」一面。"),
 ("埾", "jù", "埾从土聚聲（《說文》「土積也」），《篇海》「築也」：积土为墙。",
  "土、積、築", "土聚成垒，取「聚集」一面。"),
 ("藂", "cóng", "藂即「叢」之俗（《唐韻》「俗叢字」）；《集韻》去声「艸稚也」，草初生。",
  "艸、叢、稚", "草初生即丛聚，取「聚」一面。"),
 ("縐", "zhòu", "縐从糸芻聲（《集韻》「縐，絺也。或作𦆜」），有皱纹的细葛布。",
  "糸、絺、皺", "细葛相蹙成纹，取「迫近而蹙」一面。"),
 ("㵵", "zòu", "㵵从水聚聲，《集韻》「水流急也」；去声读 jù 则《篇海》「水聲」。",
  "水、急、聲", "水聚而争流，取「聚而疾」一面。"),
 ("㔌", "zòu", "㔌从刀取聲，《玉篇》「斷也，細切也」；《集韻》「析薪也」。",
  "刀、斷、切", "切割即从整体上取下一块，取「取」一面。"),
 ("䝒", "zhù", "䝒从豕聚聲，《集韻》「牝豕也」，《玉篇》「小母猪」；齊徐以小猪为䝒。",
  "豕、牝、小", "猪群聚而育，取「聚」一面。"),
]

claims, cards = [], []
for i, (ch, py, body, heng, sm) in enumerate(rows, 1):
    secs = [
        {"key": "bengen", "label": "字根本義", "text": BEN, "cites": [ch]},
        {"key": "zigen", "label": "字根", "text": f"{ch}（{py}）属取部（或其分化之聚、最、叢诸支）。" + body, "cites": [ch]},
        {"key": "xingpang", "label": "形旁與聲旁",
         "text": "形旁定其物类，声旁「取」取比喻义——象伸手攫取一样；表实义者则为象意字。", "cites": [ch]},
        {"key": "hengxiang", "label": "横向比較",
         "text": f"以「{ch}」为落点：{heng}；同一「取」义，形符各定落点。", "cites": [ch]},
        {"key": "shengmu", "label": "聲母義", "text": sm, "cites": [ch]},
    ]
    cards.append({"char": ch, "pinyin": py, "bus": ["取部"], "sections": secs,
                  "sources": ["《系統漢語》卷六十三「索」第376部「取部」", "說文解字", "集韻", "玉篇", "廣韻"]})
    text = "\n\n".join(f"【{s['label']}】{s['text']}" for s in secs)
    claims.append({"id": f"zk-376d-{i:02d}", "node": "hanzi-yinyuan", "topic_id": "topic-zika-shizi",
                   "title": f"{ch}（{py}）取部字卡：{heng.split('、')[0]}之取",
                   "statement": text,
                   "boundary": f"字卡释字，第376部「取部」；{ch}依原稿该条训释分属聚/最/叢三支之一。",
                   "permission": "public", "fact_classes": ["evidence_scope"],
                   "duplicate_resolution": "create_distinct_with_boundary"})

for c in cards:
    json.dump(c, open(os.path.join(ROOT, "web", "public", "cards", c["char"] + ".json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
print("cards", len(claims))

draft = {"schema_version": 1, "intent": "字卡376取部聚最叢10字 2026-10-23", "risk": "medium", "claims": claims}
path = os.path.join(ROOT, "intake", "20261023-字卡376取部丁.json")
json.dump(draft, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

rc, out = run(["knowledge-plan", "capture", "--file", path, "--format", "json"])
print("capture rc", rc)
m = re.search(r'"content_hash":\s*"([0-9a-f]{64})"', out)
b = re.search(r'"bundle_id":\s*"(bnd_[0-9a-f]+)"', out)
if not (m and b):
    print(out[-1200:]); raise SystemExit(1)
h, bid = m.group(1), b.group(1)
print("bundle", bid, "hash", h)
for s in (["bundle-approve", bid, "--content-hash", h, "--apply"],
          ["bundle-apply", bid, "--content-hash", h, "--apply"]):
    r, o = run(s); print(s[0], r, '"applied": true' in o)
r, o = run(["rebuild"]); print("rebuild", r)
