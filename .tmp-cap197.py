# -*- coding: utf-8 -*-
import io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\prompts\exegesis.md"
t=io.open(p,encoding="utf-8").read()
rule="\n- **补/核一字，先按其声旁（字根）所在的部去搜，不得全库乱搜或只搜一处就下结论**：从卡片的字根/结构与原稿字族清单定出声旁→用 `mulu.md`/`zigen.json` 定该部所在卷与 docx→只在该部段落内找「字头＋拼音＋《…》」正条；找不到再扩到相邻部并写明依据。\n"
if "先按其声旁（字根）所在的部去搜" not in t:
    t=t.rstrip()+"\n"+rule
    io.open(p,"w",encoding="utf-8",newline="\n").write(t); print("rule added")