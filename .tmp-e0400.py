# -*- coding: utf-8 -*-
import io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\prompts\exegesis.md"
t=io.open(p,encoding="utf-8").read()
add=("> **插图配属铁律（2026-10-29）**：一张照片只归它**紧跟其后的那条「▲…」图注**所指的字；"
"图注缺失的，必须人工确认画面内容合该字义（如「槭」＝枫叶）才收，否则不收。"
"严禁按“图上文下”的近邻关系批量塞图——曾把「母女举婴」塞给「䙘」（衣名），即为反例。"
"每部收尾第六查：本新字 photos 只含本字条插图，旧自动兜底图一律清掉。")
if "插图配属铁律" not in t:
    t=t.rstrip()+"\n\n"+add+"\n"
    io.open(p,"w",encoding="utf-8",newline="\n").write(t)
print("ok")