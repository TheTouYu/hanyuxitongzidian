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

BEN = ("素部（第373部）部头：据「傃」「𦅫」的甲骨文，初文从糸从集束，象纱线织成的生帛；"
       "《玉篇》「白緻繒」、《廣韻》「帛也」。轉義：生帛未漂未染，故为白、为本、为不加修饰、为平常。"
       "辯證：戰國古文訛从垂从糸，小篆沿袭，《說文》析形不确。音源：義音同「索」。")

rows = [
 ("𤢘", "sù", "𤢘从犬素聲，《廣韻》「牲白也，亦作素」：祭祀所用白色之牲。",
  "素、犧、牲", "白牲未染，取「本色白」一面。"),
 ("𢍣", "jú", "𢍣即「𦅽」之隶变，《集韻》引《說文》「素屬」，原稿谓本即「索」字。",
  "索、素、𦅽", "素属而通索，取「生帛之属」一面。"),
 ("𩝥", "sù", "𩝥从食素聲，《集韻》「蘇故切，音素，膳徹葷也」：撤去荤腥的素食。",
  "素、蔬、齋", "食去荤而存其素，取「不加修饰」一面。"),
 ("傃", "sù", "傃从人素聲，《集韻》「向也」，又《廣雅》「經也」、《字彙》「循其常分」：平素、经常、遵循。",
  "向、常、循", "常者不改其本色，循者守其旧，皆取「本色不改」一面。"),
 ("嫊", "sù", "嫊从女素聲，《集韻》「女字」，即女子之名用字，无实义可训。",
  "女字、名、字", "专用为女字，取「素」之声而不取其义，属借声之列。"),
 ("溸", "sù", "溸为「㴑」之俗，《正字通》「俗㴑字」，《爾雅·釋水》「逆流而上曰㴑洄」；《字彙》又训「舟中抒水之具」。",
  "㴑、洄、泝", "逆流者循其故道，抒水者去其浊而存其清，皆取本色一面。"),
 ("䛾", "sù", "《集韻》收「䛾」于素部，训「諳也」：凡言语、名物习之既久则熟，故字从言而声沿素；与「愫」之从心者，一外一内，同得「本色见得真」之意。",
  "諳、熟、悉", "熟者习之久而见其本色，取「本色」一面。"),
 ("㨞", "sù", "㨞从手素聲，《集韻》「暗取物也」，《正字通》「俗𢱢字」；暗而能取，正因熟悉。",
  "𢱢、摸、取", "暗中能取，是熟而生巧，仍归「素習」一面。"),
 ("䘘", "yù", "䘘《集韻》「止也，或作御，通作禦」，《正字通》以为讹字；一读 sù，训「淨也」。",
  "御、禦、淨", "此条原稿归「形近字之訛」，取义当以讹形辨之，不另立新义。"),
]

claims, cards = [], []
for i, (ch, py, body, heng, sm) in enumerate(rows, 1):
    secs = [
        {"key": "bengen", "label": "字根本義", "text": BEN, "cites": [ch]},
        {"key": "zigen", "label": "字根", "text": f"{ch}（{py}）属素部。" + body, "cites": [ch]},
        {"key": "xingpang", "label": "形旁與聲旁",
         "text": "形旁定类，声旁「素」取比喻义——象生帛未染、本色尚存一样。", "cites": [ch]},
        {"key": "hengxiang", "label": "横向比較",
         "text": f"同条所系：{heng}；形符别其内外，而「素」义一贯。", "cites": [ch]},
        {"key": "shengmu", "label": "聲母義", "text": sm, "cites": [ch]},
    ]
    cards.append({"char": ch, "pinyin": py, "bus": ["素部"], "sections": secs,
                  "sources": ["《系統漢語》卷六十三「索」第373部「素部」", "集韻", "廣韻", "玉篇", "正字通"]})
    text = "\n\n".join(f"【{s['label']}】{s['text']}" for s in secs)
    claims.append({"id": f"zk-373b-{i:02d}", "node": "hanzi-yinyuan", "topic_id": "topic-zika-shizi",
                   "title": f"{ch}（{py}）素部字卡：{heng.split('、')[0]}一路",
                   "statement": text,
                   "boundary": f"字卡释字，第373部「素部」；{ch}依原稿字族衍义相应各条分属。",
                   "permission": "public", "fact_classes": ["evidence_scope"],
                   "duplicate_resolution": "create_distinct_with_boundary"})

for c in cards:
    json.dump(c, open(os.path.join(ROOT, "web", "public", "cards", c["char"] + ".json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
print("cards", len(cards))

draft = {"schema_version": 1, "intent": "字卡373素部余九字(重拟) 2026-10-23乙", "risk": "medium", "claims": claims}
path = os.path.join(ROOT, "intake", "20261023-字卡373素部乙.json")
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

