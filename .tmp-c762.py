import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
FH="【第560部「孨部」】孨＝从子之二疊或三疊：多子（孖，一產二子）或多胞胎；疊體亦表極致，指十分幼弱孤露；引申謹慎、懦弱、孤兒、滋長。"
N="字形：古文字字形库未收。"
D=[("孨","zhuǎn",FH,"从三子：謹也（《說文》「謹也」），孤露可憐、懦弱。","zh「凿总」取「凿」：弱小而凿。"),
("孖","zī",FH,"从二子：一產二子（《集韻》「一產二子」），通作孳，蕃長。","z「凿总」取「总」：子聚而总。"),
("孱","chán",FH,"从孨在尸下：迮也，一曰呻吟（《說文》），狹窄、孱弱。","ch「刺持」取「持」：弱而持。"),
("孴","nì",FH,"从三子：聚皃（《集韻》「聚皃」），眾多聚集。","n「纳弄」取「纳」：子纳而聚。"),
("驏","zhàn",FH,"从馬孱聲：馬名（《說文》），不施鞍轡之馬。","zh取凿总：馬弱而凿。"),
("僝","chán",FH,"从人孱聲：具也（《說文》「具也」），僝僽、折磨。","ch取刺持：人弱而持。"),
("轏","zhàn",FH,"从車孱聲：竹木之車曰棧（《韻會》），臥車。","zh取凿总：車木而凿。"),
("剗","chǎn",FH,"从刀戔聲：削也、平也（《廣韻》），剗削。","ch取刺持：刀削而持。"),
("樼","zhēn",FH,"从木孱聲：木也（《說文》），同榛，叢木。","zh取凿总：木叢而凿。"),
("潺","chán",FH,"从水孱聲：潺湲，水聲（《說文》「水聲」）。","ch取刺持：水聲而持。"),
("㵫","nì",FH,"从水孴聲：水聲（《集韻》），水沸。","n取纳弄：水纳而弄。"),
("𤂇","zī",FH,"从水孳聲：同滋，蕃長也（《玉篇》），滋長。","z取凿总：水滋而总。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"孨系同取「子多而弱、疊體極致」一面：孖雙生、孴聚、孱呻吟、驏馬、僝具、轏車、剗削、樼叢木、潺水聲、𤂇滋長；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":560,"name":"孨"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lzhuan-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第560部「孨部」（卷九十二 辛）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡560a2026-10-24","risk":"low","claims":cl},open(r"intake\20261024-字卡560a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261024-字卡560a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))