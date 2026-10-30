# -*- coding: utf-8 -*-
import io,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\prompts\exegesis.md"
t=io.open(p,encoding="utf-8").read()
if "句中古文字形" not in t:
    add="""\n### 2.1 句中古文字形（硬性）\n原文句子中间夹有古文字形小图（如《說文》引文里的字形）时，必须把该图按原位插入句中，用 `<img class="gin" src="glyphs/inline/<字>/<栏>/NN.png">`；不得以空字、顿号或删句代替。抽图见 `web/public/glyphs/inline/`。\n"""
    t=t.replace("## 三",add+"\n## 三",1)
    io.open(p,"w",encoding="utf-8",newline="\n").write(t)
print("rule ok")