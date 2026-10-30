import json,subprocess,os,glob,re
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
F1="【第570部「丯部」】憲＝西周金文从目从害（害指刻削），懸法示民、目視省察，引申憲法、高起、興盛；戔系 戟＝有枝兵（戈屬），長柄直刃加橫刃，兼矛戈之長。"
N="字形：古文字字形库未收。"
D=[("憲","xiàn",F1,"从目从害聲：懸法示民（《說文》「敏也」），引申憲法、高起、興盛。","x「续消」取「续」：法懸而续。"),
("幰","xiǎn",F1,"从巾憲聲：車幔（《集韻》），車上張帷。","x取续消：帷張而续。"),
("𩍹","xiǎn",F1,"从革憲聲：革履、靴（《集韻》）。","x取续消：革堅而续。"),
("櫶","xiǎn",F1,"从木憲聲：木名（《集韻》）。","x取续消：木直而续。"),
("瀗","xiàn",F1,"从水憲聲：水名、水聲（《集韻》）。","x取续消：水流而续。"),
("萱","xuān",F1,"从艸憲聲：藼省，忘憂草（《說文》「令人忘憂」），萱堂指母。","x取续消：草柔而续。"),
("㦥","xiǎn",F1,"从心憲聲：敬畏、黠慧（《集韻》）。","x取续消：心敬而续。"),
("戟","jǐ",F1,"从戈倝聲：有枝兵也（《說文》），長柄直刃加橫刃，兼矛戈；引申雄強。","j「聚决」取「聚」：刃聚而决。"),
("撠","jǐ",F1,"从手戟聲：持也、拘持（《集韻》），抓住。","j取聚决：手抓而决。"),
("橶","jǐ",F1,"从木戟聲：木名；戟柄（《集韻》）。","j取聚决：木枝而决。"),
("𦺩","jǐ",F1,"从艸戟聲：草名（《集韻》）。","j取聚决：草刺而决。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"憲系同取「懸目示法、高起」一面（幰車帷、𩍹革履、櫶木、瀗水、萱忘憂、㦥敬畏）；戟系取「有枝之兵」（撠持、橶柄、𦺩草）；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":570,"name":"丯"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lxian-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第570部「丯部」（卷九十四 七）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
p=r"intake\20261024-字卡570c.json"
for it in range(8):
    json.dump({"schema_version":1,"intent":f"字卡570c{it}-2026-10-24","risk":"low","claims":cl},open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    out=run("knowledge-plan","capture","--file",p,"--format","json")
    if "PLAN_DUPLICATE" not in out:
        print("ok claims",len(cl)); break
    idx=int(re.search(r"claims\[(\d+)\]",out).group(1)); print("drop",cl[idx]["title"]); cl.pop(idx)
bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))