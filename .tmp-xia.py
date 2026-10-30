# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
d=json.load(io.open(os.path.join(C,"叚.json"),encoding="utf-8"))
z=[s for s in d["sections"] if s["key"]=="zizu"][0]
g2=z["groups"][1]
if not any(r[0].startswith("碬") for r in g2["rows"]):
    g2["rows"].append(["碬","xiá","石","《說文》：「厲石也。从石叚聲。《春秋傳》曰：『鄭公孫碬字子石。』乎加切。」磨刀石。《玉篇》：「磍碬，高下也。」"])
json.dump(d,io.open(os.path.join(C,"叚.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
card={"char":"碬","pinyin":"xiá","head":"碬","aliases":[],"level":3,"parent":"叚",
 "bus":[{"num":45,"name":"石"}],
 "sections":[
  {"key":"shiyi","label":"释义","text":"碬xiá《說文》：「厲石也。从石叚聲。《春秋傳》曰：『鄭公孫碬字子石。』乎加切。」磨刀石。《玉篇》：「磍碬，高下也。」"},
  {"key":"shengmu","label":"声母拟态","text":"x「续消」取「消」：磨石消去刀刃之鈍（推）。"},
  {"key":"suoshujuan","label":"所属卷","links":[{"ch":"卷七斤","label":"卷七 斤"}]}]}
json.dump(card,io.open(os.path.join(C,"碬.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("ok",len(g2["rows"]))