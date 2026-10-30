import io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\prompts\exegesis.md"
s=io.open(p,encoding="utf-8").read()
add="""
## 字族衍义分组（2026-10-24 主人定）

1. 分组的**标题**、**组数**、**每组所收的字**，一律照录原稿（「①指脂膏，表示光滑、細嫩」之类），不得自拟、改写、合并或拆分。
2. 原文只在字族行列出、未在「字族衍義 ①②③」下明确归组的字，**不得自行塞进某组**；如需列出，另设「未分组」并注明「原稿未归组」。
3. 每行的释义与分析：先引原稿该字正条的《說文》《廣韻》等原文，再写「为何取此义、为何用此形旁」的分析；分析可标（推），但不得改动原稿的分类与释义。
"""
if "## 字族衍义分组" not in s:
    io.open(p,"w",encoding="utf-8",newline="\n").write(s.rstrip()+"\n"+add)
    print("rule added")