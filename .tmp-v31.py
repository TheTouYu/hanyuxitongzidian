# -*- coding: utf-8 -*-
import io,json,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\cards\第一章士.json"; d=json.load(io.open(p,encoding="utf-8"))
rows=[["雞","系","俗称男阴为「雞雞、雞巴」；雞身如阴囊、雞頸如阴茎；雞本「系」声，系、士古通"],
      ["矢","矢／至","古矢、氐可通；鵄从至，至本矢声；士、矢可通（翳本矢声、殪从士声）"],
      ["戈（鵝）","戈","古士、戈可通（戛／拮）"],
      ["隺（鶴）","隺","古士、隺可通（確／硈）"],
      ["斤","斤／氐","古斤、氐可通（祗／祈）"]]
for s in d["sections"]:
    if s.get("key")=="zizu":
        s["label"]="五路音系（章首所列）"
        s["groups"]=[{"title":"字根与所学之物","note":"","header":["字根","类属","说明"],"rows":rows}]
    if s.get("key")=="juan":
        s["label"]="本辖七卷（第1–47部）"
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("章卡表已统一为三列：五路音系(字根/类属/说明)、七卷(卷目/音源/部属)")