import sys,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
md=open(r"D:\系统汉字\knowledge\hanzi-yinyuan\02z-shengmu-yi.md",encoding="utf-8").read()
for m in re.finditer(r"###[^\n]*",md):
    if "零" in m.group(0) or "声" in m.group(0): print(m.group(0)[:80])
i=md.find("零")
print("---", md[i-30:i+420] if i>0 else "no 零")