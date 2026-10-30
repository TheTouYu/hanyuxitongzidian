# -*- coding: utf-8 -*-
import json, io, os, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
C = r"D:\系统汉字\web\public\cards"
FIX = {
    "㢀": "c「刺持」取「刺」：屋偏出如刺（推）。",
    "刺": "c「刺持」取「刺」：以刀直刺而入（推）。",
    "拺": "c「刺持」取「刺」：馬箠刺馬（推）。",
    "敇": "c「刺持」取「刺」：鞭策刺馬（推）。",
    "蓛": "c「刺持」取「刺」：穀刺混草料（推）。",
    "𧊸": "c「刺持」取「刺」：臭蟲叮刺（推）。",
    "𧧒": "c「刺持」取「刺」：言如針刺（推）。",
    "𧻕": "q「亲缺」取「缺」：側行踮足而缺步（推）。",
}
for ch, t in FIX.items():
    p = os.path.join(C, ch + ".json")
    d = json.load(io.open(p, encoding="utf-8"))
    for s in d["sections"]:
        if s.get("key") == "shengmu":
            s["text"] = t
    json.dump(d, io.open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

CER = {
    "char": "策", "pinyin": "cè", "level": 2, "parent": "朿", "bus": [{"num": 18, "name": "朿"}],
    "sections": [
        {"key": "benyi", "label": "本义", "text": "策cè：从竹朿聲。竹一般無刺，「朿」當指細的竹條，即竹片。戰國時期的中山王壺即从「𣂔」，《集韻》：「析，古作𣂔。」或指竹枝、竹梢。不過，的確有種節上長刺的竹子，不過只生長于嶺南。具體見「箣」。", "cites": []},
        {"key": "zhuanyi", "label": "转义", "text": "竹片或竹枝的用途廣泛，可作鞭笞，故引申指馬鞭。《說文》：「馬箠也。从竹朿聲。楚革切。」由此引申指鞭打、驅使、督促。可作算籌。《廣韻》：「籌也。」《集韻》：「蓍也。」由此引申指謀略、策劃。《廣韻》：「謀也。」可作書簡。《正字通》：「與筴、册通。」可編器具。《集韻》：「小箕曰策。」大的還可作拐杖。《康典》：「金策，錫杖也。見《詩韻輯略》。」或引申指刺。《方言》：「凡草木刺人，北燕、朝鮮之閒謂之策。」", "cites": []},
        {"key": "yinyuan", "label": "音源", "text": "本朿聲。因有簡冊意，而義音同「冊」：《集韻》：「冊，與策通。」", "cites": []},
        {"key": "shengmu", "label": "声母拟态", "text": "c「刺持」取「刺」：竹片削成細尖，可刺可策（推）。", "cites": []},
        {"key": "zizu", "label": "字族衍义", "text": "字族衍義：", "groups": [
            {"title": "①指尖如策", "note": "", "rows": [
                ["箣", "cè", "竹", "《字彙補》「《字學指南》：同策」；晉戴凱之《竹譜》「箣竹，即節上有刺，南人呼竹為箣」"],
                ["鏼", "sè", "金", "《玉篇》「所革切，音梀。鐵槍也」"],
                ["𣽤（洓𩂴）", "sè", "水", "《集韻》「色責切，音㮦。小雨零皃」"]]},
            {"title": "②指刺、擊", "note": "", "rows": [
                ["憡（𢙀）", "cè", "心", "《集韻》「《博雅》：痛也。或省」"],
                ["𢿸", "cè", "攴", "《類篇》「《博雅》：擊也」"]]},
            {"title": "③指策杖", "note": "", "rows": [
                ["㩍（拺）", "cè", "手", "《集韻》「扶也。或省」扶杖"]]}]},
        {"key": "suoshujuan", "label": "所属卷", "text": "", "links": [{"ch": "卷三矢", "label": "卷三 矢"}]}],
    "aliases": list("笧筴筞箣䇲萗䇿𠞁𠞦𠷽𢄆𥫪𥬰𥯻𥮮𥳯𥮫")}
CER["head"] = "策（笧筴筞箣䇲萗䇿𠞁𠞦𠷽𢄆𥫪𥬰𥯻𥮮𥳯𥮫）"
json.dump(CER, io.open(os.path.join(C, "策.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)

FAM = [
 ("箣", "cè", "箣cè《字彙補》：「《字學指南》：同策。」晉戴凱之《竹譜》：「箣竹，即節上有刺，南人呼竹為箣。邕州舊以為城，蠻蜑來侵，竟不能入，即箣竹也。」大簕竹。", "c「刺持」取「刺」：竹節生刺（推）。"),
 ("鏼", "sè", "鏼sè《玉篇》：「所革切，音梀。鐵槍也。」", "s「失收」取「失」：鐵槍刺出即失手之器（推）。"),
 ("𣽤", "sè", "𣽤（洓𩂴）sè《集韻》：「色責切，音㮦。小雨零皃。」", "s「失收」取「收」：雨零而收（推）。"),
 ("憡", "cè", "憡（𢙀）cè《集韻》：「《博雅》：『痛也。』或省。」", "c「刺持」取「刺」：心痛如刺（推）。"),
 ("𢿸", "cè", "𢿸cè《類篇》：「《博雅》：『擊也』。」", "c「刺持」取「刺」：擊如刺下（推）。"),
 ("㩍", "cè", "㩍（拺）cè《集韻》：「扶也。或省。」扶杖。", "c「刺持」取「刺」：杖頭著地如刺（推）。"),
]
for ch, py, t, sm in FAM:
    d = {"char": ch, "pinyin": py, "level": 3, "parent": "策", "bus": [{"num": 18, "name": "朿"}],
         "sections": [{"key": "shiyi", "label": "释义", "text": t, "cites": []},
                      {"key": "shengmu", "label": "声母拟态", "text": sm, "cites": []},
                      {"key": "suoshujuan", "label": "所属卷", "text": "", "links": [{"ch": "卷三矢", "label": "卷三 矢"}]}]}
    json.dump(d, io.open(os.path.join(C, ch + ".json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("fix8", len(FIX), "ce", 1, "fam", len(FAM))
