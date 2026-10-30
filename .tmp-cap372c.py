# -*- coding: utf-8 -*-
import json, subprocess, sys, os, re

ROOT = r"D:\系统汉字"
PY = os.path.join(ROOT, ".runtime", "venv", "Scripts", "python.exe")
PKC = [PY, os.path.join(ROOT, "tools", "pkc_tmpfix.py")]
ENV = os.environ.copy()
ENV["PATH"] = os.path.join(ROOT, ".runtime", "mingit", "cmd") + os.pathsep + ENV.get("PATH", "")

def run(args):
    p = subprocess.run(PKC + args, cwd=ROOT, capture_output=True, text=True, encoding="utf-8", env=ENV)
    return p.returncode, p.stdout + p.stderr

BEN = ("束部（第372部）部头从木从〇，〇象绳缠，捆散木使聚，《說文》「縛也，書玉切」；"
       "轉義捆束、聚集、控制与事情结束；音源字，源自束縛声，义音同「索」。")

rows = [
 ("遫", "chì", "遫为「慗」之通作，《集韻》引《博雅》「張也」、一曰「開也」；与籀文「速」之遫形同而义别。",
  "慗、張、開", "此条取「收」的反而见义：张、开皆由束而解，故仍在束部收放一系内。"),
 ("駷", "sǒng", "駷从馬束聲，《集韻》「揺馬銜走，或作摗」，即掣动马嚼子催马快跑。",
  "摗、䮟、驅", "掣衔是收紧，催走是收而忽放；取「收」的一面为落点。"),
 ("竦", "sǒng", "竦从立从束，《說文》「敬也，束，自申束也，息拱切」；肅敬，四肢并拢，因义音如「共」。",
  "悚、聳、共", "四肢并拢即自束其身，故「竦」正取「收」；敬在形，不在心。"),
 ("悚", "sǒng", "悚从心束聲，《集韻》引《說文》「懼也」，或作愯、𢥠，通作聳。",
  "愯、聳、懼", "惧则心收气缩，「悚」取收在心上，与觫之收在身相别。"),
 ("踈", "shū", "踈即「疎」之讹、本作「疏」，从疋，《玉篇》「慢也」、《廣韻》「稀踈」、《正字通》「疎字之訛」。",
  "疏、疎、䟽", "稀者间开、慢者弛散，正是「收」之反；此条以反面立义。"),
 ("梀", "sù/yìn", "梀从木束聲，《說文》「短椽也，醜録切」；又赤梀木名可為車輞，去声一读为「束也」。",
  "椽、輞、束", "短椽取束木之短，去声直训「束」；收义两见。"),
 ("敕", "chì", "敕从攴束聲，《說文》「誡也，臿地曰敕，恥力切」；春秋金文从「柬」指木片，故与束形近而讹。",
  "勑、飭、誡", "告誡者以言约束之，正取「收」；攴旁定其动作。"),
 ("藗", "sù", "藗从艸遬聲（遬为籀文速），《說文》「牡茅也，桑穀切」，白茅一类。",
  "蔌、茅、葦", "茅叶丛生相束，故从速而取收；此收在草形。"),
]

claims, cards = [], []
for i, (ch, py, body, heng, sm) in enumerate(rows, 1):
    secs = [
        {"key": "bengen", "label": "字根本義", "text": BEN, "cites": [ch]},
        {"key": "zigen", "label": "字根", "text": f"{ch}（{py}）属束部。" + body, "cites": [ch]},
        {"key": "xingpang", "label": "形旁與聲旁",
         "text": "形旁定类，声旁「束」取比喻义——象被绳索捆紧一样。", "cites": [ch]},
        {"key": "hengxiang", "label": "横向比較",
         "text": f"同部取「束」者：{heng}，诸字形符各定其落点。", "cites": [ch]},
        {"key": "shengmu", "label": "聲母義", "text": sm, "cites": [ch]},
    ]
    cards.append({"char": ch, "pinyin": py, "bus": ["束部"], "sections": secs,
                  "sources": ["《系統漢語》卷六十三「索」第372部「束部」", "說文解字", "集韻", "玉篇", "廣韻"]})
    text = "\n\n".join(f"【{s['label']}】{s['text']}" for s in secs)
    claims.append({"id": f"zk-372b-{i:02d}", "node": "hanzi-yinyuan", "topic_id": "topic-zika-shizi",
                   "title": f"{ch}（{py}）：束部字卡，辨其取义一面",
                   "statement": text,
                   "boundary": f"字卡释字，第372部「束部」；依《系統漢語》卷六十三「索」原文成卡。",
                   "permission": "public", "fact_classes": ["evidence_scope"],
                   "duplicate_resolution": "create_distinct_with_boundary"})

for c in cards:
    json.dump(c, open(os.path.join(ROOT, "web", "public", "cards", c["char"] + ".json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
print("cards", len(cards))

draft = {"schema_version": 1, "intent": "字卡372束部8字丙批 2026-10-22", "risk": "medium", "claims": claims}
path = os.path.join(ROOT, "intake", "20261022-字卡372束部丙.json")
json.dump(draft, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

rc, out = run(["knowledge-plan", "capture", "--file", path, "--format", "json"])
print("capture rc", rc)
m = re.search(r'"content_hash":\s*"([0-9a-f]{64})"', out)
b = re.search(r'"bundle_id":\s*"(bnd_[0-9a-f]+)"', out)
if not (m and b):
    print(out[-1200:]); sys.exit(1)
h, bid = m.group(1), b.group(1)
print("bundle", bid, "hash", h)
for step in (["bundle-approve", bid, "--content-hash", h, "--apply"],
             ["bundle-apply", bid, "--content-hash", h, "--apply"]):
    r, o = run(step)
    print(step[0], r, '"applied": true' in o)
r, o = run(["rebuild"])
print("rebuild", r)
