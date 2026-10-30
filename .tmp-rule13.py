# -*- coding: utf-8 -*-
import io,sys,glob
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\prompts\exegesis.md"; t=io.open(p,encoding="utf-8").read()
add="""
## 十三、二级字根与并卡（2026-10-26 主人定：以后类似情况均按此办理）

1. **二级字根与一级同规格**：部内可作声旁之字（如示部之柰、祟、款、祡、市；㠯部之台、氐、矣），立 `level=2`、`parent=本部`，必须六栏齐全（本义／转义／辩证／音源／声母拟态／字族衍义表），字族表只收以该二级字根为声符的字。
2. **并卡**：简化字、异体字与正字共用一张卡。卡头 `head` 照原稿括注写（如「柰（奈）」「艷（豔豓𡤩艳）」），`aliases` 列括号内全部字，索引按 `trad／simp／aliases` 合成别名数组，确保每个写法搜得到；被并掉的旧卡置 `hidden:true`。
3. **每部收尾**：写完该部所有卡后必须重建索引（`.tmp-rel2.py`）、用 `node --check` 校验页面脚本、定向提交（卡＋索引）。
"""
if "十三、二级字根与并卡" not in t:
    t=t.rstrip()+"\n"+add; io.open(p,"w",encoding="utf-8",newline="\n").write(t); print("rule appended")
print("---- 定位第11部 ----")
for f in glob.glob(r"D:\字谱智能体\*.docx"):
    try:
        from docx import Document
        ps=[x.text.strip() for x in Document(f).paragraphs]
    except Exception: continue
    for i,s in enumerate(ps):
        if s.startswith("11.") and "部" in s[:8]:
            print(f.split("\\")[-1], i, s[:30]); print("  next:", " | ".join(x[:22] for x in ps[i+1:i+6] if x)[:200]); break