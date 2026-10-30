import json,subprocess,os,glob
B=("部首析（㭊扸斨𣂔xī）：从斤从木——可以象意砍伐樹木，也可以指砍破木頭；《說文》「破木也。一曰折也」（先激切）。"
   "轉義：由砍開木頭，引申指分開、分散、割裂（《廣韻》分也）。音源：音源字，源自木裂之聲；因有分散之義，義音同「斯」（《集韻》「蜤，蟲名，《爾雅》蜤螽蜙蝑」通作斯）。字族衍義：指砍伐，表示分開。")
N="字形：古文字字形庫未收；原稿該部有「▲蜥蜴斷尾」圖，可參。"
D=[
("淅","xī","从水析聲，《說文》「汏米也」（先擊切），淘米——分開米與糠。","析部主組：與皙（白）、晰（明）、菥（草名）、惁（憂）、蜥（斷尾）同取「剖分」，以水定落點——水洗而米糠分。","x「續消」取「消」：米糠消散。"),
("皙","xī","从白析聲，《說文》「人色白也」（先擊切）；《爾雅》「皙，無實棗」；《集韻》白也。原稿謂應从「淅」省聲——白如淘洗之米。","主組：以白定落點——淘洗之米白，故人色白曰皙。","x「續消」取「消」：色褪而白。"),
("晰","xī","从日析聲，《集韻》「明也」，清晰。","主組：日光剖分而物象分明，以日定落點。","x「續消」取「消」：霧消而明。"),
("菥","xī","从艸析聲，《爾雅》「菥蓂，大薺」，《玉篇》「葴菥草，似燕麥」——遏藍菜，葉可食、種子可榨油。","主組：莢果剖分而子出，以艸定落點。","x「續消」取「消」：草枯而消。"),
("惁","xī","从心析聲，《玉篇》「憼也、憂也」。","主組：心被剖分而憂，以心定落點。","x「續消」取「消」：憂而心消。"),
("㱤","xī","从歹析聲，《廣韻》「㱸㱤，欲死之皃」，《博雅》「極也」。","主組：氣力剖散將盡，以歹定落點。","x「續消」取「消」：精氣消散。"),
("𥮥","zhuó","从竹析聲，《字彙補》「之若切，音灼」，同「策」——計數之竹簽，或占卜蓍草。","主組：竹剖為簽，以竹定落點。","z「鑿總」取「鑿」：剖竹如鑿。"),
("唽","xī","从口析聲，《集韻》「𠴭，鳥聲，或从析」。","主組：鳥聲細碎如裂，以口定落點。","x「續消」取「消」：聲出而消。"),
("𩗱","xī","从風析聲，《集韻》「𩗱𩗱，風聲」。","主組：風裂而鳴，以風定落點。","x「續消」取「消」：風過而消。"),
("𪁻","zhì","从鳥析聲，《篇海》「之利切，音鷙」，猛鳥也。","主組：猛鳥裂物，以鳥定落點。","zh「鑿總」取「鑿」：喙鑿而裂。"),
("蜥","xī","从虫析聲，《說文》「蜥易也」（先擊切）；遇急則斷尾求生。","主組之要：斷尾正是「剖分」在蟲身上的活例，以虫定落點。","x「續消」取「消」：斷尾而存。"),
]
def card(ch,p,a,b,c):
    return {"char":ch,"pinyin":p,"bus":[],"sections":[
      {"key":"bengen","label":"字根本義","text":B,"cites":[]},
      {"key":"zigen","label":"字形","text":N,"cites":[]},
      {"key":"xingpang","label":"形旁声旁","text":a,"cites":[]},
      {"key":"hengxiang","label":"横向对照","text":b,"cites":[]},
      {"key":"shengmu","label":"声母义","text":c,"cites":[]}]}
for ch,p,a,b,c in D:
    json.dump(card(ch,p,a,b,c),open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("写卡",len(D))
BK="源自《系統漢語》第390部「析部」；字卡五步规程。"
ST={"淅":"淘米即分開米與糠，以水定其落點。","皙":"白如淘洗之米；原稿謂應从淅省聲。","晰":"日光剖分而物象分明。","菥":"菥蓂莢果剖分而子出。","惁":"心被剖分而憂。","㱤":"氣力剖散將盡，欲死之貌。","𥮥":"同策，竹剖為簽以計數。","唽":"鳥聲細碎如裂。","𩱱":"風裂而鳴。","𪁻":"猛鳥裂物。","蜥":"遇急斷尾求生，是剖分之活例。"}
cl=[{"id":f"bt5-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{d[0]}（字卡）",
     "statement":f"{d[0]}（{d[1]}）：{ST.get(d[0],d[2])}",
     "boundary":BK,"permission":"public","fact_classes":["evidence_scope"],
     "duplicate_resolution":"create_distinct_with_boundary"} for i,d in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡390析部2026-10-23","risk":"low","claims":cl},
          open(r"intake\20261023-字卡390析部.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡390析部.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    b=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",b,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",b,"--apply","--content-hash",h); run("bundle-apply",b,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",b,"err",v.get("errors"))
else: print(out[-300:])