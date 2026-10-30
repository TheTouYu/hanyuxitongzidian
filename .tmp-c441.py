import json,subprocess,os,glob
BZ=("【408 止部】部首𣥂（止zhǐ、tà）：象动物脚印形表示足（「趾」之初文，《广韵》「足也」）。"
    "轉義：足为行走器官→行走、到达、停留、静止、居住（《玉篇》「止息也、住也、容止也」，〈广韵〉「停也、禮也、息也、待也、留也」）；由止息→除灭、完毕（《广雅》「滅也」）；足在下支撑身体→基础、基脚（《说文》「下基也」）。"
    "辯證：《说文》据小篆误作「象艸木出有址」；甲骨文明是足有趾之形，故析形不确。音源：借音字，脚板歧出有趾故义音同「氏」「支」。字族衍义：①停足→基址停止 ②举足→行走牵拉 ③俗字或形近「心、寺」之讹。")
N="字形：古文字字形库未收。"
D=[
("止","zhǐ",BZ,N,"象动物脚印（趾之初文），《广韵》「足也」；引申行走、停留、居住、基础、除灭。","部头本字：一足印，趾爪分明。","zh「凿总」取「凿」：趾凿地留印。"),
("趾","zhǐ",BZ,N,"《尔雅·释言》「趾，足也」；《洪武正韵》「足指」——脚趾。","停足族①之足：以「足」定其位，趾在足端。","zh「凿总」取「凿」：趾凿而立。"),
("阯","zhǐ",BZ,N,"《说文》「基也，从𨸏止聲」——基脚（址）。","停足族①之阜：以「阜」定其基，足止为基。","zh「凿总」取「凿」：基凿于地。"),
("祉","zhǐ",BZ,N,"《说文》「福也，从示止聲」，徐铉「福所止不移也」——福。","停足族①之示：以「示」定其福，福止不移。","zh「凿总」取「总」：福总而归。"),
("芷","zhǐ",BZ,N,"《本草》「白芷，一名芳香，生河东川谷」——根粗壮如脚趾。","停足族①之艸：以「艸」定其类，根如脚趾。","zh「凿总」取「凿」：根凿土中。"),
("沚","zhǐ",BZ,N,"《说文》「小渚曰沚」；《释名》「止息也，可以止息其上」——小水洲。","停足族①之水：以「水」定其境，水中小洲可止。","zh「凿总」取「凿」：洲凿水中。"),
("企","qì",BZ,N,"《说文》「举踵也，从人止聲」——踮脚站立；《广韵》「望也」；《释名》「啟也」。","举足族②之人：以「人」定其形，举踵而望。","q「亲缺」取「缺」：足跟缺地而起。"),
("扯","chě",BZ,N,"《正字通》「俗撦字」——拉、牵。","举足族②之手：以「手」定其动，牵引而裂。","ch「刺持」取「持」：手把而扯。"),
("㢟","chān",BZ,N,"《说文》「安步㢟㢟也，从廴从止」——缓步。","举足族②之廴：以「廴」定其步，安步而缓。","ch「刺持」取「持」：步持而缓。"),
("辵","chuò",BZ,N,"《说文》「乍行乍止也，从彳从止」；《六书故》「循道疾行」——走走停停、疾行（辶旁）。","举足族②之彳：以「彳」定其行，行止相间。","ch「刺持」取「刺」：疾行如刺。"),
("咫","zhǐ",BZ,N,"《字彙》「同咫」；《说文》「中妇人手长八寸谓之咫」——八寸为咫。","举足族②之尺：以「尺」定其量，手八寸为咫。","zh「凿总」取「凿」：分寸凿然。"),
("耻","chǐ",BZ,N,"《正字通》「俗恥字」——耻，辱也（从耳从心）。","讹混族③之心：俗从止，以「心」定其情，辱而在心。","ch「刺持」取「刺」：辱刺于心。"),
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
ST={"止":"象动物脚印（趾之初文）；《广韵》「足也」——行走、停留、基础。","趾":"《尔雅》「趾，足也」——脚趾。","阯":"《说文》「基也，从𨸏止聲」——基脚。","祉":"《说文》「福也，从示止聲」，徐铉「福所止不移」。","芷":"《本草》「白芷，一名芳香」——根粗壮如脚趾。","沚":"《说文》「小渚曰沚」——《释名》「可以止息其上」。","企":"《说文》「举踵也，从人止聲」——踮脚而望。","扯":"《正字通》「俗撦字」——拉、牵。","㢟":"《说文》「安步㢟㢟也，从廴从止」——缓步。","辵":"《说文》「乍行乍止也，从彳从止」——走走停停（辶旁）。","咫":"《说文》「中妇人手长八寸谓之咫」——八寸为咫。","耻":"俗「恥」字——辱也。"}
def B(ch): return "源自《系統漢語》第408部「止部」（卷六十七 足）；字卡五步规程。"
cl=[{"id":f"bdm-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{d[0]}（字卡）",
   "statement":f"{d[0]}（{d[1]}）：{ST[d[0]]}","boundary":B(d[0]),"permission":"public",
   "fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,d in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡408止部2026-10-23","risk":"low","claims":cl},
          open(r"intake\20261023-字卡408止部.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡408止部.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    b=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",b,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",b,"--apply","--content-hash",h); run("bundle-apply",b,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",b,"err",v.get("errors"))