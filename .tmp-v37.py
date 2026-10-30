import io,json,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
idx=json.load(io.open(r"D:\系统汉字\web\public\cards\index.json",encoding="utf-8"))
v=sorted([x["c"] for x in idx if x.get("c","").startswith("卷")])
nums=[]
for c in v:
    m=re.match(r"卷([零一二三四五六七八九十]+)",c)
    nums.append((m.group(1) if m else c, c))
print([x for x in nums if not re.match(r"^(零|一|二|三|四|五|六|七|八|九|十|十一|十二|十三|十四|十五|十六|十七|十八|十九|二十|二十一|二十二|二十三|二十四|二十五|二十六|二十七|二十八|二十九|三十|三十一|三十二|三十三|三十四|三十五|三十六|三十七|三十八|三十九|四十|四十一|四十二|四十三|四十四|四十五|四十六|四十七|四十八|四十九|五十|五十一|五十二|五十三|五十四|五十五|五十六|五十七|五十八|五十九|六十|六十一|六十二|六十三|六十四|六十五|六十六|六十七|六十八|六十九|七十|七十一|七十二|七十三|七十四|七十五|七十六|七十七|七十八|七十九|八十|八十一|八十二|八十三|八十四|八十五|八十六|八十七|八十八|八十九|九十|九十一|九十二|九十三|九十四|九十五|九十六|九十七|九十八|九十九|一百)$",x[0])])
print(len(v), nums[:6], nums[-4:])