import json,subprocess,os,glob
BZ=("【407 足部】部首足（𠯁𤴕zú）：甲骨文象人的整条腿形，包括大腿、脚、掌、趾，后腿脚部分写作「口」形（《说文》「人之足也，在下，从止口」，徐锴「口象股胫之形」）。"
    "轉義：足起支撑基础作用→器物的脚、植物的根茎、事物的基础（鼎足、葵足、山足）；相对躯体足为小却能承载大部→足够、满足、增益过分（足恭）；两足等长并拢→等齐（珿）、迫促（促）。"
    "音源：音源字，源自足踏声。字族衍义：①两足距离→迫促、催促、急促 ②两足长度→齐整、相等 ③足的大小→小 ④与足相关的行为。")
N="字形：古文字字形库未收；原稿有「▲發苗的再生稻」可参。"
D=[
("足","zú",BZ,N,"甲骨文象整条腿（大腿、脚、掌、趾），《说文》「人之足也，在下，从止口」；《尔雅》「二足而毛謂之禽，四足而毛謂之獸」——鸟脚兽脚器物脚。","部头本字：止定其行，口象股胫。","z「凿总」取「凿」：足凿地而行。"),
("促","cù",BZ,N,"《说文》「迫也，从人足聲」；《广雅》「近也」；《字彙》「短也、蹙也、催也」——急迫、催促。","迫促族①之人：以「人」定其处，两足以近相逼。","c「刺持」取「刺」：刺近而迫。"),
("趗","cù",BZ,N,"《集韵》「趢趗，局小皃」；《類篇》「小步」；《玉篇》「迫也、連也」——迫促、小步相连。","迫促族①之走：以「走」定其动，步小而连。","c「刺持」取「刺」：步刺而促。"),
("𤗁","cù",BZ,N,"《广韵》「迫也」——压迫。","迫促族①之片：以「片」定其物，板压而迫。","c「刺持」取「刺」：片刺而逼。"),
("㹱","què",BZ,N,"《玉篇》「宋良犬」；《广韵》「韓獹宋㹱」——良犬名。","迫促族①之犬：以「犬」定其类，促而善逐。","q「亲缺」取「缺」：犬缺而疾。"),
("䛤","cù",BZ,N,"《等韻》「音促，言急也」；《龍龕》「心急䛤也」——言语急促、心急。","迫促族①之言：以「言」定其声，语促而急。","c「刺持」取「刺」：言刺而急。"),
("𥞺","zhuō",BZ,N,"《字彙補》「今年稻死，來年自生也」——再生稻（由根部再生）。","迫促族①之禾：以「禾」定其类，根促而更生。","zh「凿总」取「凿」：断而复生。"),
("齪","chuò",BZ,N,"《集韵》「齷齪，迫也」；《正韻》「急促局陿貌」；今指不干净，疑本指牙缝藏垢。","迫促族①之齿：以「齿」定其处，牙缝局促藏垢。","ch「刺持」取「持」：齿持垢而不去。"),
("娖","chuò",BZ,N,"《玉篇》「辯也」；《集韵》「娕，《說文》『謹也』，一曰善也」——谨慎。","迫促族①之女：以「女」定其人，局促而谨。","ch「刺持」取「持」：持谨不放。"),
("捉","zhuō",BZ,N,"《说文》「搤也，从手足聲，一曰握也」；《釋名》「促也，使相促及也」——握持。","迫促族①之手：以「手」定其动，握而促之。","zh「凿总」取「总」：总而握之。"),
("哫","zú",BZ,N,"《集韵》「哫訾，以言求媚也」——以言语求媚。","迫促族①之口：以「口」定其声，言媚而促。","z「凿总」取「凿」：言凿而媚。"),
("𩈤","chù",BZ,N,"《篇海》「音促，齊也」——齐整。","等齐族②之面：以「面」定其形，两足等则面正。","ch「刺持」取「持」：持齐不偏。"),
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
ST={"足":"《说文》「人之足也，在下，从止口」——甲骨文象整条腿；《尔雅》「二足而毛謂之禽，四足而毛謂之獸」。","促":"《说文》「迫也，从人足聲」——急迫、催促。","趗":"《集韵》「趢趗，局小皃」；《類篇》「小步」——迫促小步。","𤗁":"《广韵》「迫也」。","㹱":"《玉篇》「宋良犬」；《廣韻》「韓獹宋㹱」。","䛤":"《等韻》「音促，言急也」——言语急促。","𥞺":"《字彙補》「今年稻死，來年自生也」——再生稻。","齪":"《集韵》「齷齪，迫也」——局促拘谨；今指不洁，疑本指牙缝藏垢。","娖":"《玉篇》「辯也」；《集韵》「謹也」——谨慎。","捉":"《说文》「搤也，从手足聲，一曰握也」——握持。","哫":"《集韵》「哫訾，以言求媚也」。","𩈤":"《篇海》「音促，齊也」——齐整。"}
def B(ch): return "源自《系統漢語》第407部「足部」（卷六十七 足）；字卡五步规程。"
cl=[{"id":f"bdd-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{d[0]}（字卡）",
   "statement":f"{d[0]}（{d[1]}）：{ST[d[0]]}","boundary":B(d[0]),"permission":"public",
   "fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,d in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡407足部2026-10-23","risk":"low","claims":cl},
          open(r"intake\20261023-字卡407足部.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡407足部.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    b=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",b,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",b,"--apply","--content-hash",h); run("bundle-apply",b,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",b,"err",v.get("errors"))