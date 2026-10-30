import io
p=r"prompts\exegesis.md"; t=io.open(p,encoding="utf-8").read()
add=("- **横向比较的取字范围**（2026-10-22 主人定）：比较只在**同一条「字族衍义」**之下取字——\n"
     "  该条兄弟字多，就只列这一条的字，其它衍义不同的不必列；\n"
     "  该条只有一两个字、比较只是为解释字根本身，则把该部相关诸字全部列出。\n"
     "  总之：比较的范围随「衍义条」走，不随整个字族走。\n")
if "横向比较的取字范围" not in t:
    t=t.replace("## 二、硬规则","## 二、硬规则\n\n"+add,1)
    io.open(p,"w",encoding="utf-8",newline="\n").write(t); print("ok")