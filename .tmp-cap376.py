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

BEN = ("取部（第376部）部头：从耳从又（手），可象意三——以手抓耳表获得（《說文》「捕取也」，引《周禮》「獲者取左耳」，"
       "即猎获割耳计数）；或手贴己耳以听细微，表凭藉、索取；或手贴人耳为传声筒，即「趣」之趋向靠近。"
       "轉義：凡获取、收取、聚集；又由贴近耳而引申短促、快速。音源借音，义音同「九」「束」。")

rows = [
 ("取", "qǔ", "本部部首字：从耳从又，三象意如部头所述；本义捕取、获取。",
  "耳、又、獲", "手取耳而获之，取「取得」一面；本部诸字皆由取义分张。"),
 ("娶", "qǔ", "娶从女从取，取亦声，《說文》「取婦也，七句切」：把女子接过来成亲。",
  "女、取、婚", "婚娶即取，取妇入门，取「取得」一面。"),
 ("掫", "zōu/chōu", "掫从手取聲，《說文》「夜戒守，有所擊，子矦切」，夜巡敲击；又训手取物、持物相著。",
  "守、擊、持", "巡守执击即手持，取「执取」一面。"),
 ("𢮝", "ná", "𢮝为「拏」之俗，《篇海》「相牽引也」，即互相牵扯。",
  "拏、牽、引", "牵引者手取而不放，取「牵取」一面。"),
 ("𣽇", "còng", "𣽇从水取聲，《集韻》引《說文》「小水入大水曰潨」，或作灇、漎，水会合处。",
  "潨、會、匯", "小水入大水，取「聚」一面；聚即取之引申。"),
 ("黀", "zōu", "黀从麻取聲，《說文》「麻䕸也，側鳩切」，麻秆；《廣韻》「聚麻也」。",
  "麻、稈、聚", "麻秆聚而成束，取「聚」一面。"),
 ("菆", "zōu/cuán", "菆从艸取聲，《說文》「麻蒸也，一曰蓐」，麻秆、草席；又训利箭、草丛林聚、积木以殡。",
  "蒸、蓐、叢", "草聚成丛、木积成殡，皆取「聚」一面。"),
 ("郰", "zōu", "郰字从邑而声取，邑者人所聚居；《說文》定为「魯下邑，孔子之鄉」，故后世鄒、鄹、郰三文并行，皆指一地——孔子所生之陬邑，地在鲁。",
  "鄒、邑、鄉", "邑聚而居，取「聚」一面；地名用其声。"),
 ("緅", "zōu", "緅从糸取聲，《說文》新附「帛青赤色」，郑玄谓五入为緅，即黑褐色。",
  "帛、色、爵", "多色相入而聚于一，取「聚」一面。"),
 ("陬", "zōu", "陬从𨸏取聲，《說文》「阪隅也」，山坡一角；《爾雅》「正月為陬」；《廣韻》「聚居」。",
  "隅、角、聚", "山角为众石所聚，取「聚」一面。"),
]

claims, cards = [], []
for i, (ch, py, body, heng, sm) in enumerate(rows, 1):
    secs = [
        {"key": "bengen", "label": "字根本義", "text": "取部部头从耳从又，象手取耳而获；「%s」即由这一「取」义分张而来。" % ch, "cites": [ch]},
        {"key": "zigen", "label": "字根", "text": f"{ch}（{py}）属取部。" + body, "cites": [ch]},
        {"key": "xingpang", "label": "形旁與聲旁",
         "text": "形旁定类，声旁「取」取比喻义——象手抓耳而取得一样。", "cites": [ch]},
        {"key": "hengxiang", "label": "横向比較",
         "text": f"以「{ch}」为落点：{heng}；形旁别其地、其物、其色，取声之义一贯而不相混。", "cites": [ch]},
        {"key": "shengmu", "label": "聲母義", "text": sm, "cites": [ch]},
    ]
    cards.append({"char": ch, "pinyin": py, "bus": ["取部"], "sections": secs,
                  "sources": ["《系統漢語》卷六十三「索」第376部「取部」", "說文解字", "集韻", "玉篇", "廣韻"]})
    text = "\n\n".join(f"【{s['label']}】{s['text']}" for s in secs)
    claims.append({"id": f"zk-376-{i:02d}", "node": "hanzi-yinyuan", "topic_id": "topic-zika-shizi",
                   "title": f"{ch}（{py}）取部字卡：{heng.split('、')[0]}一路",
                   "statement": text,
                   "boundary": f"字卡释字，第376部「取部」；{ch}依原稿该条训释分属。",
                   "permission": "public", "fact_classes": ["evidence_scope"],
                   "duplicate_resolution": "create_distinct_with_boundary"})

for c in cards:
    json.dump(c, open(os.path.join(ROOT, "web", "public", "cards", c["char"] + ".json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
print("cards", len(claims))

draft = {"schema_version": 1, "intent": "字卡376取部十字(三拟) 2026-10-23乙", "risk": "medium", "claims": claims}
path = os.path.join(ROOT, "intake", "20261023-字卡376取部.json")
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


