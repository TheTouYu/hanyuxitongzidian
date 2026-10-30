# -*- coding: utf-8 -*-
import io,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\prompts\exegesis.md"
t=io.open(p,encoding="utf-8").read()
add=("\n> **字形行归属铁律（2026-10-29 立）**：变体读音段（形如「（…pinyin）：」）里的一串古文字图，"
"是**该部所有字头共用的一行**，必须按紧随图后的字头标签分组：标签「𨑩」前的图归前一字头，"
"「釣（鈟）」前的三图归鈟，行末无标签的归部头。例：29 弔部一行 25 图 = 弔20 + 𨑩2 + 鈟3。"
"逐部成卡时必须把这一行拆给每个有标签的字头，不得只取部头或漏掉族字；否则即「字形图不全」。\n")
if "字形行归属铁律" not in t:
    lines=t.split("\n")
    idx=None
    for i,l in enumerate(lines):
        if l.startswith("#") and "字形" in l: idx=i; break
    if idx is None: t=t.rstrip()+"\n"+add
    else: lines.insert(idx+1,add); t="\n".join(lines)
    io.open(p,"w",encoding="utf-8",newline="\n").write(t)
print("ok")