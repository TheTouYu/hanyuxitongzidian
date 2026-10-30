import json,subprocess,os,glob
B="【415 得部（原属它部，从又从贝）】得＝从又从贝，象意拾取贝壳（或从「彳」）；「贝」本指钱贝，故也指获得钱财（《说文》「行有所得也」）。转义：拾取贝壳时会停下脚步，故引申指停止（碍，《集韵》「碍，止也」）。辯證：小篆把「贝」写得像「见」，故《说文》「䙷，取也，从见从寸」析形不确。音源：借音字，因有碍止义而义音同「寺」。字族衍义：①指拾贝时的样子，表示走走停停 ②（缺）③指拾贝，表示阻碍。"
N="字形：古文字字形库未收。"
D=[
("㥂","tè","《广韵》「㥂㥂，快也」；《字汇》「动心，得也」；《集韵》「心惧」。","拾贝族①之心：以「心」定其情，得之而快。","t「涂突」取「突」：心动如突。"),
("𠮊","dé","《广韵》「取也」——取。","拾贝族①之口：以「口」定其取。","d「囤动」取「囤」：囤取于口。"),
("𡭂","dé","《玉篇》「弱貌」——弱小貌。","拾贝族①之小：以「小」定其形，得而弱。","d「囤动」取「囤」：小如囤粒。"),
("𢕚","dí","《集韵》「𢕚滴，水少」——水少。","拾贝族①之彳：以「彳」定其行，滴少而止。","d「囤动」取「囤」：囤滴而蓄。"),
("𣮊","dé","《玉篇》「毛少也」——毛少。","拾贝族①之毛：以「毛」定其物，毛少如得而止。","d「囤动」取「囤」：毛囤而稀。"),
("𤙰","tè","《玉篇》「牛也」；《集韵》「特，牛父也，或作犆、𤙰」——公牛。","拾贝族①之牛：以「牛」定其类，公牛独立。","t「涂突」取「突」：突出而立。"),
("𤷙","dé","《集韵》「病也」——病。","拾贝族①之疒：以「疒」定其类，得而病。","d「囤动」取「囤」：病囤于身。"),
("𨁽","dé","《玉篇》「行𨁽𨁽也」——行走貌。","拾贝族①之足：以「足」定其行，走走停停。","d「囤动」取「囤」：囤步而行。"),
("淂","dé","《集韵》「水貌，一曰水名」——水貌、水名。","拾贝族①之水：以「水」定其物。","d「囤动」取「囤」：水囤而聚。"),
("碍","ài","《正字通》「俗碍字」——妨碍、阻止。","阻礙族③之石：以「石」定其物，石阻而止。","零声母不系（今读 ài 影母字）。"),
("𨵏","ài","《正字通》「以木栏门」，碍、硋、閡并通。","阻礙族③之门：以「门」定其处，栏门而止。","零声母不系（今读 ài 影母字）。"),
("棏","dé","《唐韵》「木名」；《集韵》「㭙，槌也，或作棏」——蚕箔搁架上的横木。","拾贝族①之木：以「木」定其物，横木承箔。","d「囤动」取「囤」：木囤而架。"),
]
def card(ch,p,Bx,desc,sm,_extra=None):
    return {"char":ch,"pinyin":p,"bus":[],"sections":[
      {"key":"bengen","label":"字根本义","text":Bx,"cites":[]},
      {"key":"zigen","label":"字形","text":N,"cites":[]},
      {"key":"xingpang","label":"形旁声旁","text":desc,"cites":[]},
      {"key":"hengxiang","label":"横向对照","text":"同取得部「拾而得之／拾而止之」一面，形符各定其落点；故声符给义、形符定落点。","cites":[]},
      {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]}
for ch,p,stmt,desc,sm in D:
    json.dump(card(ch,p,B,stmt+'　'+desc,sm),open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("写卡",len(D))
cl=[{"id":f"bdc-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{t[0]}（字卡）",
   "statement":f"{t[0]}（{t[1]}）：{t[2]}","boundary":"源自《系統漢語》第415部「得部」（卷六十七 足）；字卡五步规程。",
   "permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,t in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡415得部b2026-10-23","risk":"low","claims":cl},
          open(r"intake\20261023-字卡415得部b.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡415得部b.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))