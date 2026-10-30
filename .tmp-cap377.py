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

BEN = "芻部部头作「又」（手）持斷艸斷木之形，本義拔草、採枝葉；《說文》析作「象包束艸之形」不確（小篆訛「又」為「包」），楷化又或訛「又」為「丑」。"

rows = [
 ("芻", "chú", "芻（蒭）本义刈草采集，转指牲口草料（《玉篇》「茭草」），再引申幼小（鶵）、席草（石龍芻）。",
  "又、艸、刈", "手持断草，取「抓取刈割」一面。"),
 ("犓", "chú", "犓从牛芻聲（《說文》「以芻莖養牛也，測愚切」），以草喂牛。",
  "牛、芻、養", "以草饲牛，取「草料」一面。"),
 ("騶", "zōu", "騶从馬芻聲（《說文》「廏禦也，側鳩切」），牧马人；去声「馳也」。",
  "馬、牧、馳", "牧者随马食草而行，取「喂养」一面。"),
 ("趨", "qū", "趨从走芻聲（《說文》「走也，七逾切」）；《廣雅》「疾也」、《集韻》「促也」，牛马边吃边走的步态。",
  "走、疾、促", "边走边吃，取「趋走」一面。"),
 ("𨃘", "zōu", "𨃘从足芻聲，《玉篇》「獸足」，《類篇》「獸走也」，《龍龕》「獸跡」。",
  "足、獸、跡", "兽足踏草而行，取「行」一面。"),
 ("搊", "zǒu", "搊从手芻聲，《集韻》「持也」，《六書故》「五指摳㩜也」，抓持拨弄；又摺扇之名。",
  "手、持、撥", "五指收拢抓取，正与部头「手持」同象。"),
 ("媰", "chú", "媰从女芻聲（《說文》「婦人妊身也，側鳩切」），怀孕；去声「好也」。",
  "女、孕、好", "怀妊者腹中如草之萌，取「幼小」一面。"),
 ("鶵", "chú", "鶵从隹芻聲（《說文》「雞子也」，籀从鳥），小鸡。",
  "隹、雛、小", "草料取嫩，故引申幼小，取「嫩小」一面。"),
 ("縐", "zhòu", "縐从糸芻聲（《說文》「絺之細也，側救切，一曰蹴也」），细葛布；又衣不伸展、皱缩。",
  "糸、絺、皺", "细布蹴之而蹙，取「粗糙皱缩」一面。"),
 ("皺", "zhòu", "皺从皮芻聲，《玉篇》「面皺也」，《增韻》「眉攢也」，皮肉蹙缩。",
  "皮、蹙、攢", "皮肉蹙缩，取「皱缩」一面。"),
]

claims, cards = [], []
for i, (ch, py, body, heng, sm) in enumerate(rows, 1):
    secs = [
        {"key": "bengen", "label": "字根本義", "text": BEN, "cites": [ch]},
        {"key": "zigen", "label": "字根", "text": f"{ch}（{py}）属芻部。" + body, "cites": [ch]},
        {"key": "xingpang", "label": "形旁與聲旁",
         "text": "形旁定类，声旁「芻」取比喻义——象手持草茎刈取而归一样；表实义者为象意字。", "cites": [ch]},
        {"key": "hengxiang", "label": "横向比較",
         "text": f"以「{ch}」为落点：{heng}；同一刈草之象，形符各定落点。", "cites": [ch]},
        {"key": "shengmu", "label": "聲母義", "text": sm, "cites": [ch]},
    ]
    cards.append({"char": ch, "pinyin": py, "bus": ["芻部"], "sections": secs,
                  "sources": ["《系統漢語》卷六十三「索」第377部「芻部」", "說文解字", "集韻", "玉篇", "廣韻"]})
    text = "\n\n".join(f"【{s['label']}】{s['text']}" for s in secs)
    claims.append({"id": f"zk-377-{i:02d}", "node": "hanzi-yinyuan", "topic_id": "topic-zika-shizi",
                   "title": f"{ch}（{py}）芻部字卡：{heng.split('、')[0]}之象",
                   "statement": text,
                   "boundary": f"字卡释字，第377部「芻部」；{ch}依原稿该条训释分属喂养、嫩小、皱缩、反芻四支之一。",
                   "permission": "public", "fact_classes": ["evidence_scope"],
                   "duplicate_resolution": "create_distinct_with_boundary"})

for c in cards:
    json.dump(c, open(os.path.join(ROOT, "web", "public", "cards", c["char"] + ".json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
print("cards", len(claims))

draft = {"schema_version": 1, "intent": "字卡377芻部10字 2026-10-23", "risk": "medium", "claims": claims}
path = os.path.join(ROOT, "intake", "20261023-字卡377芻.json")
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
