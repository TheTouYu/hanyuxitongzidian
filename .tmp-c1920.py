# -*- coding: utf-8 -*-
import json, io, os, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
from docx import Document
C = r"D:\系统汉字\web\public\cards"
G = r"D:\系统汉字\web\public\glyphs"
P = os.path.join(G, "photos")
doc = Document(r"D:\字谱智能体\卷三  矢.docx")
parts = doc.part.related_parts
ps = doc.paragraphs
B = [{"num": 24, "name": "射"}]
SZ = "卷三 矢"
# --- 字形 16 形（p716）---
gd = os.path.join(G, "射")
os.makedirs(gd, exist_ok=True)
for f in os.listdir(gd):
    os.remove(os.path.join(gd, f))
n = 0
for el in ps[716]._p.iter():
    for a, v in el.attrib.items():
        if a.endswith("}embed") or a.endswith("}id"):
            try:
                b = parts[v].blob
            except KeyError:
                continue
            if len(b) < 800:
                continue
            ext = ".png" if b[:4] == b"\x89PNG" else ".jpg"
            open(os.path.join(gd, f"{n+1:02d}{ext}"), "wb").write(b)
            n += 1
gi = json.load(io.open(os.path.join(G, "index.json"), encoding="utf-8"))
gm = gi.get("chars") or gi
gm["射"] = {"doc": "卷三 矢", "files": [f"射/{f}" for f in sorted(os.listdir(gd))]}
json.dump({"chars": gm}, io.open(os.path.join(G, "index.json"), "w", encoding="utf-8"), ensure_ascii=False)
# --- 插图：p720 逐鹿中原 ---
ph = json.load(io.open(os.path.join(P, "index.json"), encoding="utf-8"))["photos"]
pm = os.path.join(P, "射")
os.makedirs(pm, exist_ok=True)
cap = ""
for el in ps[720]._p.iter():
    for a, v in el.attrib.items():
        if a.endswith("}embed") or a.endswith("}id"):
            try:
                b = parts[v].blob
            except KeyError:
                continue
            if len(b) > 20000:
                ext = ".png" if b[:4] == b"\x89PNG" else ".jpg"
                open(os.path.join(pm, "01" + ext), "wb").write(b)
                ph["射"] = ["01" + ext]
                cap = "漢畫像磚《逐鹿中原》局部"
json.dump({"photos": ph}, io.open(os.path.join(P, "index.json"), "w", encoding="utf-8"), ensure_ascii=False)
def w(d, name):
    json.dump(d, io.open(os.path.join(C, name + ".json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
head = {"char": "射", "pinyin": "shè", "level": 1, "bus": B, "head": "射（䠶𨈡）", "aliases": ["䠶", "𨈡"],
 "sections": [
  {"key": "benyi", "label": "本义", "text": "本義：象矢在弓弦上欲射出的樣子。或加「又」，用手拉弓射箭的意思。象意射箭。shè，《集韻》：「弓弩發也。或从寸。」", "cites": []},
  {"key": "zhuanyi", "label": "转义", "text": "轉義：由箭的發射而出之狀，比喻指照射、陳述、猜度、投射、離開、厭棄等。《廣韻》：「繹也。」yì，《爾雅》：「厭也。」由射的目的性，引申指猜度。《康典》：「又指物而取曰射。」由射箭而引申指軍事。yè，《集韻》：「僕射，官名。射者，武事。」", "cites": []},
  {"key": "bianzheng", "label": "辩证", "text": "辯證：因戰國文字將「弓」演變成「身」，故或从身从矢或寸，故《說文》：「弓弩發於身而中於遠也。从矢从身。」析形不確。", "cites": []},
  {"key": "yinyuan", "label": "音源", "text": "音源：音源字。源自射箭聲。因「矢」聲本源自射箭，故可歸入《矢部》。", "cites": []},
  {"key": "shengmu", "label": "声母拟态", "text": "sh「失收」取「失」：箭離弦即失手而去（推）。", "cites": []},
  {"key": "zizu", "label": "字族衍义", "text": "字族衍義：多指射箭，表示離、棄、速", "groups": [
    {"title": "", "note": "", "rows": [
      ["謝", "xiè", "言", "《說文》：「辭去也。从言䠶聲。」辭也，絕也。《韻會》：「拜賜曰謝。」"],
      ["榭（𢲌）", "xiè", "木", "《新附》：「臺有屋也。」古指無室的廳堂，也為藏器或講軍習武的處所。"],
      ["㓔", "xiè", "冫", "《集韻》：「祠夜切，音謝。凋也。」"],
      ["塮", "xiè", "土", "指用豬羊等家畜糞便漚成的肥料。"],
      ["㴬", "xiè", "水", "《山海經》：「瞻諸之山，㴬水出焉。」水名。"],
      ["𧎭", "yè", "虫", "《玉篇》：「以謝切。蟲名。」因蜮名射工，加寸作𧎭。"],
      ["𧛼", "xiè", "衣", "《集韻》：「吳人謂衣曰𧛼。」"],
      ["𩘧", "yì", "風", "《龍龕》：「疾風。」"],
      ["𪋧（麝𤚑𤠭）", "xiè", "鹿", "《說文》：「如小麋，臍有香。从鹿䠶聲。」雄麝臍部有香腺，分泌麝香，善跳如射。"]]}]},
  {"key": "suoshujuan", "label": "所属卷", "text": "", "links": [{"ch": "卷三矢", "label": SZ}]}]}
if cap:
    head["captions"] = [cap]
w(head, "射")
rows = [("謝", "xiè", "言", "《說文》：「辭去也。从言䠶聲。」辭也，絕也。"),
        ("榭（𢲌）", "xiè", "木", "《新附》：「臺有屋也。从木䠶聲。」古指無室的廳堂。"),
        ("㓔", "xiè", "冫", "《集韻》：「祠夜切，音謝。凋也。」"),
        ("塮", "xiè", "土", "指用豬羊等家畜糞便漚成的肥料。"),
        ("㴬", "xiè", "水", "《山海經》：「瞻諸之山，㴬水出焉。」水名。"),
        ("𧎭", "yè", "虫", "《玉篇》：「以謝切。蟲名。」"),
        ("𧛼", "xiè", "衣", "《集韻》：「吳人謂衣曰𧛼。」"),
        ("𩘧", "yì", "風", "《龍龕》：「疾風。」"),
        ("𪋧（麝𤚑𤠭）", "xiè", "鹿", "《說文》：「如小麋，臍有香。从鹿䠶聲。」善跳如射。")]
for ch, py, cls, tx in rows:
    nm = ch.split("（")[0]
    al = [x for x in ch[ch.find("（") + 1:ch.find("）")]] if "（" in ch else []
    d = {"char": nm, "pinyin": py, "level": 3, "parent": "射", "bus": B,
         "sections": [{"key": "shiyi", "label": "释义", "text": tx, "cites": []},
                      {"key": "shengmu", "label": "声母拟态", "text": "sh「失收」取「失」：射而禽失，故從射之字多含離去義（推）。", "cites": []},
                      {"key": "suoshujuan", "label": "所属卷", "text": "", "links": [{"ch": "卷三矢", "label": SZ}]}]}
    if al:
        d["head"] = ch
        d["aliases"] = al
    w(d, nm)
print("射部 1+9 卡，字形", n, "插图", bool(cap))
