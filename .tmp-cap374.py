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

BEN = ("㐁部（第374部）部头：甲骨文象一块有斜纹的编织品，指席子，《廣雅》「席也」；或专指竹席，故引申为竹皮"
       "（《玉篇》「一曰竹上皮」）；席粗而暗，故又训「无光」；辯證：战国以后㐁、因相混，㐁不再单用，"
       "唯作尋、宿、迎等字构件时仍存席形，《說文》依小篆释为「舌皃」不确；音源：借音字，义音同「簟」。")

rows = [
 ("䄼", "tiǎn", "䄼从田㐁聲，《集韻》「鄉名，在濟北蛇丘縣」；原稿疑本指晒谷物用的竹席，地名借其音。",
  "席、簟、畦", "席以承物，义从㐁之席；形符田则示所承者。"),
 ("䇧", "zhì/jī", "䇧从竹㐁聲，《集韻》「以竹補缺」，又《玉篇》「古文箕字」；以竹片补缺口，其竹片如席之篾。",
  "箕、補、篾", "竹篾补缺，正是席之编织法，故取席之竹皮一面。"),
 ("𦭮", "zhì", "𦭮从艸㐁聲，《說文》「以艸補缺，讀若陸，或以為綴，一曰約空也，直例切」。",
  "綴、補、約", "以草补缺如以篾织席，取「编缀补空」一面。"),
 ("𠈇", "sù", "𠈇即「夙」之古字，《集韻》引《說文》「早敬也，从𠃨，持事雖夕不休」；隶作夙。",
  "夙、早、敬", "此字只借㐁之声，义在早敬，不取席义，是为借声。"),
 ("縮", "suō", "縮从糸宿聲，《說文》「亂也，一曰蹴也」；《爾雅》「繩之謂之縮之」，即以绳捆束；《廣韻》「斂也、退也、短也」。",
  "斂、退、短", "席可卷而收，捆束即卷收，故縮取「卷收」一面。"),
 ("摍", "suō", "摍从手宿聲，《說文》「蹴引也」，《廣韻》「抽也」：以足蹴而抽引之。",
  "抽、引、蹴", "抽取如卷席而抽其篾，取「卷而抽之」一面。"),
 ("蹜", "sù", "蹜从足宿聲，《集韻》「足迫也」，《正字通》「行不舉趾也」：脚步局促，抬不起脚。",
  "迫、蹙、跼", "足迫如席之紧卷，取「卷迫」一面。"),
 ("樎", "sù", "樎从木宿聲，《玉篇》「櫪也，養馬器」，《方言》「櫪，梁宋齊楚北燕之間謂之樎」。",
  "櫪、皁、槽", "马槽围木如席之围，取「围合」一面，而形符定其为木器。"),
]

claims, cards = [], []
for i, (ch, py, body, heng, sm) in enumerate(rows, 1):
    secs = [
        {"key": "bengen", "label": "字根本義", "text": BEN, "cites": [ch]},
        {"key": "zigen", "label": "字根", "text": f"{ch}（{py}）属㐁部。" + body, "cites": [ch]},
        {"key": "xingpang", "label": "形旁與聲旁",
         "text": "形旁定类，声旁「㐁」取比喻义——象一张编织的席子一样（可卷可铺、竹皮粗暗）。", "cites": [ch]},
        {"key": "hengxiang", "label": "横向比較",
         "text": f"同部相邻者：{heng}；形符各定所附之物，义则由「席」之某面分张。", "cites": [ch]},
        {"key": "shengmu", "label": "聲母義", "text": sm, "cites": [ch]},
    ]
    cards.append({"char": ch, "pinyin": py, "bus": ["㐁部"], "sections": secs,
                  "sources": ["《系統漢語》卷六十三「索」第374部「㐁部」", "說文解字", "集韻", "玉篇", "廣韻"]})
    text = "\n\n".join(f"【{s['label']}】{s['text']}" for s in secs)
    claims.append({"id": f"zk-374-{i:02d}", "node": "hanzi-yinyuan", "topic_id": "topic-zika-shizi",
                   "title": f"{ch}（{py}）㐁部字卡：{heng.split('、')[0]}之取象",
                   "statement": text,
                   "boundary": f"字卡释字，第374部「㐁部」；{ch}依原稿该条训释分属。",
                   "permission": "public", "fact_classes": ["evidence_scope"],
                   "duplicate_resolution": "create_distinct_with_boundary"})

for c in cards:
    json.dump(c, open(os.path.join(ROOT, "web", "public", "cards", c["char"] + ".json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
print("cards", len(claims))

draft = {"schema_version": 1, "intent": "字卡374㐁部首8字 2026-10-23", "risk": "medium", "claims": claims}
path = os.path.join(ROOT, "intake", "20261023-字卡374㐁部.json")
json.dump(draft, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

rc, out = run(["knowledge-plan", "capture", "--file", path, "--format", "json"])
print("capture rc", rc)
m = re.search(r'"content_hash":\s*"([0-9a-f]{64})"', out)
b = re.search(r'"bundle_id":\s*"(bnd_[0-9a-f]+)"', out)
if not (m and b):
    print(out[-1000:]); raise SystemExit(1)
h, bid = m.group(1), b.group(1)
print("bundle", bid, "hash", h)
for s in (["bundle-approve", bid, "--content-hash", h, "--apply"],
          ["bundle-apply", bid, "--content-hash", h, "--apply"]):
    r, o = run(s); print(s[0], r, '"applied": true' in o)
r, o = run(["rebuild"]); print("rebuild", r)
