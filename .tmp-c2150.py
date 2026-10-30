import io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\prompts\exegesis.md"; t=io.open(p,encoding="utf-8").read()
add="\n## 〇 总则（最高优先）\n除格式（栏位顺序、表格列式、字号样式）按规定外，**一切内容必须遵照原文**：本义、转义、辩证、音源、字族组名与各组收字、释义文字，一律逐字照录，不得概括、改写、补字、删字或自拟说明。\n只有两处允许超出原文：①声母拟态（须落物性并标「（推）」）；②表格的「类属」列（只能取该字形旁或原文用字，不得凭空拟定）。\n"
if "除格式" not in t:
    t=t.rstrip()+"\n"+add
    io.open(p,"w",encoding="utf-8",newline="\n").write(t); print("rule added")