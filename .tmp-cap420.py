import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
idx=json.load(io.open(r"D:\系统汉字\web\public\cards\index.json",encoding="utf-8"))
def find(q):
    return [x["c"] for x in idx if x.get("c")==q or q in (x.get("a") or [])]
for q in ("颐","顯","显","長","长","愛","爱","門","门","魚","鱼","龍","龙","頤","𦣞"):
    print(q,find(q))