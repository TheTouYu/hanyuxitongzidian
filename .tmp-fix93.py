# -*- coding: utf-8 -*-
import io,json,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"; Z=json.load(io.open(r"D:\系统汉字\web\public\zigen.json",encoding="utf-8"))
CN="零一二三四五六七八九十"
def cn(n):
    if n<=10: return CN[n]
    if n<20: return "十"+CN[n%10]
    if n<100: return CN[n//10]+"十"+(CN[n%10] if n%10 else "")
    return "一百"
note="本卷与原卷合稿（原稿同文件内承接上一卷），无独立卷首导言，直接列部目。"
for j in Z["juan"]:
    if j["no"] in (56,93):
        nm="卷%s%s"%(cn(j["no"]),j["name"]); p=os.path.join(C,nm+".json"); d=json.load(io.open(p,encoding="utf-8"))
        for s in d["sections"]:
            if s.get("key")=="juanshou": s["text"]=note
        json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); print("fixed",nm)
d=json.load(io.open(os.path.join(C,"卷八虎.json"),encoding="utf-8"))
s=[x for x in d["sections"] if x.get("key")=="juanshou"][0]
print("卷八 卷首:",s["text"][:120].replace("\n"," / "))