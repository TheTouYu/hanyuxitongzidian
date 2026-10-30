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
 ("趣", "qù/qū/cù", "趣从走取聲，《說文》「疾也，七句切」；又训向（《集韻》「向也」）、促（「促也，或作趨」）；巡夜打更亦作趣。",
  "走、取、趨", "疾与向皆由贴近而生：贴耳则近，近则促，促则疾——取「凑近」一面。"),
 ("諏", "zōu", "諏从言取聲，《說文》「聚謀也，子於切」，聚集而悄悄商议；《玉篇》「問正事也」。",
  "言、謀、聚", "聚而谋者必贴耳低语，取「凑近相聚」一面。"),
 ("齱", "zōu", "齱从齒取聲，《說文》「齵也」，齿偏不正；《集韻》「齒叢生」。",
  "齒、叢、偏", "齿丛生而相迫，取「迫近」一面。"),
 ("棷", "zōu/sǒu", "棷从木取聲，《說文》「木薪也」，砍枝为柴；又通「藪」，聚草、泽。",
  "薪、藪、柴", "枝聚成柴，取「聚集」一面。"),
 ("娵", "jū", "娵从女取聲，《集韻》「美女」，又为星次「娵訾」（营室东壁）。",
  "女、星、美", "女美而近人，取「亲近」一面；星名则借声。"),
 ("鯫", "zōu", "鯫从魚取聲，《說文》「白魚也，士垢切」，头尾皆向上之鱼，亦名鱎；又训小、浅鯫小人貌。",
  "魚、小、淺", "小鱼杂处成群，取「聚而小」一面。"),
 ("𠉧", "jù", "𠉧从人取聲，《集韻》「促也」，《玉篇》「𠉧促也」：局促、狭小。",
  "促、局、狹", "局促者空间既近，取「迫近」一面。"),
 ("𦝒", "tiē", "𦝒从肉取聲，《集韻》「𦛖𦣀，肉動也」，俗作𦛖。",
  "肉、動、貼", "肉动是贴近而颤，取「贴近」一面。"),
 ("鋷", "zuì/niè", "鋷从金取聲，《玉篇》「錐屬也」，又《正字通》以为「銸」之讹，即镊子。",
  "錐、鑷、銸", "锥镊皆以尖取物，取「取」之器用一面。"),
 ("𤭡", "nà", "𤭡从瓦取聲，《廣韻》「𤭧，牡瓦」，房上俯盖之瓦。",
  "瓦、覆、屋", "瓦相覆压而近，取「迫近相覆」一面。"),
]

claims, cards = [], []
for i, (ch, py, body, heng, sm) in enumerate(rows, 1):
    secs = [
        {"key": "bengen", "label": "字根本義", "text": "取部部头从耳从又，象手取耳而获；「%s」即由「取」义之近取一面分张。" % ch, "cites": [ch]},
        {"key": "zigen", "label": "字根", "text": f"{ch}（{py}）属取部。" + body, "cites": [ch]},
        {"key": "xingpang", "label": "形旁與聲旁",
         "text": "形旁定类，声旁「取」取比喻义——象手贴耳而凑近、取得一样。", "cites": [ch]},
        {"key": "hengxiang", "label": "横向比較",
         "text": f"以「{ch}」为落点：{heng}；形旁别其类，取声之义一贯。", "cites": [ch]},
        {"key": "shengmu", "label": "聲母義", "text": sm, "cites": [ch]},
    ]
    cards.append({"char": ch, "pinyin": py, "bus": ["取部"], "sections": secs,
                  "sources": ["《系統漢語》卷六十三「索」第376部「取部」", "說文解字", "集韻", "玉篇", "廣韻"]})
    text = "\n\n".join(f"【{s['label']}】{s['text']}" for s in secs)
    claims.append({"id": f"zk-376b-{i:02d}", "node": "hanzi-yinyuan", "topic_id": "topic-zika-shizi",
                   "title": f"{ch}（{py}）取部字卡：{heng.split('、')[0]}之取象",
                   "statement": text,
                   "boundary": f"字卡释字，第376部「取部」；{ch}依原稿该条训释分属贴耳凑近一系。",
                   "permission": "public", "fact_classes": ["evidence_scope"],
                   "duplicate_resolution": "create_distinct_with_boundary"})

for c in cards:
    json.dump(c, open(os.path.join(ROOT, "web", "public", "cards", c["char"] + ".json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
print("cards", len(claims))

draft = {"schema_version": 1, "intent": "字卡376取部贴耳10字 2026-10-23", "risk": "medium", "claims": claims}
path = os.path.join(ROOT, "intake", "20261023-字卡376取部乙.json")
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
