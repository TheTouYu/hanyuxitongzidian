import io,json,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
old="<div class=\"ch\">${esc(ch)}</div>"
new="<div class=\"ch\">${esc(ch)}${d.simp?`（${esc(d.simp)}）`:''}</div>"
for h in [r"D:\系统汉字\web\public\test.html", r"D:\系统汉字\web\public\index.html"]:
    s=io.open(h,encoding="utf-8").read(); assert old in s, h
    io.open(h,"w",encoding="utf-8",newline="\n").write(s.replace(old,new,1))
C=r"D:\系统汉字\web\public\cards"
M={"軹":"轵","鞵":"鞋","雞":"鸡","谿":"溪","嵠":"嵠","縘":"系","鼷":"鼷","豯":"豯","貕":"貕","謑":"謑","螇":"螇","㜎":"㜎","鸂":"㶉","騱":"騱","𡰄":"𡰄","𥰥":"𥰥","𥉐":"𥉐","傒":"傒","徯":"徯","榽":"榽","蒵":"蒵","㨙":"㨙","膎":"膎","枳":"枳","抧":"抧","疻":"疻","䳅":"䳅","胑":"胑","咫":"咫","䅩":"䅩","伿":"伿","鉙":"鉙","齞":"齞","𣲵":"𣲵","𧲻":"𧲻","只":"只","奚":"奚"}
n=0
for ch,sp in M.items():
    p=os.path.join(C,ch+".json")
    if not os.path.exists(p): continue
    d=json.load(open(p,encoding="utf-8"))
    if sp and sp!=ch:
        d["simp"]=sp; d["trad"]=ch; n+=1
    json.dump(d,open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("simp set",n)