import json,io,sys,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
L=json.load(io.open(r"D:\系统汉字\.tmp-left.json",encoding="utf-8"))
for ch in L[:20]:
    d=json.load(io.open(rf"D:\系统汉字\web\public\cards\{ch}.json",encoding="utf-8"))
    sm=[s["text"][:40] for s in d["sections"] if s["key"]=="shengmu"]
    by=[ (s.get("text") or "") for s in d["sections"] if s["key"] in ("benyi","shiyi","bengen")]
    print(ch,d.get("pinyin"),"|",(by[0] if by else "")[:70],"|",sm[0] if sm else "")