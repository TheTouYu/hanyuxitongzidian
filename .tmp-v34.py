# -*- coding: utf-8 -*-
import io,json,subprocess,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
raw=subprocess.run([r"D:\系统汉字\tools\git.cmd","show","HEAD~1:web/public/cards/卷一雞.json"],cwd=r"D:\系统汉字",capture_output=True).stdout.decode("utf-8")
old=json.loads(raw)
g=[s for s in old["sections"] if s.get("key")=="zizu"][0]["groups"][0]
rows=[]; links=[]
for r in g["rows"]:
    # 原： [部首, 第N部, 部名, 说明]
    ch=r[0]; no=r[1]; name=r[2]; note=r[3] if len(r)>3 else ""
    rows.append([ch+"部", no, note]); links.append(ch)
g2={"title":"卷一「雞」所辖七部","note":"","header":["部首","部号","所辖"],"rows":rows,"links":links}
p=r"D:\系统汉字\web\public\cards\卷一雞.json"; d=json.load(io.open(p,encoding="utf-8"))
for s in d["sections"]:
    if s.get("key")=="zizu": s["groups"]=[g2]
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("restored", len(rows))