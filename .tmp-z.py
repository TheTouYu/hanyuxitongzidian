import sys,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
md=open(r"D:\系统汉字\knowledge\hanzi-yinyuan\02z-shengmu-yi.md",encoding="utf-8").read()
i=md.find("零聲母")
print(md[i-50:i+700])