import sys,json,glob,collections
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
ROOT=r"D:\系统汉字"
tot=0;miss=0;nopy=0;pend=0;short=0
for fp in glob.glob(ROOT+r"\web\public\cards\*.json"):
    d=json.load(open(fp,encoding="utf-8")); tot+=1
    ks={s["key"]:s["text"] for s in d["sections"]}
    if not {"bengen","zigen","xingpang","hengxiang","shengmu"}<=set(ks): miss+=1
    if not d.get("pinyin"): nopy+=1
    if any("待補" in t or "待按" in t for t in ks.values()): pend+=1
    if any(len(t)<8 for t in ks.values()): short+=1
print("总卡",tot,"缺栏",miss,"空拼音",nopy,"含待补",pend,"短文本",short)