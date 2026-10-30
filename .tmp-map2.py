import json,os
p=r"D:\系统汉字\.tmp-charbu.json"
print("exists",os.path.exists(p))
if os.path.exists(p):
    m=json.load(open(p,encoding="utf-8"))
    print(len(m))
    chars="情慍懼憾懌悔恨怖怯恭恥悉慰慷慨慕憲愆懲憊惕悚惋懣懃愍憫憨懇戀志忠忌忘忍忽怠惟惰意愚慈慧想愁"
    for c in chars:
        print(c, m.get(c,"—"))