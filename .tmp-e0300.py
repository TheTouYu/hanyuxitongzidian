# -*- coding: utf-8 -*-
import io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\prompts\exegesis.md"
t=io.open(p,encoding="utf-8").read()
add=("> **行内字形两条铁律（2026-10-29）**：①页面只认占位符：`text` 写 `{{benyi/01.png}}`，该栏加 `\"gdir\":\"inline/<字>\"`；"
"直接写 `<img class=gin …>` 会被转义成源码。②提取时**不得按字节数过滤**：1×1 透明图才算空格（读 PNG IHDR 宽高判断），"
"小到 27×29、仅 211 字节的也是真字形。例：28 弔部本義段有两个行内图——`{{benyi/01.png}}`＝弋（27×29），"
"`{{benyi/02.png}}`＝弔（EMF 转 PNG），分别落在「之形。」后、「即弋；」后。")
if "行内字形两条铁律" not in t:
    t=t.rstrip()+"\n\n"+add+"\n"
    io.open(p,"w",encoding="utf-8",newline="\n").write(t)
print("ok")