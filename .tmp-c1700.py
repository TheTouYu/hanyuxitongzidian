# -*- coding: utf-8 -*-
import json, io, os, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
C = r"D:\系统汉字\web\public\cards"
B = [{"num": 20, "name": "次"}]
SZ = "卷三 矢"
R = [
 ("羨（埏）", "xiàn", "羊", "《說文》：「貪欲也。从㳄，从羑省。似面切。」《廣韻》：「餘也。」yán，《集韻》：「埏或作羨。墓道也。」yí，《佩觿》：「江夏地。」"),
 ("䢭", "yàn", "辵", "《說文》：「遮䢭也。从辵羨聲。於線切。」《廣韻》：「行皃。又遮也、移也。」"),
 ("𦅗", "chǎn", "糸", "《說文》：「偏緩也。从糸羨聲。昌善切。」一部分鬆緩。yàn，《篇海》：「纏也。」"),
 ("𠩗（𠩦）", "yì", "厂", "《說文》：「歠也。从㳄厂聲。讀若移。以支切。」飲。《段注》：「厂，抴也。」所从「厂」當為「𠂆」或「乙」，指口水的曳出。"),
 ("𠿢（涎）", "xián", "口", "《篇海》：「與涎同。又去聲，與羨同。」"),
 ("㵪", "xián", "水", "《集韻》：「徐連切，音唌。與㳄同。口液也。」yàn，《集韻》：「延面切，音衍。水溢皃。」"),
]
SM = ["x「续消」取「续」：涎續流而貪羨（推）。", "y「零声母」不系：零聲母，緒論七組未列（照實）。",
      "ch「刺持」取「持」：絲偏緩而鬆持（推）。", "y「零声母」不系：零聲母，緒論七組未列（照實）。",
      "x「续消」取「续」：涎續流（推）。", "x「续消」取「续」：水溢續流（推）。"]
for i, (ch, py, cls, t) in enumerate(R):
    name = ch.split("（")[0]
    al = [x for x in ch[ch.find("（") + 1:ch.find("）")]] if "（" in ch else []
    d = {"char": name, "pinyin": py, "level": 3, "parent": "㳄", "bus": B,
         "sections": [{"key": "shiyi", "label": "释义", "text": t, "cites": []},
                      {"key": "shengmu", "label": "声母拟态", "text": SM[i], "cites": []},
                      {"key": "suoshujuan", "label": "所属卷", "text": "", "links": [{"ch": "卷三矢", "label": SZ}]}]}
    if al:
        d["head"] = ch
        d["aliases"] = al
    json.dump(d, io.open(os.path.join(C, name + ".json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
head = {"char": "㳄", "pinyin": "xián", "level": 2, "parent": "次", "rootLevel": 2, "bus": B,
 "head": "㳄（涎𣳧𣶛𣶜𣶚𣶙）", "aliases": list("涎𣳧𣶛𣶜𣶚𣶙"),
 "sections": [
  {"key": "benyi", "label": "本义", "text": "甲骨文从欠的口部有許多小點。「欠」，象嘴張開形；小點，戰國古文演化作「水」，指唾沫、口水。象意唾沫橫飛的樣子。xián，《集韻》：「涎本字。」", "cites": []},
  {"key": "zhuanyi", "label": "转义", "text": "由垂涎而引申指貪欲。xiàn，《說文》：「慕欲口液也。从欠从水。凡㳄之屬皆从㳄。敘連切。」", "cites": []},
  {"key": "yinyuan", "label": "音源", "text": "本「欠」聲，應屬于《欠部》。為方便比對，附于《次部》。", "cites": []},
  {"key": "shengmu", "label": "声母拟态", "text": "x「续消」取「续」：口水垂而續流，欲滴不斷（推）。", "cites": []},
  {"key": "zizu", "label": "字族衍义", "text": "字族衍義：多指垂涎狀，表示拖曳、溢出", "groups": [
    {"title": "多指垂涎狀，表示拖曳、溢出", "note": "", "rows": [list(r) for r in R]}]},
  {"key": "suoshujuan", "label": "所属卷", "text": "", "links": [{"ch": "卷三矢", "label": SZ}]}]}
json.dump(head, io.open(os.path.join(C, "㳄.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
# 次部头加二级字根链接
p = os.path.join(C, "次.json")
d = json.load(io.open(p, encoding="utf-8"))
if not any(s.get("key") == "erji" for s in d["sections"]):
    idx = [i for i, s in enumerate(d["sections"]) if s["key"] == "zizu"][0]
    d["sections"].insert(idx + 1, {"key": "erji", "label": "本部二级字根", "text": "",
                                   "links": [{"ch": "㳄", "label": "㳄（涎）"}]})
    d["sections"] = [s for s in d["sections"]]
    json.dump(d, io.open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("次部头加二级字根链接")
print("㳄部 1+6 建卡")
