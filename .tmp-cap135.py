# -*- coding: utf-8 -*-
import io,re,sys,glob,json
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\prompts\exegesis.md"; s=io.open(p,encoding="utf-8").read()
rule="""
### 声母拟态的推导规矩（2026-10-26 主人定，一律照此）

1. **先定取哪一面**：绪论每组拟态义都是相对两面（如 zh「凿总」、x「续消」）。写卡时必须明写「取『X』」，不得把整组照抄当成结论（反例：「zh取凿总：刺凿而总」「x取续消：水續而消」）。
2. **必须落到该字所指之物的具体特点**：写成可检验的物性/行为链——枳取 zh「凿」，因枳枝有刺、扎刺人；谿（溪）取 x「续」，因溪流潺潺不断、续而不绝。凡只能写出抽象凑句（「刺凿而总」「水續而消」），即为未完成。
3. **不得以组名当解释**：组名只是取义方向，不是释义本身；一句话读不出所释之物的特点，就退回重写。
4. **不合则换面或标注**：一面讲不通，换另一面；仍不能落到物性者标「（推）」，不得含糊过关。
5. 一审不过不提交：每批成卡前自查本规矩，抽三条读，读不出物性即重写。
"""
if "声母拟态的推导规矩" not in s:
    s=s.rstrip()+"\n"+rule
    io.open(p,"w",encoding="utf-8",newline="\n").write(s); print("exegesis 已写入规矩")
else: print("已存在")
# 审计现有卡：疑似凑句
bad=[]
for f in glob.glob(r"D:\系统汉字\web\public\cards\*.json"):
    if f.endswith("index.json"): continue
    d=json.load(io.open(f,encoding="utf-8"))
    for x in d.get("sections",[]):
        if x.get("key")=="shengmu":
            t=(x.get("text") or "").strip()
            if not t or re.search(r"而(总|消|聚|决|缺|收)$",t) or ("取「" not in t and "取" in t and len(t)<16):
                bad.append(d["char"])
print("疑似未落到物性的卡:",len(bad),bad[:30])