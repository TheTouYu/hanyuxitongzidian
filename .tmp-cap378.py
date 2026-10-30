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

BEN = "十部部头甲骨文象竖置的算筹，表数字十；十进为用数之极，引申完备、极点、十倍很多；《說文》以「一为东西、ㄧ为南北、四方中央备矣」析形不确，战國古文中间加粗演为一横。"

rows = [
 ("十", "shí", "十象竖置算筹；转完备极点（十全、十足）、十倍很多（十室九空）；音源借音同「丮」（五指并拢）。",
  "算籌、數、完備", "五指并拢为十，取「合」一面。"),
 ("計", "jì", "計从言从十（《說文》「會也，筭也，古詣切」），总计、计算、谋划、考察。",
  "言、算、謀", "以十为计之极，取「总合」一面。"),
 ("叶", "xié", "叶即「協」（《說文》「眾之同和也，从劦从十」），众人齐心；甲骨文从口十声，众口一词；今为「葉」之简化字。",
  "劦、眾、和", "众口合于一，取「合」一面。"),
  "二十、并、合", "两十相并，取「合」一面。"),
  "三十、并、合", "三十相并，取「合」一面。"),
  "四十、并、合", "四十相并，取「合」一面。"),
 ("耴", "zhé", "耴从耳乚声，《說文》「耳垂也」；字族輒、㡇、𢬴等取「附而不脱」之象。",
  "耳、垂、附", "耳垂附于头侧，取「附合」一面。"),
 ("直", "zhí", "直从目从十（《說文》「正見也」），以十目相交验之而正视：正直、径直。",
  "目、正、視", "十目相交而正视，取「合而正」一面。"),
]

claims, cards = [], []
for i, (ch, py, body, heng, sm) in enumerate(rows, 1):
    secs = [
        {"key": "bengen", "label": "字根本義", "text": BEN, "cites": [ch]},
        {"key": "zigen", "label": "字根", "text": f"{ch}（{py}）属十部。" + body, "cites": [ch]},
        {"key": "xingpang", "label": "形旁與聲旁",
         "text": "形旁定类，声旁「十」多取比喻义——象数之满、十指相合一样；表实义者为象意字。", "cites": [ch]},
        {"key": "hengxiang", "label": "横向比較",
         "text": f"以「{ch}」为落点：{heng}；同一「合而成十」之象，形符各定落点。", "cites": [ch]},
        {"key": "shengmu", "label": "聲母義", "text": sm, "cites": [ch]},
    ]
    cards.append({"char": ch, "pinyin": py, "bus": ["十部"], "sections": secs,
                  "sources": ["《系統漢語》卷六十三「索」第378部「十部」", "說文解字", "集韻", "玉篇", "廣韻"]})
    text = "\n\n".join(f"【{s['label']}】{s['text']}" for s in secs)
    claims.append({"id": f"zk-378-{i:02d}", "node": "hanzi-yinyuan", "topic_id": "topic-zika-shizi",
                   "title": f"{ch}（{py}）十部字卡：{heng.split('、')[0]}之象",
                   "statement": text,
                   "boundary": f"字卡释字，第378部「十部」；{ch}依原稿该条训释属「数字十或多」一支。",
                   "permission": "public", "fact_classes": ["evidence_scope"],
                   "duplicate_resolution": "create_distinct_with_boundary"})

for c in cards:
    json.dump(c, open(os.path.join(ROOT, "web", "public", "cards", c["char"] + ".json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
print("cards", len(claims))

draft = {"schema_version": 1, "intent": "字卡378十部5字 2026-10-23b", "risk": "medium", "claims": claims}
path = os.path.join(ROOT, "intake", "20261023-字卡378十b.json")
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

