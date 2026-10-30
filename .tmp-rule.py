# -*- coding: utf-8 -*-
import io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\prompts\exegesis.md"
t=io.open(p,encoding="utf-8").read()
rule='''
> **原文不可删省（主人 2026-10-30 严令）**
> 1. 页头必须照录原文括注，如「奪（夺）」「愯（𢥠悚聳）」「篗（𧤽籆籰𧤯䈅）」，一个不省。
> 2. 括注内每一个字（含简化字、或体、同字异体）都要进 `aliases` 并建索引，即使该字另有独立卡（这时允许一搜两卡，以页头括注区分）。
> 3. 不得以「已有独立卡」「避免重复」为由删去括注或别名——宁可重，不可缺。
> 4. 建卡脚本、清洗脚本一律不改写 `head`；只允许补 `aliases`，不允许缩写。
'''
if "原文不可删省" not in t:
    t=t.rstrip()+"\n"+rule
io.open(p,"w",encoding="utf-8",newline="\n").write(t)
print("ok")