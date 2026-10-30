import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
FD="【第527部「向部」·黨系（二级字根）】黨（党）＝从黑尚聲：「黑」為墨色不鮮，「尚」為敞開；本義色暗不鮮（《說文》「不鮮也」）；轉義同色相聚→朋黨、黨與，又借為「儻」表或然。字族三面：色暗不明／朋群相合／直而不隱。"
FZ="【第527部「向部」·掌系（二级字根）】掌（牚𣥺䟫）＝从手尚聲：本義手掌（《說文》「手中也」），即「手」之攤平者；轉義以掌持物→掌管、主持；又掌之平展→支撐（牚、撐）。字族三面：手掌所為／支撐抵距／平展覆蓋。"
N="字形：古文字字形库未收。"
D=[("黨","dǎng",FD,"从黑尚聲：色暗不鮮（《說文》「不鮮也」），引申朋黨、黨與。","d「囤动」取「囤」：聚而同囤。"),
("钂","tǎng",FD,"古兵器，形如半月，當中有槍尖，兩邊出翅。","t「涂突」取「涂」：器銳而突。"),
("儻","tǎng",FD,"从人黨聲：倜儻，卓異、豁達、大志；或然之詞。","t取涂突：人卓而突。"),
("讜","dǎng",FD,"从言黨聲：直言也（《說文》）；又中理、美言。","d取囤动：言直而囤。"),
("攩","dáng",FD,"从手黨聲：朋群也（《說文》），結成朋黨；俗用為抵攩、遮遏。","d取囤动：手擋而囤。"),
("欓","dǎng",FD,"茱萸類、越椒（《玉篇》），莖有刺故有「擋」義。","d取囤动：木刺而囤。"),
("爣","tǎng",FD,"爣朗，火光寬明（《廣韻》）。","t取涂突：火光而突。"),
("曭","tǎng",FD,"日無光也（《集韻》）。","t取涂突：日暗而突。"),
("灙","dǎng",FD,"漭灙，水皃；又水名（灙水）。","d取囤动：水聚而囤。"),
("矘","tǎng",FD,"从目黨聲：目無精直視也（《說文》），茫然直視。","t取涂突：目直而突。"),
("掌","zhǎng",FZ,"从手尚聲：手掌（《說文》「手中也」），引申掌管；掌之平展→支撐。","zh「凿总」取「总」：掌合而總。"),
("撐","chēng",FZ,"从手掌聲：柱也（《集韻》），斜柱支撐；橕、撐、牚、𣥺音義同。","ch「刺持」取「持」：手撐而持。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"黨系諧聲字分三面：色暗不明（爣／曭／矘）／朋群相合（攩／欓／黨）／直而不隱（讜／儻／钂／灙）；掌系分手掌所為（掌）與支撐抵距（撐）；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":527,"name":"向"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"ldang3-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}（{p}）＝{xp}",
 "boundary":"源自《系統漢語》第527部「向部」（卷八十八 昜，黨系／掌系）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡527h2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡527h.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡527h.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))