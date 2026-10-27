# -*- coding: utf-8 -*-
"""Append 姊妹篇 usage rule to memory/DECISIONS.md."""
import io

P = r"memory\DECISIONS.md"
t = io.open(P, encoding="utf-8").read()
orig = t

block = """
## 2026-10-21 姊妹篇用法（《说物解字》与《系统汉语》）

- **两书是姊妹篇，查字以《系统汉语》为主、以《说物解字》为参考**（主人 m08982）：「《说物解字》跟《系统汉语》本来是姊妹篇，查字时，除以《系统汉语》中的内容为主外，也可以同时用《说物解字》的有关文章作为参考」。故释字、字卡、对外问答一律以《系统汉语》的部次与释读为主证据；《说物解字》的篇目作旁证与补充，引用时照样标 `[clm_…]`，并在出处上写明《说物解字》某卷某篇，不得反过来压过《系统汉语》的说法。
- **落成 Claim**：前言主题「与《系统汉语》的关系」一条已改写，写明「姊妹篇」与主次用法（`clm_B571DE0908621D47124647FAB4`）。
"""

if "## 2026-10-21 姊妹篇用法" in t:
    print("SKIP already present")
else:
    t = t.rstrip("\n") + "\n" + block
    print("APPENDED")

io.open(P, "w", encoding="utf-8", newline="\n").write(t)
print("changed", t != orig, "len", len(t))
