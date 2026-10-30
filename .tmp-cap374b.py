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

BEN = ("㐁部（第374部）部头：甲骨文象有斜纹的编织品，指席子；引申竹皮、无光；战国后㐁、因相混，㐁只作构件存席形；"
       "音源借音，义音同「簟」。本部「宿」声一系，取席可卷可收之象，故多收缩、捆敛、迫促之义。")

rows = [
 ("鏥", "xiù", "鏥从金宿聲，《集韻》「鐵生衣也，或作銹、鏽」：铁被蚀而生的锈衣。",
  "銹、鏽、蝕", "锈生如皮起皱、层层收附，取「收缩附著」一面。"),
 ("㴼", "sù", "㴼从水宿聲，《類篇》「濕也」；原稿疑本指棉布经水洗而缩紧，即俗所谓「缩水」。",
  "縮、濕、浥", "布入水而缩，正是「卷收」之验，故取收缩一面。"),
 ("䈹", "sǒu", "䈹从竹宿聲，《集韻》引《說文》「炊𥯬也」，或从叜；淘米竹箕，用则米减。",
  "籔、箕、淘", "箕淘则米减，减者收也；形符定其为竹器。"),
 ("䑿", "sù", "䑿从舟宿聲，《方言》「小舸謂之艖，艖謂之艒䑿」：小船。",
  "艖、舸、舟", "小船局促，容膝而已，取「卷迫」一面。"),
 ("𤛝", "suō", "𤛝从牛宿聲，《字彙補》「𢳔（摍），亦作𤛝」；抽引，当指牵牛。",
  "摍、牽、抽", "牵牛而引之，如卷席而抽其篾，取抽引一面。"),
 ("𥀝", "niǔ", "𥀝从皮宿聲，《篇海類編》「女六切，音忸」，义不详；原稿疑指皮肤皱褶。",
  "皺、皮、蹙", "皮皱即收，虽训未定，仍归收缩一系。"),
 ("𨣡", "sù", "𨣡《字彙補》「音義與莤字同」，祭神时用以渗酒的茅草，起过滤作用。",
  "莤、洒、濾", "茅束而渗酒，束者收也，取「束而滤之」一面。"),
 ("𩘰", "sù", "𩘰《玉篇》「風吼」，《集韻》引《廣雅》「風也」，或从宿，训寒风。",
  "颼、寒、風", "寒风使物收缩，故「寒风」即「收」之气象。"),
]

claims, cards = [], []
for i, (ch, py, body, heng, sm) in enumerate(rows, 1):
    secs = [
        {"key": "bengen", "label": "字根本義", "text": BEN, "cites": [ch]},
        {"key": "zigen", "label": "字根", "text": f"{ch}（{py}）属㐁部宿声一系。" + body, "cites": [ch]},
        {"key": "xingpang", "label": "形旁與聲旁",
         "text": "形旁定类，声旁取比喻义——象席子可卷可收、收则形缩一样。", "cites": [ch]},
        {"key": "hengxiang", "label": "横向比較",
         "text": f"同系相邻者：{heng}；形符各定所附之物，义皆由「卷收」一面分张。", "cites": [ch]},
        {"key": "shengmu", "label": "聲母義", "text": sm, "cites": [ch]},
    ]
    cards.append({"char": ch, "pinyin": py, "bus": ["㐁部"], "sections": secs,
                  "sources": ["《系統漢語》卷六十三「索」第374部「㐁部」", "集韻", "玉篇", "方言", "類篇"]})
    text = "\n\n".join(f"【{s['label']}】{s['text']}" for s in secs)
    claims.append({"id": f"zk-374b-{i:02d}", "node": "hanzi-yinyuan", "topic_id": "topic-zika-shizi",
                   "title": f"{ch}（{py}）㐁部字卡：{heng.split('、')[0]}之取象",
                   "statement": text,
                   "boundary": f"字卡释字，属㐁部（第374部）宿声一系；{ch}依原稿该条训释分属。",
                   "permission": "public", "fact_classes": ["evidence_scope"],
                   "duplicate_resolution": "create_distinct_with_boundary"})

for c in cards:
    json.dump(c, open(os.path.join(ROOT, "web", "public", "cards", c["char"] + ".json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
print("cards", len(claims))

draft = {"schema_version": 1, "intent": "字卡374㐁部宿声8字 2026-10-23", "risk": "medium", "claims": claims}
path = os.path.join(ROOT, "intake", "20261023-字卡374㐁部乙.json")
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
