import io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\prompts\exegesis.md"
s=io.open(p,encoding="utf-8").read()
old="3. 每行的释义与分析：先引原稿该字正条的《說文》《廣韻》等原文，再写「为何取此义、为何用此形旁」的分析；分析可标（推），但不得改动原稿的分类与释义。"
new="""3. 分组的标题与其下「指脂膏，表示光滑、細嫩」这类**分类说明不得改动**；但每行的**取义落点不得照搬原文引文**，要用自己的话写三段式分析：①本义是什么 → ②取了声根的哪一面义 → ③形旁定它落在哪一类；推演性的可标（推）。
4. 原稿的《說文》《廣韻》引文只作为释义依据，不搬进落点格；需要原文时放在「释义」栏，不混入分析。"""
if old in s:
    io.open(p,"w",encoding="utf-8",newline="\n").write(s.replace(old,new,1)); print("updated")
else: print("anchor not found")