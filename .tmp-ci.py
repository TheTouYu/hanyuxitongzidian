import json,os,shutil
p=r"web\public\photo-index.json"
d=json.load(open(p,encoding="utf-8"))
os.makedirs(r"web\public\glyphs\photos\搓",exist_ok=True)
shutil.copy(r"web\public\glyphs\photos\差\01.jpg", r"web\public\glyphs\photos\搓\01.jpg")
for x in d:
    if x["char"]=="搓": break
else:
    d.append({"char":"搓","file":"卷卌二  丵.docx","para":179,"w":1500,"h":1125})
json.dump(d,open(p,"w",encoding="utf-8",newline="\n"),ensure_ascii=False,indent=1)
print("ok",len(d))