# -*- coding: utf-8 -*-
import io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\prompts\exegesis.md"
t=io.open(p,encoding="utf-8").read()
add="\n> h 组「豁活」释义（主人 2026-10-29 定）：「豁」＝開豁、裂開、張開（如門戶洞開、皮肉裂開）；「活」＝活動、流動、生機不息。不可把「豁」解作「豁然開朗」的心境或「豁然可辨」的清楚，那是引申的评價义，不是拟态义。\n"
if "h 组「豁活」释义" not in t:
    t=t.rstrip()+"\n"+add
io.open(p,"w",encoding="utf-8",newline="\n").write(t)
print("updated")