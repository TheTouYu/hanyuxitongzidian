# -*- coding: utf-8 -*-
import json,io,os,shutil,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
P=r"D:\系统汉字\web\public\glyphs\photos"
idx=json.load(io.open(os.path.join(P,"index.json"),encoding="utf-8")); ph=idx.get("photos") or idx
cap=json.load(io.open(os.path.join(P,"captions.json"),encoding="utf-8")); cm=cap.get("captions") or cap
src=os.path.join(P,"到")
if os.path.isdir(src):
    bak=os.path.join(r"D:\系统汉字\intake","misassigned-到-"+str(len(os.listdir(src))))
    shutil.copytree(src,bak,dirs_exist_ok=True); shutil.rmtree(src)
ph.pop("到",None); cm.pop("到",None)
json.dump({"photos":ph},io.open(os.path.join(P,"index.json"),"w",encoding="utf-8"),ensure_ascii=False)
json.dump({"captions":cm},io.open(os.path.join(P,"captions.json"),"w",encoding="utf-8"),ensure_ascii=False)
print("到 图已移除（备份 intake）")