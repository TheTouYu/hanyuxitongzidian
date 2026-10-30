import json,io,os,sys,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
p=os.path.join(C,"射.json"); d=json.load(io.open(p,encoding="utf-8"))
for s in d["sections"]:
    if s["key"]=="zizu":
        s["text"]="字族衍義：多指射箭，表示離、棄、速"
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
# 全库：凡 zizu 栏 text 为空而已被剥掉前缀的，不回填；仅修 射
print("射 zizu 恢复原文前缀")