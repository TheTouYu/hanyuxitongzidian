import json,subprocess,os,glob,re
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
F="【第574部「剌部」】剌（là）＝甲骨文从刀从𥞥（脫粒的秸稈束）亦聲，以秸稈反覆刮擦、拋光器物，「揧」之初文；轉義乖違不正；又因粗糙刺膚引申灼痛；音源為刮擦聲，與蠍螫之痛近故義音同「萬」。"
N="字形：古文字字形库未收。"
D=[("剌","là",F,"从刀从𥞥亦聲：戾也（《說文》），以秸稈刮擦拋光→乖違不正、灼痛。","l「拢离」取「离」：刮擦而离。"),
("楋","là",F,"从木剌聲：木也（《說文》），樹可放蠟、煎汁為燭（水㯿樹）。","l取拢离：木割而离。"),
("𢃴","là",F,"从巾剌聲：刜也（《說文》），拂拭。","l取拢离：巾拂而离。"),
("揦","là",F,"从手剌聲：撥攋，手披也（《集韻》），撥開、毀裂。","l取拢离：手撥而离。"),
("揧","là",F,"从手𥞥聲：揅也（《博雅》），研破（《廣韻》）。","l取拢离：研磨而离。"),
("𥈙","là",F,"从目剌聲：目子不正也（《玉篇》），眸子不正。","l取拢离：目斜而离。"),
("溂","là",F,"从水剌聲：瀨之或體（《集韻》），水流激石。","l取拢离：水激而离。"),
("辣","là",F,"从辛剌聲：辛痛（《正字通》），薑蒜之辛辣刺痛。","l取拢离：辛烈而离。"),
("瘌","là",F,"从疒剌聲：楚人謂藥毒曰痛瘌（《方言》），惡疾、禿瘡。","l取拢离：疾散而离。"),
("蝲","là",F,"从蟲剌聲：蝲蟿（《集韻》），蟲名。","l取拢离：蟲動而离。"),
("喇","lǎ",F,"从口剌聲：喇叭（《集韻》），吹器之聲。","l取拢离：聲散而离。"),
("賴","lài",F,"从貝剌聲：贏也（《說文》），依靠、利；字族 癩／籟／懶／獺。","l取拢离：依附而离。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"剌部同取「刮擦、灼痛、乖違」一面：楋放蠟、𢃴拂拭、揦撥裂、揧研破、𥈙目斜、溂激水、辣辛痛、瘌惡疾、蝲蟲、喇聲、賴依附；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":574,"name":"剌"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lla-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第574部「剌部」（卷九十四 七）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
p=r"intake\20261024-字卡574a.json"
for it in range(10):
    json.dump({"schema_version":1,"intent":f"字卡574a{it}-2026-10-24","risk":"low","claims":cl},open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    out=run("knowledge-plan","capture","--file",p,"--format","json")
    if "PLAN_DUPLICATE" not in out:
        print("ok claims",len(cl)); break
    idx=int(re.search(r"claims\[(\d+)\]",out).group(1)); print("drop",cl[idx]["title"]); cl.pop(idx)
bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))