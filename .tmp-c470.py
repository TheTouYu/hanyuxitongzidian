import json,subprocess,os,glob
BS="【410 此部（原属它部，从勹止声）】此＝从勹（俯伏、背负）从止（脚踏），象意踩在对方背上；是「跐」的初文（《释名》「跐，弭也，足践之使弭服也」，《广雅》「履也」）。转义：由脚下所踩，引申指近处之物（《尔雅》「兹，此也」）；由脚踩引申击打（㧗「拳加人也」）、瘀青（紫「帛青赤色」）；鸟类交尾雌伏于下故引申雌性（雌「鸟母也」），雌性体小故引申短小（啙「短也」）。辯證：「匕、勹」形近多混，《说文》「从止从匕，匕相比次也」析形不确。字族衍义：①踩使勹→相仇相斗、踩踏叠垒 ②殴伤→青、紫色 ③鸟类交尾→雌性、短小。"
N="字形：古文字字形库未收。"
D=[
("眥","zì","《说文》「目匡也」——眼眶；《集韵》「眦睚，恨视」。","踩踏族①之目：以「目」定其物，踩而怒视则眼眶张。","z「凿总」取「凿」：目裂如凿。"),
("𡗼","xiè","《说文》「瞋大也」——瞪大眼睛怒视。","踩踏族①之大：以「大」定其形，怒而目张。","x「续消」取「消」：怒气消不得。"),
("呰","zǐ","《说文》「苛也」——诋毁、口毁；又「些」之语辞。","踩踏族①之口：以「口」定其声，相啄如相踩。","z「凿总」取「凿」：口凿而毁。"),
("訿","zǐ","《说文》「不思称意也」——发牢骚、指责。","踩踏族①之言：以「言」定其声，怨言如踩。","z「凿总」取「凿」：言凿而怨。"),
("㧗","zǐ","《说文》「捽也」——以手击取；《广韵》「拳加人也」。","踩踏族①之手：以「手」定其动，踩之即为击。","z「凿总」取「凿」：手凿而击。"),
("㧘","zì","《说文》「积也」——聚积；又拔颊须、批颊。","踩踏族①之手：以「手」定其聚，叠垒如踩。","z「凿总」取「总」：总聚而积。"),
("齜","chái","《说文》「齿相齗也，一曰开口见齿之皃」——磨牙、龇牙。","踩踏族①之齿：以「齿」定其物，相斗则龇。","ch「刺持」取「刺」：齿刺而出。"),
("𧺼","cǐ","《说文》「浅渡也」——从浅水中走过。","踩踏族①之走：以「走」定其行，踩水而渡。","c「刺持」取「持」：持步而渡。"),
("跐","cǐ","《集韵》「蹈也、蹋也、履也」；《释名》「弭也，足践之使弭服也」——踩、踏。","踩踏族①之足：以「足」定其本，此即跐之初文。","c「刺持」取「刺」：足刺而下。"),
("紪","cī","《集韵》「缇，帛文，或从此」——交错的花纹。","踩踏族①之糸：以「糸」定其物，交错如踩叠。","c「刺持」取「刺」：纹如刺交。"),
("觜","zī","《说文》「鸱旧头上角觜也」——猫头鹰头上的角状毛；又鸟嘴。","踩踏族①之角：以「角」定其形，尖锐如踩。","z「凿总」取「凿」：尖凿而出。"),
("茈","zǐ","《说文》「茈艸也」——紫色的草，代指紫色。","殴伤族②之艸：以「艸」定其物，色青紫如殴伤。","z「凿总」取「总」：草色总聚而紫。"),
]
def card(ch,p,Bx,Nx,a,b,c):
    return {"char":ch,"pinyin":p,"bus":[],"sections":[
      {"key":"bengen","label":"字根本义","text":Bx,"cites":[]},
      {"key":"zigen","label":"字形","text":Nx,"cites":[]},
      {"key":"xingpang","label":"形旁声旁","text":a,"cites":[]},
      {"key":"hengxiang","label":"横向对照","text":b,"cites":[]},
      {"key":"shengmu","label":"声母义","text":c,"cites":[]}]}
b="同取此部「踩踏而下／殴伤而紫」一面，形符各定其落点；故声符给义、形符定落点。"
for ch,p,Bx,a,c in D:
    json.dump(card(ch,p,BS,N,a,b,c),open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("写卡",len(D))
def B(ch): return "源自《系統漢語》第410部「此部」（卷六十七 足）；字卡五步规程。"
cl=[{"id":f"bdc-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{t[0]}（字卡）",
   "statement":f"{t[0]}（{t[1]}）：{t[2]}","boundary":B(t[0]),"permission":"public",
   "fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,t in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡410此部2026-10-23","risk":"low","claims":cl},
          open(r"intake\20261023-字卡410此部.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡410此部.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))