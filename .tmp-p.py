import re
p=r"D:\系统汉字\.tmp-c405.py"
t=open(p,encoding="utf-8").read()
t=t.replace("def card(ch,p,a,b,c):","def card(ch,p,Bx,a,b,c):").replace('{"key":"bengen","label":"字根本義","text":B,','{"key":"bengen","label":"字根本義","text":Bx,')
t=t.replace("for ch,p,a,b,c in D:\n    json.dump(card(ch,p,a,b,c)","for ch,p,Bx,a,b,c in D:\n    json.dump(card(ch,p,Bx,a,b,c)")
t=t.replace("for i,(ch,p,a,b,c) in enumerate(D,1):","for i,(ch,p,Bx,a,b,c) in enumerate(D,1):")
open(p,"w",encoding="utf-8").write(t)
print("patched")