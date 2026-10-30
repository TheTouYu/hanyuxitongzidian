import json,subprocess,os,glob
BS=("【407 足部·歮（二级）】歮（歰𣥒sè）：「歮」与「步」同源——「步」两足故可视作独体，「止」的三叠为歮、四叠为歰，止指脚印、叠体表示极致，象意行走难、脚印杂乱（《字彙補》「歮，與澀同」）。"
    "也可表示快走（分化作奔）、来往次数多（分化作频）。轉義：由行走滞缓→转不动、流不畅、说不顺、咽不下（《玉篇》「難轉也」，《博雅》「吃也」，《六书故》「水涸行艱謂之歰，味苦歰亦謂之歰」）。"
    "辯證：或因「𡿺」古字形楷化后与歮相近而混同（如「𦠊」本脑字）。音源：音源字，源自脚步移动声；因脚步相接而义音同「妾」（《集韵》「歰，與翣同，棺羽飾也」）。字族衍义：①滞缓→不顺畅、受阻、多而杂乱 ②形近「𡿺、惢」之讹。")
N="字形：古文字字形库未收。"
D=[
("歮","sè",BS,N,"止之三叠（步为二叠），象脚印杂乱、行走艰难；《字彙補》「與澀同」；引申不滑、不快。","部头本字：三止相叠，叠体表极致。","s「失收」取「失」：行而不前。"),
("譅","sè",BS,N,"《玉篇》「言甚多也」；《集韵》「譅譶，言不止」；《正字通》「訓語難」——话多而拗口、口吃。","滞涩族①之言：以「言」定其难，语多而滞。","s「失收」取「失」：言失其顺。"),
("澀","sè",BS,N,"《集韵》「歰，《說文》『不滑也』」——不滑溜、不快、语言艰难、道路险阻。","滞涩族①之水：以「水」定其状，水涸行艰。","s「失收」取「失」：水失其流。"),
("𢕬","sà",BS,N,"《说文》「行皃，从彳歰聲」；《广韵》「眾行皃」；《集韵》「行不進也」——众人行走之貌、行而不进。","滞涩族①之彳：以「彳」定其行，众行而滞。","s「失收」取「失」：行失其进。"),
("㒊","sè",BS,N,"《玉篇》「不及也」；《广韵》「㒊譶，言不止也」；《广雅》「擾也」——不及、多言、扰乱。","滞涩族①之人：以「人」定其状，言多而行不及。","s「失收」取「失」：人失其及。"),
("䔼","sè",BS,N,"《集韵》「䔼䔼，艸聲」；zé 香菜——草声、香菜。","滞涩族①之艸：以「艸」定其声，风过草涩。","s「失收」取「失」：草失其柔。"),
("𢡉","sè",BS,N,"《集韵》「慳也」——吝啬。","滞涩族①之心：以「心」定其性，吝而不出。","s「失收」取「收」：收而不与。"),
("𣚟","sè",BS,N,"《集韵》「木茂皃」——木茂盛。","滞涩族①之木：以「木」定其形，枝密而滞。","s「失收」取「收」：枝收而密。"),
("𧴎","nǎo",BS,N,"《广韵》「㺁，雌狢」；《集韵》「獸名，似狐善睡」——貉，唯一冬眠的犬科。","讹混族②之豸：以「豸」定其类，善睡不动。","n「纳弄」取「纳」：纳而不出。"),
("㛴","nǎo",BS,N,"《集韵》「㛴，《說文》『有所恨也』，或作惱」——恼恨。","讹混族②之女：以「女」定其情，恨而不平。","n「纳弄」取「纳」：怨纳于心。"),
("匘","nǎo",BS,N,"《集韵》「匘，《說文》『頭𩪦也』」——脑。","讹混族②之匕：以「匕」定其形，囟象脑形。","n「纳弄」取「纳」：脑纳于颅。"),
("蕋","ruǐ",BS,N,"《字彙》「蕊，與蘂同，又草木叢生貌，又聚也」——花蕊、丛聚。","讹混族②之艸：以「艸」定其类，花心丛聚。","r「柔锐」取「柔」：蕊柔而聚。"),
]
def card(ch,p,Bx,Nx,a,b,c):
    return {"char":ch,"pinyin":p,"bus":[],"sections":[
      {"key":"bengen","label":"字根本义","text":Bx,"cites":[]},
      {"key":"zigen","label":"字形","text":Nx,"cites":[]},
      {"key":"xingpang","label":"形旁声旁","text":a,"cites":[]},
      {"key":"hengxiang","label":"横向对照","text":b,"cites":[]},
      {"key":"shengmu","label":"声母义","text":c,"cites":[]}]}
for ch,p,Bx,Nx,a,b,c in D:
    json.dump(card(ch,p,Bx,Nx,a,b,c),open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("写卡",len(D))
ST={"歮":"《字彙補》「歮，與澀同」——止之三叠，象脚印杂乱、行走艰难。","譅":"《玉篇》「言甚多也」；《正字通》「訓語難」——话多而拗口。","澀":"《说文》「不滑也」——不滑溜、语言艰难、道路险阻。","𢕬":"《说文》「行皃，从彳歰聲」；《集韵》「行不進也」。","㒊":"《玉篇》「不及也」；《广韵》「言不止也」。","䔼":"《集韵》「䔼䔼，艸聲」。","𢡉":"《集韵》「慳也」——吝啬。","𣚟":"《集韵》「木茂皃」。","𧴎":"《集韵》「獸名，似狐善睡」——貉。","㛴":"《集韵》「㛴，《說文》『有所恨也』，或作惱」。","匘":"《集韵》「匘，《說文》『頭𩪦也』」——脑。","蕋":"《字彙》「蕊，與蘂同，又草木叢生貌，又聚也」。"}
def B(ch): return "源自《系統漢語》第407部「足部」内二级字根歮部（卷六十七 足）；字卡五步规程。"
cl=[{"id":f"bdj-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{d[0]}（字卡）",
   "statement":f"{d[0]}（{d[1]}）：{ST[d[0]]}","boundary":B(d[0]),"permission":"public",
   "fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,d in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡407歮部2026-10-23","risk":"low","claims":cl},
          open(r"intake\20261023-字卡407歮部.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡407歮部.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    b=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",b,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",b,"--apply","--content-hash",h); run("bundle-apply",b,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",b,"err",v.get("errors"))