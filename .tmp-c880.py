import json,subprocess,os,glob,re
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
N="字形：古文字字形库未收。"
F="【第591部「殸部」】殸＝甲骨文从声从殳（声＝草繩系懸之石，殳＝持槌敲擊），象敲擊懸挂石磬，磬之初文（《說文》「樂石也」）；轉義 泛指聲響、擊打之敵、空盡（磬懸不著物故空）、彎曲（磬折）；音源＝擊磬聲（古殸、生通用）。"
D=[("殸","qìng",F,"从声从殳：象敲擊懸石，磬之初文（《說文》「樂石也」）；引申 聲響、空盡、彎曲。","q「亲缺」取「缺」：擊石而缺。"),
("聲","shēng",F,"从耳殸聲：音也（《說文》「音也」），樂音、聲響。","sh「失收」取「失」：聲發而收。"),
("馨","xīn",F,"从香殸聲：香之遠聞者（《說文》），香氣綿綿如磬聲。","x「续消」取「续」：香遠而续。"),
("䡰","kēng",F,"从車殸聲：車堅也（《說文》「車堅也」）；又車聲。","k「口控」取「控」：車堅而控。"),
("𣍆","níng",F,"从日殸聲：告也（《玉篇》）。","n「纳弄」取「纳」：告而纳。"),
("鏧","lóng",F,"从金殸聲：鼓聲（《集韻》「𪔳，鼔聲，或作鏧」）。","l「拢离」取「拢」：鼓聲而拢。"),
("𪔰","yìn",F,"从鼓殸聲：鼓聲（《廣韻》引《兵書》）。","y「续消」取「续」：鼓續而续。"),
("韾","yīn",F,"从音殸聲：聲和靖也（《廣韻》），聲音安和。","y取续消：聲和而续。"),
("𡄔","qìng",F,"从口殸聲：長聲（《篇海》）。","q取亲缺：長聲而缺。"),
("𪚣","qìng",F,"从鬼殸聲：𪚣生，鬼名（《漢典》），疑本指雷聲。","q取亲缺：鬼名而缺。"),
("𤹥","yìng",F,"从疒殸聲：㰽聲（《集韻》），大呼用力；又謳聲。","y取续消：呼而续。"),
("𥃟","qīng",F,"从目殸聲：不可進皃（《龍龕》）。","q取亲缺：視阻而缺。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"殸部同取「擊石清越之聲」一面：聲樂音、馨香遠、䡰車堅、鏧鼓聲、𪔰鼓聲、韾聲和、𡄔長聲、𪚣鬼名、𤹥呼聲、𥃟阻視；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":591,"name":"殸"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lqing-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第591部「殸部」（卷九十七 殸）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
p=r"intake\20261024-字卡591a.json"
for it in range(10):
    json.dump({"schema_version":1,"intent":f"字卡591a{it}-2026-10-24","risk":"low","claims":cl},open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    out=run("knowledge-plan","capture","--file",p,"--format","json")
    if "PLAN_DUPLICATE" not in out:
        print("ok claims",len(cl)); break
    idx=int(re.search(r"claims\[(\d+)\]",out).group(1)); print("drop",cl[idx]["title"]); cl.pop(idx)
bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))