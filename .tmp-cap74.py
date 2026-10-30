# -*- coding: utf-8 -*-
import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
m={"𢼗":"赦","𤵫":"𤶣","𦊎":"罘"}
for ch,z in m.items():
    p=rf"{C}\{ch}.json"; d=json.load(io.open(p,encoding="utf-8"))
    for s in d["sections"]:
        if s["key"]=="ezhi":
            s["text"]=f"示部字族③组：「形近字『赤、余、不、木』之訛」。本字為「{z}」之訛寫，原稿組名與《龍龕》《正字通》皆明言「{ch}，俗；{z}，正」。" 
    json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("ok")