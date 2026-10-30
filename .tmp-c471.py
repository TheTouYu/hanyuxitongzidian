import json,subprocess,os,glob
BS="【410 此部（原属它部，从勹止声）】此＝从勹（俯伏、背负）从止（脚踏），象意踩在对方背上；是「跐」的初文（《释名》「跐，弭也，足践之使弭服也」，《广雅》「履也」）。转义：由脚下所踩，引申指近处之物（《尔雅》「兹，此也」）；由脚踩引申击打与瘀青（紫「帛青赤色」）；鸟类交尾时雌伏于下故引申雌性（雌「鸟母也」），雌性体小故引申短小（啙「短也」）。辯證：「匕、勹」形近多混，《说文》「从止从匕，匕相比次也」析形不确。字族衍义：①踩使勹→相仇相斗、踩踏叠垒 ②殴伤→青、紫色 ③鸟类交尾→雌性、短小。"
N="字形：古文字字形库未收。"
D=[
("紫","zǐ","《说文》「帛青赤色」；《释名》「紫，疵也，非正色，五色之疵瑕，以惑人者也」——青赤相间的间色。","殴伤族②之糸：以「糸」定其物，色如殴后青紫，故为间色、非正色。","z「凿总」取「总」：青赤总聚成紫。"),
("𦺱","zī","《玉篇》「𦺱菜，生水中」；《集韵》「菜名，芜菁也」。","殴伤族②之艸：以「艸」定其物，色近紫。","z「凿总」取「总」：草聚而生。"),
("玼","cǐ","《说文》「玉色鲜也」；又「玉病」「玉中石」。","殴伤族②之玉：以「玉」定其物，色如伤而鲜。","c「刺持」取「刺」：瑕如刺。"),
("𣐑","cí","《广韵》「无𣐑木，一名楡」——小樟木，即棆。","殴伤族②之木：以「木」定其物，材理如伤纹。","c「刺持」取「持」：木持而纹。"),
("鴜","cí","《说文》「𪈁鴜也」；《玉篇》「水鸟，似鱼虎，苍黑色」。","殴伤族②之鳥：以「鳥」定其物，苍黑如伤色。","c「刺持」取「持」：鸟持而黑。"),
("疵","cī","《说文》「病也」——黑斑、痣；《集韵》「毁也」。","殴伤族②之疒：以「疒」定其类，黑斑如殴伤。","c「刺持」取「刺」：病刺于肤。"),
("䖪","cí","《集韵》「虫，似蝉」；又「蠀螬」虫名。","殴伤族②之虫：以「虫」定其物，色苍如伤。","c「刺持」取「刺」：虫刺而鸣。"),
("𦍧","cǐ","《说文》「羊名，蹏皮可以割桼」——疑指黑山羊。","殴伤族②之羊：以「羊」定其物，毛色黑如伤。","c「刺持」取「持」：羊持而黑。"),
("𪕊","zī","《说文》「鼠，似鸡，鼠尾」；《玉篇》「似鸡而鼠毛，见即大旱」。","殴伤族②之鼠：以「鼠」定其物，色苍如伤。","z「凿总」取「总」：鼠聚而兆旱。"),
("雌","cī","《说文》「鸟母也」；甲骨文从「止」——鸟交尾时雌伏于下。","交尾族③之隹：以「隹」定其类，雌伏在下，故为母鸟。","c「刺持」取「持」：伏而受持。"),
("𩢑","cǐ","《说文》「马名」——疑指母马或矮种马。","交尾族③之馬：以「馬」定其类，雌小故为矮马。","c「刺持」取「持」：伏而受持。"),
("貲","zī","《说文》「小罚以财自赎也」；《玉篇》「财也、货也」——以财赎罪。","交尾族③之貝：以「貝」定其物，罚小如雌小。","z「凿总」取「总」：财总而赎。"),
]
def card(ch,p,Bx,Nx,a,b,c):
    return {"char":ch,"pinyin":p,"bus":[],"sections":[
      {"key":"bengen","label":"字根本义","text":Bx,"cites":[]},
      {"key":"zigen","label":"字形","text":Nx,"cites":[]},
      {"key":"xingpang","label":"形旁声旁","text":a,"cites":[]},
      {"key":"hengxiang","label":"横向对照","text":b,"cites":[]},
      {"key":"shengmu","label":"声母义","text":c,"cites":[]}]}
b="同取此部「殴伤而青紫／雌伏而短小」一面，形符各定其落点；故声符给义、形符定落点。"
for ch,p,Bx,a,c in D:
    json.dump(card(ch,p,BS,N,a,b,c),open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("写卡",len(D))
def B(ch): return "源自《系統漢語》第410部「此部」（卷六十七 足）；字卡五步规程。"
cl=[{"id":f"bdc-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{t[0]}（字卡）",
   "statement":f"{t[0]}（{t[1]}）：{t[2]}","boundary":B(t[0]),"permission":"public",
   "fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,t in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡410此部b2026-10-23","risk":"low","claims":cl},
          open(r"intake\20261023-字卡410此部b.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡410此部b.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))