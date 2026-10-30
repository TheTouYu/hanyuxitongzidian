import io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\prompts\exegesis.md"; t=io.open(p,encoding="utf-8").read()
if "空组不列" not in t:
    t=t.replace("### 7.1","### 7.1 空组不列（硬性）\n原稿某组一个可列字都没有（或该组原稿未列具体字）时，整组不列，不得留下只有标题和表头的空表。\n\n### 7.1",1) if "### 7.1" in t else t+"\n\n## 7.1 空组不列\n原稿某组无具体字时整组不列。\n"
    io.open(p,"w",encoding="utf-8",newline="\n").write(t)
print("rule ok")