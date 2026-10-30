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

BEN = "芻部部头作「又」（手）持斷艸斷木之形，本義拔草、採枝葉；楷化或訛「又」為「丑」，俗作「蒭」。四支衍义：喂养、嫩小、皱缩、反芻。"

rows = [
 ("蒭", "chú", "蒭即芻之俗字（《六書正訛》「芻，俗作蒭」），草料。",
  "艸、芻、俗", "俗写增艸以显其类，取「草料」一面。"),
 ("䅳", "chú", "䅳从禾芻聲，《廣韻》「稷穰」，《集韻》「禾穰也」：禾秆。",
  "禾、稈、穰", "禾秆即饲草之属，取「草料」一面。"),
 ("䐢", "zhù", "䐢从肉芻聲，《集韻》「妍也、皺也」，《玉篇》「脯也」，皱缩的干肉。",
  "肉、脯、皺", "风干而蹙缩，取「皱缩」一面。"),
 ("𩌄", "zhōu", "𩌄从韋芻聲，《集韻》「革文蹙也」；又「束也」。",
  "韋、革、蹙", "皮革蹙纹，取「皱缩」一面。"),
 ("𪎪", "zōu", "𪎪《玉篇》「古文黀字」，麻秆。",
  "麻、稈、古", "麻秆可析可饲，取「草料之秆」一面。"),
 ("鄒", "zōu", "鄒从邑芻聲（《說文》「魯縣，古邾國」，側鳩切）；《釋名》「狹小之言也」。",
  "邑、邾、小", "地名借声，而释名训「狭小」，仍从「嫩小」一面来。"),
 ("謅", "zhòu", "謅从言芻聲，《集韻》「小言私授謂之謅」，又「弄言」「私語」。",
  "言、小、私", "私语细碎，取「小」一面。"),
 ("𩱦", "chǎo", "𩱦从𩰲芻聲（《說文》「𤎅也，尺沼切」），俗作「煼」，别作「炒」。",
  "火、熬、炒", "翻炒即反复翻动，取「反芻翻覆」一面。"),
 ("篘", "chōu", "篘从竹芻聲，《玉篇》「酒籠」，《集韻》「漉取酒也」：滤酒竹器。",
  "竹、漉、酒", "漉酒如捋草，取「刈取滤出」一面。"),
 ("㱀", "chǐ", "㱀《唐韻》「與欼同，齧也」，指牛羊鹿反芻，胃中半消化之食返口再嚼。",
  "齧、反芻、嚼", "返口再嚼，正是「反芻」一面的本相。"),
 ("𪕾", "hú", "𪕾《漢典》「𪕱之訛字」，𪖎𪕮，猿类；一说指长鼻猴，亦反芻。",
  "猿、反芻、疑", "同取反芻一象，然字属讹形，取义存疑。"),
 ("𧛸", "zhòu", "𧛸从衣芻聲，《集韻》「側救切，音縐，衣不伸也」。",
  "衣、蹙、伸", "衣皱不伸，取「皱缩」一面。"),
]

claims, cards = [], []
for i, (ch, py, body, heng, sm) in enumerate(rows[:-1], 1):
    secs = [
        {"key": "bengen", "label": "字根本義", "text": BEN, "cites": [ch]},
        {"key": "zigen", "label": "字根", "text": f"{ch}（{py}）属芻部。" + body, "cites": [ch]},
        {"key": "xingpang", "label": "形旁與聲旁",
         "text": "形旁定类，声旁「芻」取比喻义——象手捋草叶而刈取一样。", "cites": [ch]},
        {"key": "hengxiang", "label": "横向比較",
         "text": f"以「{ch}」为落点：{heng}；同一刈草之象，形符各定落点。", "cites": [ch]},
        {"key": "shengmu", "label": "聲母義", "text": sm, "cites": [ch]},
    ]
    cards.append({"char": ch, "pinyin": py, "bus": ["芻部"], "sections": secs,
                  "sources": ["《系統漢語》卷六十三「索」第377部「芻部」", "說文解字", "集韻", "玉篇", "廣韻"]})
    text = "\n\n".join(f"【{s['label']}】{s['text']}" for s in secs)
    claims.append({"id": f"zk-377b-{i:02d}", "node": "hanzi-yinyuan", "topic_id": "topic-zika-shizi",
                   "title": f"{ch}（{py}）芻部字卡：{heng.split('、')[0]}之象",
                   "statement": text,
                   "boundary": f"字卡释字，第377部「芻部」；{ch}依原稿该条训释分属四支衍义之一。",
                   "permission": "public", "fact_classes": ["evidence_scope"],
                   "duplicate_resolution": "create_distinct_with_boundary"})

for c in cards:
    json.dump(c, open(os.path.join(ROOT, "web", "public", "cards", c["char"] + ".json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
print("cards", len(claims))

draft = {"schema_version": 1, "intent": "字卡377芻部后段11字 2026-10-23b", "risk": "medium", "claims": claims}
path = os.path.join(ROOT, "intake", "20261023-字卡377芻乙b.json")
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

