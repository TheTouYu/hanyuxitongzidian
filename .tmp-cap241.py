import json,io,sys,glob,os,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
pat=re.compile(r"(本義|本义|轉義|转义)\s*[：:]")
hits=0; names=[]
for p in glob.glob(r"D:\系统汉字\web\public\cards\*.json"):
    d=json.load(io.open(p,encoding="utf-8"))
    txt=json.dumps(d,ensure_ascii=False)
    if pat.search(txt):
        hits+=1
        if len(names)<8: names.append(os.path.basename(p))
print("含「本义：」字样卡",hits,names)