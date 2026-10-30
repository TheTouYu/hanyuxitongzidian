import json,io,sys,os,glob
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
for p in glob.glob(r"D:\系统汉字\**\尺.json",recursive=True):
    d=json.load(io.open(p,encoding="utf-8"))
    ss=[s for s in d.get("sections",[]) if s.get("key")=="suoshujuan"]
    print(p, "photos" in d, ss)