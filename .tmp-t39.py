# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
T={
 "隺":["指鶴的棲息于濕地，表示灌溉、漁獲、橋","指鶴狀，表示鶴狀物、高舉","指鶴的相守，表示專一、堅定","指鶴羽，表示白色或黑白相雜"],
 "靃":["指鶴的棲息于濕地，表示水上、水中，或盛水之物","指鶴狀，表示高聲、高舉","指鶴飛，表示翻飛、迅疾、葉大而密","指鶴的相守，表示專一、堅硬","指鶴羽，表示白色、明亮，或黑白相雜"],
}
for ch,titles in T.items():
    p=os.path.join(C,ch+".json"); d=json.load(io.open(p,encoding="utf-8"))
    for s in d["sections"]:
        if s.get("key")=="zizu":
            for i,g in enumerate(s["groups"]):
                if i<len(titles): g["title"]=titles[i]
    json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("titles set")
# checker
chk=r"D:\系统汉字\tools\check-groups.py"
src='''# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\\系统汉字\\web\\public\\cards"
bad=[]
for f in os.listdir(C):
    if not f.endswith(".json") or f in ("index.json","variants.json"): continue
    try: d=json.load(io.open(os.path.join(C,f),encoding="utf-8"))
    except Exception: continue
    for s in d.get("sections",[]):
        if s.get("key")=="zizu":
            for g in s.get("groups",[]):
                if not (g.get("title") or "").strip():
                    bad.append((f,g.get("no","?"),len(g.get("rows",[]))))
print("groups missing title:",len(bad))
for b in bad[:40]: print(b)
'''
io.open(chk,"w",encoding="utf-8",newline="\n").write(src)
print("checker written")