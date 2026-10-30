# -*- coding: utf-8 -*-
import json,copy,sys,io
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
base=json.load(open(rf"{C}\匃.json",encoding="utf-8"))
for v in ["丐","匄"]:
    d=copy.deepcopy(base)
    d["char"]=v; d["trad"]=v; d["simp"]="匃"; d["level"]=1; d["parent"]=""
    for s in d["sections"]:
        if s["key"]=="benyi" and "字源依本字" not in s["text"]:
            s["text"]="字源依本字「匃」（"+v+"為其異體）："+s["text"]
    json.dump(d,open(rf"{C}\{v}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
p=r"D:\系统汉字\prompts\exegesis.md"; s=io.open(p,encoding="utf-8").read()
add="""
## 镜像字（2026-10-24 主人定）

1. **音义全同、仅写法不同**的异体（如匃／丐／匄、尔／爾），一律作**镜像卡**：各字各存一张卡，内容以本字为准，本义栏首句写「字源依本字「匃」（丐為其異體）」；搜索任一写法都能打开同一套内容。
2. 异体而**分属不同字根**者（如蹋／蹹／踏）不作镜像，各按本字立卡。
3. 一简对多繁者各立卡，不镜像。
"""
if "## 镜像字" not in s:
    io.open(p,"w",encoding="utf-8",newline="\n").write(s.rstrip()+"\n"+add)
print("丐/匄 镜像卡建立")