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

BEN = "十部部头象竖置算筹；「直」支从目从十，以十目相交验之而正视，故其族多取「立而正、置而定」之象。"

rows = [
 ("值", "zhí", "值从人直聲，本训措置（《說文》「措也」），又相遇、相当：值遇、价值。",
  "人、置、遇", "人直立而相当，取「正」一面。"),
 ("置", "zhì", "置从网直聲（《說文》「赦也」，一说从网直），安置、设立、弃置。",
  "网、設、安", "立而正之，取「正」一面。"),
 ("植", "zhí", "植从木直聲，户植（门中立柱）也（《說文》「户植也」），引申种植、树立。",
  "木、立、種", "木直立为柱，取「正」一面。"),
 ("稙", "zhí", "稙从禾直聲（《說文》「早種也」），先种而早熟之谷。",
  "禾、早、種", "禾早立而先成，取「正」一面。"),
 ("德", "dé", "德从彳㥁聲（悳），心得于内而行于外：道德、恩德、德性。",
  "彳、心、得", "内得于己而正，取「正」一面。"),
 ("矗", "chù", "矗从三直，高耸直立之貌（《玉篇》「齊也」，《集韻》「直立貌」）。",
  "直、高、立", "三直相叠，取「直立」一面。"),
 ("埴", "zhí", "埴从土直聲（《說文》「黏土也」），可制陶之黏土。",
  "土、黏、陶", "土黏而可植立成器，取「正」一面。"),
 ("特", "tè", "特从牛寺聲，本指公牛（《說文》「朴特，牛父也」），引申独特、专一。",
  "牛、牡、獨", "牡牛独处而立，取「单独」一面。"),
 ("汁", "zhī", "汁从水十聲；原稿指出「汁、什、卙」当从「七」，因古「七、十」形近而混。",
  "水、七、混", "形近借形，非取十义，记作借形。"),
 ("什", "shí", "什从人十聲，《說文》「相什保也」，十家为什、十分之一；亦同「十」。",
  "人、十、伍", "十人相保，取「合」一面。"),
]

claims, cards = [], []
for i, (ch, py, body, heng, sm) in enumerate(rows, 1):
    secs = [
        {"key": "bengen", "label": "字根本義", "text": BEN, "cites": [ch]},
        {"key": "zigen", "label": "字根", "text": f"{ch}（{py}）属十部。" + body, "cites": [ch]},
        {"key": "xingpang", "label": "形旁與聲旁",
         "text": "形旁定类，声旁「十」（或「直」）多取比喻义——象树立而正一样；借形者注明。", "cites": [ch]},
        {"key": "hengxiang", "label": "横向比較",
         "text": f"以「{ch}」为落点：{heng}；同一直立而正之象，形符各定落点。", "cites": [ch]},
        {"key": "shengmu", "label": "聲母義", "text": sm, "cites": [ch]},
    ]
    cards.append({"char": ch, "pinyin": py, "bus": ["十部"], "sections": secs,
                  "sources": ["《系統漢語》卷六十三「索」第378部「十部」", "說文解字", "廣韻", "集韻"]})
    text = "\n\n".join(f"【{s['label']}】{s['text']}" for s in secs)
    claims.append({"id": f"zk-378d-{i:02d}", "node": "hanzi-yinyuan", "topic_id": "topic-zika-shizi",
                   "title": f"{ch}（{py}）十部字卡：{heng.split('、')[0]}之立",
                   "statement": text,
                   "boundary": f"字卡释字，第378部「十部」；{ch}依原稿该条训释属直立置定一系。",
                   "permission": "public", "fact_classes": ["evidence_scope"],
                   "duplicate_resolution": "create_distinct_with_boundary"})

for c in cards:
    json.dump(c, open(os.path.join(ROOT, "web", "public", "cards", c["char"] + ".json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
print("cards", len(claims))

draft = {"schema_version": 1, "intent": "字卡378十部直立系10字 2026-10-23", "risk": "medium", "claims": claims}
path = os.path.join(ROOT, "intake", "20261023-字卡378十丁.json")
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
