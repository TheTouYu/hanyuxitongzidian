import json,subprocess,os,glob
BS="【410 此部（原属它部，从勹止声）】此＝从勹（俯伏、背负）从止（脚踏），象意踩在对方背上；是「跐」的初文（《释名》「跐，弭也，足践之使弭服也」）。转义：由脚下所踩，引申指近处之物（《尔雅》「兹，此也」）；由脚踩引申击打、瘀青（紫「帛青赤色」）；鸟类交尾时雌伏于下故引申雌性（雌「鸟母也」），雌性体小故引申短小（啙「短也」）。辯證：「匕、勹」形近多混，《说文》「从止从匕，匕相比次也」析形不确。字族衍义：①踩使勹→相仇相斗、踩踏叠垒 ②殴伤→青、紫色 ③鸟类交尾→雌性、短小。"
N="字形：古文字字形库未收。"
D=[
("頾","zī","《说文》「口上须也」；甲骨文象人颊有须形，西周金文才加「此」作声符。","短小族③之须：以「须」定其物，加「此」表短小——短须曰頾（后俗作髭）。","z「凿总」取「总」：须总而生。"),
("鈭","zī","《说文》「鈭錍，釜也」——短斧；一说小釜。","短小族③之金：以「金」定其器，小故为短斧。","z「凿总」取「凿」：短小而凿。"),
("姕","zī","《说文》「妇人小物也」（严可均校：物当作弱）——妇人柔弱貌；《集韵》「舞也」。","短小族③之女：以「女」定其人，小弱故为姕。","z「凿总」取「总」：柔而总聚。"),
("祡","chái","《说文》「烧祡焚燎以祭天神」——烧柴祭天；通作柴。","踩踏族①之示：以「示」定其礼，柴燎祭天。","ch「刺持」取「刺」：柴刺而燃。"),
("柴","chái","《说文》「小木散材」；《广韵》「薪也」；又「柴池，参差也」。","踩踏族①之木：以「木」定其物，散材堆积如踩叠。","ch「刺持」取「刺」：木刺而为薪。"),
("𤿙","zhì","《广韵》「𤿙皱，皮不展也」——皮皱不展；又赖皮。","踩踏族①之皮：以「皮」定其物，践踏则皱。","zh「凿总」取「凿」：皮凿而皱。"),
("啙","zǐ","《说文》「窳也」；《方言》「短也」；《广韵》「弱也」。","短小族③之口：以「口」定其声，小弱故啙。","z「凿总」取「总」：口总而小。"),
("鮆","jì","《说文》「饮而不食，刀鱼也」；《方言》「凡物生而不长大，亦谓之鮆」。","短小族③之魚：以「魚」定其物，刀鱼细长而不长大。","j「聚决」取「决」：决水而出。"),
("飺","cí","《玉篇》「嫌食貌」；《集韵》「歉食也」「恶食也」——厌食。","短小族③之食：以「食」定其事，食少故为飺。","c「刺持」取「持」：持食而少。"),
("㠿","zī","《玉篇》「布也」；《类篇》「布名」——精美的细布。","踩踏族①之巾：以「巾」定其物，细密如踩平。","z「凿总」取「总」：丝总而布。"),
("佌","cǐ","《尔雅·释训》「佌佌，小也」；《玉篇》「小舞貌」。","短小族③之人：以「人」定其形，小故佌佌。","c「刺持」取「刺」：小如刺。"),
("呲","cī","《集韵》「嫌食也」「无食也」；又同「龇」，露齿。","踩踏族①之口：以「口」定其声，露齿相向如踩。","c「刺持」取「刺」：齿刺而露。"),
]
def card(ch,p,Bx,Nx,a,b,c):
    return {"char":ch,"pinyin":p,"bus":[],"sections":[
      {"key":"bengen","label":"字根本义","text":Bx,"cites":[]},
      {"key":"zigen","label":"字形","text":Nx,"cites":[]},
      {"key":"xingpang","label":"形旁声旁","text":a,"cites":[]},
      {"key":"hengxiang","label":"横向对照","text":b,"cites":[]},
      {"key":"shengmu","label":"声母义","text":c,"cites":[]}]}
b="同取此部「踩踏叠垒／雌伏而短小」一面，形符各定其落点；故声符给义、形符定落点。"
for ch,p,Bx,a,c in D:
    json.dump(card(ch,p,BS,N,a,b,c),open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("写卡",len(D))
def B(ch): return "源自《系統漢語》第410部「此部」（卷六十七 足）；字卡五步规程。"
cl=[{"id":f"bdc-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{t[0]}（字卡）",
   "statement":f"{t[0]}（{t[1]}）：{t[2]}","boundary":B(t[0]),"permission":"public",
   "fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,t in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡410此部c2026-10-23","risk":"low","claims":cl},
          open(r"intake\20261023-字卡410此部c.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡410此部c.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))