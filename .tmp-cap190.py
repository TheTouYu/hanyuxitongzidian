import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
for ch in ("㿣","䄦","㿩","䬞","伳","初","刺","副","劫","咺","唐","嘅"):
    d=json.load(io.open(rf"D:\系统汉字\web\public\cards\{ch}.json",encoding="utf-8"))
    g=""
    for k in ("benyi","shiyi"):
        s=[x for x in d["sections"] if x["key"]==k]
        if s: g=(s[0].get("text") or "")[:60]; break
    print(ch,"|",g)