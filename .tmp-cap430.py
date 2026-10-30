# -*- coding: utf-8 -*-
import io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\prompts\exegesis.md"
t=io.open(p,encoding="utf-8").read()
anchor="## 十六、知识入库（PKC）与授权"
add="""### 15.4 繁简与别名（每卡必写，2026-10-27 主人定为规定）

1. **每张卡建好即写**：`simp`＝该字的简化字（有则必写）；`aliases`＝原文字头括注内的全部异体字＋简化字＋对应繁体（去重、排序）。
2. **索引必须能反查**：重建索引后，用简化字搜一次、用繁体本字搜一次，都要命中同一张卡；搜不到就是没写别名，不许报完成。
3. **索引重建是本条规定的一部分**：改卡 → 重建 `web/public/cards/index.json` → 抽查至少两个简化字（如 颐/显）→ 才可提交、才可回复主人。
4. **不是映射问题的不算漏**：繁简表里有而字头尚未做的繁体字（如 錒、皚），属「字未做」，按逐部推进补，不得当作别名缺失糊过去。

"""
assert anchor in t and "15.4" not in t
t=t.replace(anchor, add+anchor, 1)
io.open(p,"w",encoding="utf-8",newline="\n").write(t)
print("写入 15.4")