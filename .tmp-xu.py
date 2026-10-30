import sys,json,glob,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
m=json.load(open(r"D:\系统汉字\.tmp-charmap.json",encoding="utf-8"))
print("charmap:",m.get("徐"))
hits=0
for f in glob.glob(r"D:\系统汉字\knowledge\hanzi-yinyuan\*.md"):
    t=open(f,encoding="utf-8").read()
    for blk in re.finditer(r"<!-- CLAIM:START (clm_[0-9A-F]+) -->\s*\n### (.+?)\n([\s\S]*?)#### 适用边界\n\n(.+?)\n", t):
        if "徐" in blk.group(2) or re.search(r"徐（",blk.group(3)):
            print(blk.group(1), "|", blk.group(2)[:80], "|", blk.group(4)[:40]); print("   ", blk.group(3).strip()[:260]); hits+=1
            if hits>=6: break
    if hits>=6: break
t=open(r"D:\系统汉字\knowledge\hanzi-origin\mulu.md",encoding="utf-8").read()
for line in t.splitlines():
    if "余部" in line or "徐部" in line: print("目录:",line[:100])