import io
# 1) 体例文件加硬规则
p = r"prompts\exegesis.md"
t = io.open(p, encoding="utf-8").read()
add = "- **字形缺则补构件**：本字没有古文字字形时，**必须分别引出其构件**（声符、形符，必要时再下一级）的字形图，逐个说明各构件所象；构件也无字形者，写明「该构件字形库缺，待补」。\n"
if add not in t:
    t = t.replace("- **术语统一**", add + "- **术语统一**", 1)
    io.open(p, "w", encoding="utf-8", newline="\n").write(t); print("exegesis patched")
# 2) 释字方法记一条
p2 = r"memory\HANZI-EXEGESIS.md"
t2 = io.open(p2, encoding="utf-8").read()
line = "\n**构件补形**（2026-10-21 主人定）：凡释字，本字无古文字字形者，必须分别引出其构件（声符、形符）的古文字字形，逐个说明；构件亦缺者写明待补，不得跳过。\n"
if "构件补形" not in t2:
    io.open(p2, "a", encoding="utf-8", newline="\n").write(line); print("exegesis-memory appended")