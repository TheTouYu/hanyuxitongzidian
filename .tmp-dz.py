import json
p=r"web\public\photo-index.json"; d=json.load(open(p,encoding="utf-8"))
if not any(x["char"]=="冎" for x in d):
    d.append({"char":"冎","file":"卷六十  𦟀.docx","para":79,"w":666,"h":422})
json.dump(d,open(p,"w",encoding="utf-8",newline="\n"),ensure_ascii=False,indent=1)
print("ok")
import io
q=r"prompts\exegesis.md"; t=io.open(q,encoding="utf-8").read()
add=("- **按体例直接贴图，不要问**（2026-10-22 主人定）：五步规程里的字形图与插图，取到即贴、取不到先找；\n"
     "  不得以「要不要贴」「原稿可能没有」为由省略或反问。找不到图时，须先扫该部全节（部标题到下一个部标题），仍无才写明「本部无配图」。\n")
if "按体例直接贴图" not in t:
    t=t.replace("## 二、硬规则","## 二、硬规则\n\n"+add,1)
    io.open(q,"w",encoding="utf-8",newline="\n").write(t); print("rule ok")