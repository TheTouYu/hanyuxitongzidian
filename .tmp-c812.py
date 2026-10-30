import json,subprocess,os,glob,re
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
F="【第574部「剌部」·賴支】賴＝从貝剌聲，贏也（《說文》），依靠、利益；其字族多从賴聲，取「依附、毀壞、怠惰」諸面。"
N="字形：古文字字形库未收。"
D=[("癩","lài",F,"从疒賴聲：惡疾（《集韻》），麻風、疥癩。","l「拢离」取「离」：疾散而离。"),
("籟","lài",F,"从竹賴聲：三孔籥也（《說文》），簫；引申天籟、萬籟。","l取拢离：聲散而离。"),
("懶","lǎn",F,"从心賴聲：怠也（《集韻》），懈怠、懶惰。","l取拢离：心散而离。"),
("獺","tǎ",F,"从犬賴聲：如小狗，水居食魚（《說文》），水獺。","t「涂突」取「突」：獸突而噬。"),
("攋","là",F,"从手賴聲：把攋，棄也（《集韻》），毀裂、毀壞。","l取拢离：手裂而离。"),
("襰","lài",F,"从衣賴聲：墮壞也（《集韻》），衣壞。","l取拢离：衣壞而离。"),
("䲚","lài",F,"从魚賴聲：魚名（《集韻》）。","l取拢离：魚散而离。"),
("嬾","lǎn",F,"从女賴聲：懈也（《說文》「懈也，怠也」），懶惰（俗作懶）。","l取拢离：女惰而离。"),
("䠭","lài",F,"从足賴聲：跛行（《集韻》），行不正。","l取拢离：足跛而离。"),
("䄤","lài",F,"从示賴聲：祭名（《集韻》），禱祭。","l取拢离：祭散而离。"),
("𠘝","lài",F,"从冫賴聲：寒也（《集韻》），寒凍。","l取拢离：寒收而离。"),
("鶒","chì",F,"从鳥剌聲：鸂鶒（《集韻》），水鳥，形似鴛鴦而稍大。","ch「刺持」取「刺」：鳥立而刺。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"賴支同取「依附所生之疾、壞、怠」一面：癩疾、籟聲、懶怠、獺食魚、攋毀、襰壞、䲚魚、嬾惰、䠭跛、䄤祭、𠘝寒、鶒水鳥；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":574,"name":"剌"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"llai-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第574部「剌部」（卷九十四 七）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
p=r"intake\20261024-字卡574b.json"
for it in range(10):
    json.dump({"schema_version":1,"intent":f"字卡574b{it}-2026-10-24","risk":"low","claims":cl},open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    out=run("knowledge-plan","capture","--file",p,"--format","json")
    if "PLAN_DUPLICATE" not in out:
        print("ok claims",len(cl)); break
    idx=int(re.search(r"claims\[(\d+)\]",out).group(1)); print("drop",cl[idx]["title"]); cl.pop(idx)
bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))