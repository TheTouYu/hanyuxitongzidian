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

BEN = "㚔部部头甲骨文象古代桎梏（捕鸟兽之夹），两竹板捆紧、中撑开，兽足踏中即夹住；后用于拷人手腕；《說文》「从大从𢆉」析形不确，战国古文与「𡴘」形近而同讹作「幸」，今楷「幸」实为五字之混。"

rows = [
 ("㚔", "niè", "㚔本刑具桎梏，只羁押惩罚而非杀头，故亦有幸义；字族多取双手被拘系义，义音同「拘」。",
  "桎梏、夾、拘", "两板夹足，取「夹住不动」一面。"),
 ("執", "zhí", "執（执）从丮从㚔（《說文》「捕罪人也，之入切」），甲骨文象双手被拷、颈或套绳：拘捕、控制、持守。",
  "丮、手、拘", "双手被拷而持，取「夹持」一面。"),
 ("慹", "zhí", "慹从心執聲（《說文》「悑也，之入切」），恐怖、懾服；去声「不動貌」。",
  "心、恐、懾", "被执而心慑，取「拘制」一面。"),
 ("騺", "zhì", "騺从馬執聲（《說文》「馬重貌，陟利切」），马负重难行，如被绊住脚。",
  "馬、絆、重", "马足被絆，取「夹住」一面。"),
 ("摯", "zhì", "摯从手从執（《說文》「握持也，脂利切」），握持攫取；又训「至」；执物为相见之礼（同贄）。",
  "手、握、至", "握手不放，取「握持」一面。"),
 ("𡠗", "zhì", "𡠗从女執聲（《說文》「至也，讀若摯」，《集韻》「同贄」）。",
  "女、至、贄", "至而相执，取「至」一面。"),
 ("墊", "diàn", "墊从土執聲（《說文》「下也，都念切」），下陷、倾塌；《方言》「屋而下曰墊」。",
  "土、陷、塌", "下压而陷，取「压住」一面。"),
 ("蟄", "zhé", "蟄从虫執聲（《說文》「藏也」），虫伏藏不出：蟄伏、驚蟄。",
  "虫、藏、伏", "伏而不动，取「拘藏」一面。"),
 ("圉", "yǔ", "圉从囗㚔（《說文》「囹圄，所以拘罪人」），又养马之地、养马人。",
  "囗、囚、牧", "围而拘之，取「拘禁」一面。"),
]

claims, cards = [], []
for i, (ch, py, body, heng, sm) in enumerate(rows, 1):
    secs = [
        {"key": "bengen", "label": "字根本義", "text": BEN, "cites": [ch]},
        {"key": "zigen", "label": "字根", "text": f"{ch}（{py}）属㚔部。" + body, "cites": [ch]},
        {"key": "xingpang", "label": "形旁與聲旁",
         "text": "形旁定类，声旁「㚔」取比喻义——象被桎梏夹住、动不得一样。", "cites": [ch]},
        {"key": "hengxiang", "label": "横向比較",
         "text": f"以「{ch}」为落点：{heng}；同一「夹持拘系」之象，形符各定落点。", "cites": [ch]},
        {"key": "shengmu", "label": "聲母義", "text": sm, "cites": [ch]},
    ]
    cards.append({"char": ch, "pinyin": py, "bus": ["㚔部"], "sections": secs,
                  "sources": ["《系統漢語》卷六十三「索」第379部「㚔部」", "說文解字", "廣韻", "集韻", "釋名"]})
    text = "\n\n".join(f"【{s['label']}】{s['text']}" for s in secs)
    claims.append({"id": f"zk-379-{i:02d}", "node": "hanzi-yinyuan", "topic_id": "topic-zika-shizi",
                   "title": f"{ch}（{py}）㚔部字卡：{heng.split('、')[0]}之拘",
                   "statement": text,
                   "boundary": f"字卡释字，第379部「㚔部」；{ch}依原稿该条训释属拘押执持一系。",
                   "permission": "public", "fact_classes": ["evidence_scope"],
                   "duplicate_resolution": "create_distinct_with_boundary"})

for c in cards:
    json.dump(c, open(os.path.join(ROOT, "web", "public", "cards", c["char"] + ".json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
print("cards", len(claims))

draft = {"schema_version": 1, "intent": "字卡379㚔部9字 2026-10-23b", "risk": "medium", "claims": claims}
path = os.path.join(ROOT, "intake", "20261023-字卡379㚔b.json")
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
