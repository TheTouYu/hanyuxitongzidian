import json,subprocess,os,glob
BXI="【416 昔部（从日𡿧声）】昔＝从日𡿧声：「𡿧」指大水，「日」指太阳，象意太阳入水、夜晚降临（《广雅》「夜也」），或象水面映日、波光粼粼；日又引申指时间，指被洪水淹没的时候——故表示过去、以往（《玉篇》「往也、久也、昨也」）。转义：由波光日影引申指涂饰（《正字通》「与错通」）。辯證：《说文》「乾肉也」所释应是「腊」。音源：借音字，义音同「舃」（鹊）。字族衍义：①指涂饰，表示错磨、交错、粗糙 ②指往昔，表示安置、吝惜、时间久。"
D=[("趞","què","《说文》「趞趞也，一曰行貌」——行轻貌；侧行、践。","涂饰族①之走：以「走」定其行，行轻如错。","q「亲缺」取「缺」：轻行而缺痕。"),
("踖","jí","《说文》「长胫行也，一曰踧踖」；《广韵》「践也」；《尔雅》「踖踖，敏也」。","涂饰族①之足：以「足」定其行，践履交错。","j「聚决」取「决」：足决而行。"),
("齰","zé","《说文》「啮也」——咬嚼；又「齿相值」「上下齿不齐」。","涂饰族①之齒：以「齒」定其动，齿错而不齐。","z「凿总」取「凿」：齿凿而啮。"),
("斮","zhuó","《说文》「斩也」；《尔雅》「鱼则斮之」，郭注「削鳞也」。","涂饰族①之斤：以「斤」定其器，斩削如错。","zh「凿总」取「凿」：斤凿而斩。"),
("矠","zé","《说文》「矛属」；《广韵》「以矛叉取物也」——刺取。","涂饰族①之矛：以「矛」定其器，叉刺如错入。","z「凿总」取「凿」：矛凿而入。"),
("簎","cè","《说文》「刺也」；《周礼》「簎鱼鳖」——以竹钉器具夜照叉鱼。","涂饰族①之竹：以「竹」定其器，竹钉刺取。","c「刺持」取「刺」：竹刺而取。"),
("䇎","què","《说文》「惊貌」；《集韵》「竦也、敬也」。","涂饰族①之立：以「立」定其态，惊而立。","q「亲缺」取「缺」：立而缺安。"),
("碏","què","《左传》卫大夫石碏；《广韵》「敬也」；《集韵》「碍也」。","涂饰族①之石：以「石」定其物，石错而碍。","q「亲缺」取「缺」：石缺而碍。"),
("剒","cuò","《尔雅》「犀谓之剒」，治朴之名；《玉篇》「亦作错」，锉磨之义。","涂饰族①之刀：以「刀」定其器，锉磨如错。","c「刺持」取「刺」：刀刺而锉。"),
("䱜","cuò","《集韵》「鱼名，出东海」；一说鼻前有骨如斧斤；鱕䱜即鲨鱼。","涂饰族①之魚：以「魚」定其物，鼻骨如斧。","c「刺持」取「刺」：骨刺而利。"),
("鵲","què","喜鹊；《本草》「以音感而孕，以视而抱，季冬始巢」。","涂饰族①之鳥：以「鳥」定其物，鹊羽黑白交错。","q「亲缺」取「缺」：鹊鸣而缺。"),
("諎","zé","《说文》「大声也」；又「酬言」「说话快」「诱言」。","涂饰族①之言：以「言」定其声，言交错而急。","z「凿总」取「凿」：言凿而利。")]
N="字形：古文字字形库未收。"
for ch,p,stmt,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":BXI,"cites":[]},
         {"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":stmt+"　"+xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取昔部「错磨交错／往昔之久」一面，形符各定其落点；故声符给义、形符定落点。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("写卡",len(D))
cl=[{"id":f"bdc-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{t[0]}（字卡）",
   "statement":f"{t[0]}（{t[1]}）：{t[2]}","boundary":"源自《系統漢語》第416部「𡿧部」（卷六十九 舄）；字卡五步规程。",
   "permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,t in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡416b2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡416b.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡416b.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))