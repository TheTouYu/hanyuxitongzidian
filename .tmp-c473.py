import json,subprocess,os,glob
BS="【411 之部（原属它部，从止从一）】之＝甲骨文从止（足迹）从一（地面、处所）：有了足迹，意味已经来过、已经到达，故象意往、到（《玉篇》「至也、往也」）。转义：由足的迈出，引申指生出、滋长（《玉篇》「出也」）；不同的动物有不同脚印，故引申指代人或事物的名称；又引申作虚词，表领有、假设、连属、顺承、停顿（《尔雅》「间也」）。辯證：小篆已看不出「止」，与「屮」形近，故《说文》「出也，象艸过屮，枝茎益大，有所之」析形不确。又「㞢」的甲骨文与「之」的小篆形近，后世或混「㞢」作「之」；「㞢」本象木耳、灵芝等菌类的轮廓形，为「芝」之初文（《六书略》「隶作㞢，象芝出地」）。音源：之部本从「止」，因与「㞢」相混故单设部；「㞢」为借音字，附生如「至」。字族衍义：①本从㞢，指灵芝，表示多、好 ②本从之，讹作㞢，表示行走 ③形近「屮、朩」之讹。"
N="字形：古文字字形库未收。"
D=[
("芝","zhī","《说文》「神艸也」；徐锴《系传》作「从艸，㞢声」——灵芝，生于枯木根际，入药；古人以为瑞草，服之可仙；或指芝麻。","灵芝族①之艸：以「艸」定其物，㞢即其轮廓，芝本从㞢不从之。","zh「凿总」取「总」：瑞草总生。"),
("𦐉","chī","《说文》「飞盛貌」——羽翼盛；《类篇》「𦐉𦐉，羽翼盛也」。","灵芝族①之羽：以「羽」定其形，灵芝丛生如羽盛。","ch「刺持」取「持」：羽张而持。"),
("𧥳","shī","《说文》「诗，志也」，古文诗省；《释名》「之也，志之所之也」。","灵芝族①之言：以「言」定其体，疑本从㞢——如芝一般美好。","sh「失收」取「收」：志收于言。"),
("旹","shí","《集韵》「时，古作旹」——四时；一曰伺也、是也。","行走族②之日：以「日」定其时，当是「之」之讹。","sh「失收」取「收」：日行而时收。"),
("妛","chī","《集韵》同「媸」——侮也、痴也、丑也。","行走族②之女：以「女」定其人，形讹而义从媸。","ch「刺持」取「刺」：丑而刺人。"),
("𣢑","xī","《说文》「𣢑𣢑，戏笑貌」；《广韵》「喜笑」——嬉戏讥笑，同「嗤」。","行走族②之欠：以「欠」定其声，张口而笑。","x「续消」取「消」：笑气消出。"),
("徔","cóng","《汉典》「古同從」——随行。","行走族②之彳：以「彳」定其行，随之而往。","c「刺持」取「持」：随持而行。"),
("𠕓","qiāng","《说文》「帱帐之象，从𠔼，㞢其饰也」；《正字通》「峕，𠕓字之讹」。","形讹族③之𠔼：以「𠔼」定其形，㞢为帐饰。","q「亲缺」取「缺」：帐缺而饰。"),
("汖","pìn","《字汇》「分枲皮也」——剥取苧麻茎皮；《字汇补》「此为朩字之讹」。","形讹族③之水：以「水」定其物，沤麻而分皮。","p「拼辟」取「辟」：辟而分皮。"),
]
def card(ch,p,Bx,Nx,a,b,c):
    return {"char":ch,"pinyin":p,"bus":[],"sections":[
      {"key":"bengen","label":"字根本义","text":Bx,"cites":[]},
      {"key":"zigen","label":"字形","text":Nx,"cites":[]},
      {"key":"xingpang","label":"形旁声旁","text":a,"cites":[]},
      {"key":"hengxiang","label":"横向对照","text":b,"cites":[]},
      {"key":"shengmu","label":"声母义","text":c,"cites":[]}]}
b="同取之部「往到而生／灵芝之状」一面，形符各定其落点；故声符给义、形符定落点。"
for ch,p,Bx,a,c in D:
    json.dump(card(ch,p,BS,N,a,b,c),open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("写卡",len(D))
def B(ch): return "源自《系統漢語》第411部「之部」（卷六十七 足）；字卡五步规程。"
cl=[{"id":f"bdc-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{t[0]}（字卡）",
   "statement":f"{t[0]}（{t[1]}）：{t[2]}","boundary":B(t[0]),"permission":"public",
   "fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,t in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡411之部2026-10-23","risk":"low","claims":cl},
          open(r"intake\20261023-字卡411之部.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡411之部.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))