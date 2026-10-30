import io, re
p = r"web\server.mjs"
t = io.open(p, encoding="utf-8").read()
if "EXEGESIS_STYLE" in t:
    print("already patched"); raise SystemExit
old = 'const CARD_PROMPT = `你是《系统汉语》字卡的编辑。'
assert old in t, "anchor missing"
new = ('let EXEGESIS_STYLE = "";\n'
       'try {\n'
       '  const { readFileSync } = await import("node:fs");\n'
       '  EXEGESIS_STYLE = readFileSync(new URL("./prompts/exegesis.md", new URL("../", import.meta.url)), "utf8").trim();\n'
       '} catch (e) { EXEGESIS_STYLE = ""; }\n'
       'const CARD_PROMPT = `${EXEGESIS_STYLE ? "【释字回答体例（共用规范，必须照此组织答案）】\\n" + EXEGESIS_STYLE + "\\n\\n" : ""}你是《系统汉语》字卡的编辑。')
t = t.replace(old, new, 1)
io.open(p, "w", encoding="utf-8", newline="\n").write(t)
print("patched")