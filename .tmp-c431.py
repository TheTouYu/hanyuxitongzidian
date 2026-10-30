import json,subprocess,os,glob
BJ=("【406 畟部】部首畟（𤰯cè、稷jì）：据「稷」的甲骨文，「畟」与「祝」所从或同，象人下跪祷告之状（《古文字类编》以为「貺」，赐也与也）；小篆从「田」，实即「稷」。"
    "稷为五谷之长（《说文》「𪗉也，五穀之長」），今称糜子、甜高粱。轉義：生长期短、最早收获故为五谷之长，引申五谷总名、谷神（《字彙》「穀神」）；莖高穗长不能直立→偏斜（昃）；莖稈挺→挺拔有力（畟畟，耜利也）；谷粒小→小。"
    "辯證：战国古文讹将跪跽之形写作「夊」，故《说文》「治稼畟畟進也，从田、人，从夊」析形不确。音源：借音字，因偏斜义同「仄」，因粒小义同「即」。字族衍义：①指稷 ②指稷莖表示劲挺 ③指稷實表示小。")
N="字形：古文字字形库未收；原稿有「▲稷」「▲中國水松（頻危物種）」可参。"
D=[
("畟","cè",BJ,N,"《说文》「治稼畟畟進也」；《广韵》「畟畟，陳器狀」；《集韵》「畟畟，耜利也」——形容器陈齐整、耒耜锋利。","部头本字：以「田」定其域，从跪人之形示治稼。","c「刺持」取「刺」：耜刺入土。"),
("稷","jì",BJ,N,"《说文》「𪗉也，五穀之長」——糜子、甜高粱；《广韵》「五穀之揔名」；又谷神（《字彙》「穀神」）。","主组①之稷：以「禾」定其类，畟声。","j「聚决」取「聚」：粒聚成穗。"),
("禝","jì",BJ,N,"《集韵》「堯臣能播五穀，有功于民，祀之，通作稷」——后稷，谷神。","主组①之祀：以「示」定其礼，稷为谷神。","j「聚决」取「决」：祭而决之。"),
("㮨","jì",BJ,N,"《说文》「細理木也，从木畟聲」——水松（《玉篇》「似松，有刺細理」）。","枝组②之木：以「木」定其类，稷莖劲挺。","j「聚决」取「聚」：木聚而理细。"),
("謖","sù",BJ,N,"《尔雅·释言》「起也」；《世说新语》「謖謖如勁松」——峻挺貌；又謖然，翕敛貌。","枝组②之言：以「言」定其动，挺而起。","s「失收」取「收」：言收而敛。"),
("𠞅","jī",BJ,N,"《集韵》「畟，畟畟，耜利也，或从耒、从刀」——耒耜锋利入土。","枝组②之刀：以「刀」定其利，刺土之锋。","j「聚决」取「决」：刃决土开。"),
("𢱩","sù",BJ,N,"《集韵》「㩋，擊也，或作𢱩」——击打。","枝组②之手：以「手」定其击，劲而击之。","s「失收」取「收」：收手而击。"),
("𦃩","sù",BJ,N,"《字海》「勁拔有力的樣子」。","枝组②之丝：以「糸」定其状，紧劲之丝。","s「失收」取「收」：丝收而劲。"),
("溭","zé",BJ,N,"《玉篇》「波也」；《广韵》「溭淢，水勢」；《集韵》「溭淢，奔湍」——水势奔涌。","枝组②之水：以「水」定其势，劲涌之波。","z「凿总」取「凿」：水凿而涌。"),
("㹄","jì",BJ,N,"《集韵》「牛名，犤也」；《本草纲目》「廣南有㹄牛，即果下牛，形最卑小」。","实组③之牛：以「牛」定其类，小如稷粒。","j「聚决」取「聚」：小牛聚群。"),
("𤠎","jí",BJ,N,"《玉篇》「犬生三子」——一胎三犬。","实组③之犬：以「犬」定其类，小犬多子。","j「聚决」取「聚」：犬聚而多。"),
("𠋻","jī",BJ,N,"《集韵》「節力切，音積，小也」。","实组③之人：以「人」定其形，小小之人。","j「聚决」取「聚」：小聚之形。"),
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
ST={"畟":"《说文》「治稼畟畟進也」；《集韵》「畟畟，耜利也」——耒耜锋利入土。","稷":"《说文》「𪗉也，五穀之長」——糜子、甜高粱；又五谷总名、谷神。","禝":"《集韵》「堯臣能播五穀，有功于民，祀之，通作稷」——后稷。","㮨":"《说文》「細理木也，从木畟聲」——水松。","謖":"《尔雅》「起也」；《世说》「謖謖如勁松」——峻挺貌。","𠞅":"《集韵》「畟畟，耜利也，或从耒、从刀」——锋利入土。","𢱩":"《集韵》「㩋，擊也，或作𢱩」。","𦃩":"《字海》「勁拔有力的樣子」。","溭":"《集韵》「溭淢，奔湍」——水势奔涌。","㹄":"《集韵》「牛名，犤也」；《本草》「果下牛，形最卑小」。","𤠎":"《玉篇》「犬生三子」。","𠋻":"《集韵》「音積，小也」。"}
def B(ch): return "源自《系統漢語》第406部「畟部」（卷六十六 采）；字卡五步规程。"
cl=[{"id":f"bdc-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{d[0]}（字卡）",
   "statement":f"{d[0]}（{d[1]}）：{ST[d[0]]}","boundary":B(d[0]),"permission":"public",
   "fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,d in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡406畟部2026-10-23","risk":"low","claims":cl},
          open(r"intake\20261023-字卡406畟部.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡406畟部.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    b=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",b,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",b,"--apply","--content-hash",h); run("bundle-apply",b,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",b,"err",v.get("errors"))