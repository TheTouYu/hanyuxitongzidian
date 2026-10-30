import io,json,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
for ch in ["只","奚","旨","欠"]:
    d=json.load(io.open(rf"D:\系统汉字\web\public\cards\{ch}.json",encoding="utf-8"))
    b=[s for s in d["sections"] if s.get("key")=="benyi"][0]["text"]
    print(ch,"::",b[:100])