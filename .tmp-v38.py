import io,json,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
Z=json.load(io.open(r"D:\系统汉字\web\public\zigen.json",encoding="utf-8"))
print([ (j["no"],j["name"]) for j in Z["juan"] if not j.get("name") or j["no"]<1 or j["no"]>100])
print([j for j in Z["juan"] if j["no"]==100][0]["name"])