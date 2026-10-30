import json
d=json.load(open(r"web\public\photo-index.json",encoding="utf-8"))
for x in d:
    if x["char"]=="茛": print(x)