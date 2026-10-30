# -*- coding: utf-8 -*-
import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\cards\家.json"; d=json.load(io.open(p,encoding="utf-8"))
ks=[s["key"] for s in d["sections"]]
if "zizu" not in ks:
    d["sections"].append({"key":"zizu","label":"字族衍义（以家为声旁）","text":"","groups":[{"title":"","note":"","rows":[
     ["嫁","jià","女","《說文》「女適人也」；家聲，取「有家（成家）」義"],
     ["稼","jià","禾","《說文》「禾之秀實為稼，莖節為禾。一曰稼，家事也」；家聲，取家事義"],
     ["傢","jiā","人","傢伙；家聲記音"],
     ["鎵","jiā","金","金屬元素 Ga；家聲為音譯字"],
     ["幏","jià","巾","《說文》「南郡蠻夷賨布」；家聲記音"],
     ["榢（架枷）","jià","木","木名，一說即「架」之異體；家聲，取架屋義"],
     ["𢜿","jià","心","《集韻》「心不安也」；家聲，若有所失之意"]]}]})
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("家 字族已加")