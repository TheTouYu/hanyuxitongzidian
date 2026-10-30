import json,subprocess,os,glob
BA=("【才部·才声】部首才（cái）：甲骨文从「一」穿过「▽」（▽指花房），从「一」表示连接花房果蒂与枝茎的花梗。"
    "轉義：花未成先有梗→开始（《集韵》「始也」）；梗承花果、输送养分，细梗而大花重果→才能；连梗采摘易伤枝茎须裁切留梗→剪裁；花谢果熟从蒂先落、残梗后枯→留存。"
    "辯證：小篆省去花房结构，《说文》「艸木之初也」析形不确。音源：借音字，义音同「采」。字族衍义：①以小胜大表才能 ②开始 ③形近「丰、木」之讹。")
BB=("【才部·在声】部首才（cái）：梗承花果，花谢果熟先落梗、残梗后枯，故「在、存」皆从才声表留存。"
    "「在」据西周金文本从「士」才声——「士」指雄性生殖器，「才」指能力，表勃起即交配繁殖之力；转指成年雄性之周期性勃起，故引申存留（《玉篇》「存也、终也、察也、居也」），又作介词表时地情形范围。"
    "辯證：「士」「土」形近，周代晚期讹从土，故《说文》「存也，从土才声」析形不确。字族衍义：指生殖器勃起之状（留存）。")
N="字形：古文字字形库未收；才部原稿有「▲花的结构图」（花梗、花托、子房、花柱、柱头、花药、花丝、花萼、花瓣俱标名）。"
D=[
("䴭","cái",BA,"从麦才声，《说文》「饼𥶶也」昨哉切——酒麴，饼状发酵之块。","主组①之用：以「麦」定其质，麦之才制为麴。","c「刺持」取「持」：麴持其性而发。"),
("䊷","zī",BA,"《集韵》「缁，《说文》帛黑也；《周礼》七入为缁。或作䊷、纯」——七染而成的黑色帛。","主组①之色：以「糸」定其质，才之极染成缁。","z「凿总」取「总」：七入而总其色。"),
("釮","qí",BA,"《字彙》「利也」——锋锐之器用。","主组①之器：以「金」定其质，才之利者为釮。","q「亲缺」取「缺」：刃薄而缺乃利。"),
("𣘥","bì",BA,"《唐韵》「蒲计切，音薛。木名」——木名，不详其状。","主组①之木：以「木」定其类，记名而已。","b「闭剥」取「闭」：木密如闭。"),
("𢲾","bì",BA,"《字彙》「批也」——手批击。","主组①之手：以「手」定其动，批而击之。","b「闭剥」取「剥」：批而剥之。"),
("䞗","cāi",BA,"从走才声，《说文》「疑之，等䞗而去也」仓才切——因猜疑而迟滞以行；《广韵》「起去也」。","主组②之始：以「走」定其动，疑而缓起，正是「始」。","c「刺持」取「刺」：疑生而刺步。"),
("𠮹","cái",BA,"《字海》「全，都」——总括之辞。","主组②之全：声借而义为总括，记其语用。","c「刺持」取「持」：尽持而无遗。"),
("𤿋","què",BA,"《字彙补》「皮皴也」——皮肤开裂。","主组①之皮：以「皮」定其处，才之燥而裂。","q「亲缺」取「缺」：皮缺而裂。"),
("茬","chí",BB,"从艸在声，《说文》「艸貌」仕甾切；《玉篇》「艸盛貌」；chá 今指庄稼收割后留在地里的短茎根，或喻短而硬的毛发。","在族之草：以「艸」定其类，留存之短茎，正是「在」之留。","ch「刺持」取「刺」：茬短而刺手。"),
("𢙮","kàn",BB,"《五音篇海》「苦陷切，音勘。忆也」——忆念、记挂。","在族之心：以「心」定其处，留在心上为忆。","k「口控」取「控」：心中所控而不去。"),
]
def card(ch,p,Bx,a,b,c):
    return {"char":ch,"pinyin":p,"bus":[],"sections":[
      {"key":"bengen","label":"字根本义","text":Bx,"cites":[]},
      {"key":"zigen","label":"字形","text":N,"cites":[]},
      {"key":"xingpang","label":"形旁声旁","text":a,"cites":[]},
      {"key":"hengxiang","label":"横向对照","text":b,"cites":[]},
      {"key":"shengmu","label":"声母义","text":c,"cites":[]}]}
for ch,p,Bx,a,b,c in D:
    json.dump(card(ch,p,Bx,a,b,c),open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("写卡",len(D))
ST={"䴭":"《说文》「饼𥶶也。从麦才声」——酒麴，饼状发酵之块。","䊷":"《集韵》「缁，《说文》帛黑也；《周礼》七入为缁。或作䊷、纯」。","釮":"《字彙》「利也」——锋锐之器用。","𣘥":"《唐韵》「蒲计切，音薛。木名」。","𢲾":"《字彙》「批也」——手批击。","䞗":"《说文》「疑之，等䞗而去也」——因猜疑而迟滞以行；《广韵》「起去也」。","𠮹":"《字海》「全，都」。","𤿋":"《字彙补》「皮皴也」——皮肤开裂。","茬":"《说文》「艸貌，从艸在声」；《玉篇》「艸盛貌」；今指收割后留地的短茎根。","𢙮":"《五音篇海》「苦陷切，音勘。忆也」。"}
cl=[{"id":f"bch-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{d[0]}（字卡）",
   "statement":f"{d[0]}（{d[1]}）：{ST[d[0]]}","boundary":"源自《系統漢語》第400部「才部」（卷六十六 采）；字卡五步规程。","permission":"public",
   "fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,d in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡400才部余10字2026-10-23","risk":"low","claims":cl},
          open(r"intake\20261023-字卡400才部余.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡400才部余.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    b=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",b,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",b,"--apply","--content-hash",h); run("bundle-apply",b,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",b,"err",v.get("errors"))