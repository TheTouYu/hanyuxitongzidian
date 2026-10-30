# -*- coding: utf-8 -*-
import io,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\prompts\exegesis.md"
t=io.open(p,encoding="utf-8").read()
new=("> **字形行归属铁律（2026-10-29 立，含句号分段）**：变体读音段里的一串古文字图是全部字头共用的一行，"
"**以原文的「。」分段**：句号前的图归本段字头，句号后的图归下一段；段末若出现字头标签（如「𨑩」「釣（鈟）」「熾」），该标签即本段字头。"
"例：29 弔部 25 图 = 弔20 + 𨑩2 + 鈟3；31 戠部 14 图 = 戠12 + 熾2（第13、14 图在句号后，属熾）。"
"逐部成卡时必须按段拆给每个字头，不得只取部头或漏族字；否则即「字形图不全」。")
t=re.sub(r"> \*\*字形行归属铁律[^\n]*\n?", new+"\n", t, count=1)
if "含句号分段" not in t:
    t=t.rstrip()+"\n\n"+new+"\n"
io.open(p,"w",encoding="utf-8",newline="\n").write(t)
print("ok")