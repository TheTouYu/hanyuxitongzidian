import json,subprocess,os,glob,re
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
F="【第577部「制部」】制＝甲骨文从木从刀，象整枝／砍樹／加工木頭；引申禁止、約束、法度、決斷；音源借音（義音同丯）。"
N="字形：古文字字形库未收。"
D=[("剬","zhì",F,"从刀耑聲：斷也（《說文》「剬，斷也」），裁斷。","zh「凿总」取「总」：斷齊而总。"),
("䱥","zhì",F,"从魚制聲：魚名（《廣韻》），可為醬，閩之鯽魚。","zh取凿总：魚聚而总。"),
("痸","chì",F,"从疒制聲：癡病（《字彙補》），抽風、痙攣。","ch「刺持」取「持」：筋搐而持。"),
("猘","zhì",F,"从犬制聲：狂犬（《集韻》本作狾），瘋狗。","zh取凿总：犬狂而总。"),
("㫼","zhì",F,"从日制聲：明也（《集韻》），日光昭明。","zh取凿总：日明而总。"),
("𡝧","xì",F,"从女制聲：凶恣也（《集韻》），婦人凶橫。","x「续消」取「续」：怒續而消。"),
("𢛁","dá",F,"从心制聲：驚也（《玉篇》），驚恐；又心動。","d「囤动」取「动」：心動而囤。"),
("𤙲","zhì",F,"从牛制聲：牛名（《集韻》），牛之別稱。","zh取凿总：牛馴而总。"),
("𥇕","zhì",F,"从目制聲：目明（《集韻》），視之審。","zh取凿总：目視而总。"),
("𦜋","zhì",F,"从肉制聲：腶也（《集韻》），肉脯。","zh取凿总：肉切而总。"),
("𧨰","zhì",F,"从言制聲：言也（《集韻》），言語。","zh取凿总：言斷而总。"),
("𨧳","zhì",F,"从金制聲：鐵也（《集韻》），金屬。","zh取凿总：金凝而总。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"制部餘字同取「裁斷所及」（魚、疒、犬、日、女、心、牛、目、肉、言、金）一面：剬、䱥、痸、猘、㫼、𡝧、𢛁、𤙲、𥇕、𦜋、𧨰、𨧳；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":577,"name":"制"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lzhi-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第577部「制部」（卷九十四 七）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
p=r"intake\20261024-字卡577a.json"
for it in range(10):
    json.dump({"schema_version":1,"intent":f"字卡577a{it}-2026-10-24","risk":"low","claims":cl},open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    out=run("knowledge-plan","capture","--file",p,"--format","json")
    if "PLAN_DUPLICATE" not in out:
        print("ok claims",len(cl)); break
    idx=int(re.search(r"claims\[(\d+)\]",out).group(1)); print("drop",cl[idx]["title"]); cl.pop(idx)
bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))