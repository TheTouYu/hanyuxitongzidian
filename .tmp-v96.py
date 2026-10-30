import io,json,glob,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
empty=[];tot=0
for f in glob.glob(r"D:\系统汉字\web\public\cards\卷*.json"):
    d=json.load(io.open(f,encoding="utf-8")); tot+=1
    if not any(s.get("text") for s in d["sections"] if s.get("label") in ("导语","音源","说物","文化")):
        empty.append(f.split("\\")[-1])
print("卷卡",tot,"无卷首文",len(empty),empty[:4])