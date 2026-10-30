import json,subprocess,os,glob,re
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
F="【第579部「䍜部」】䍜（罩）＝以網罩鳥；羅＝以絲罟鳥，轉義環繞羅列、遭遇；音源借音（義音同離）。"
N="字形：古文字字形库未收。"
D=[("欏","luó",F,"从木羅聲：檖木也（《玉篇》），桫欏；又籬格。","l「拢离」取「离」：木列而离。"),
("㦬","luǒ",F,"从心羅聲：懡㦬，慙也（《集韻》），慚愧。","l取拢离：心慙而离。"),
("𧟌","luò",F,"从衣羅聲：女人上衣也（《玉篇》）。","l取拢离：衣覆而离。"),
("㿚","luò",F,"从疒羅聲：病也（《集韻》），瘦病。","l取拢离：病瘦而离。"),
("玀","luó",F,"从犬羅聲：玀玀（《龍龕》），元明清史籍對彝族的蔑稱。","l取拢离：族分而离。"),
("𤓓","luó",F,"从火羅聲：糊味（《漢典》），燒焦氣味。","l取拢离：火焦而离。"),
("𥗴","luǒ",F,"从石羅聲：眾石貌（《集韻》），磊砢。","l取拢离：石聚而离。"),
("𥗿","luó",F,"从石羅聲：𥗿砢，山貌（《集韻》）。","l取拢离：山石而离。"),
("𦣇","luó",F,"从肉羅聲：驢腹下肉（《集韻》）。","l取拢离：肉垂而离。"),
("𧹐","luò",F,"从貝羅聲：貝殼也（《五侯鯖字海》）。","l取拢离：貝列而离。"),
("𨇽","luò",F,"从足羅聲：𨇽䟶，猶蹭蹬也（《集韻》），失意、原地打轉。","l取拢离：足滯而离。"),
("𩽰","luó",F,"从魚羅聲：魚名，一身十首（《集韻》），八帶魚（章魚）。","l取拢离：魚聚而离。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"羅聲諸字同取「環繞、牽連」一面：欏木、㦬慙、𧟌衣、㿚病、玀族、𤓓焦、𥗴石、𥗿山、𦣇肉、𧹐貝、𨇽足滯、𩽰魚；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":579,"name":"䍜"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lzhao2-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第579部「䍜部」（卷九十五 離）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
p=r"intake\20261024-字卡579b.json"
for it in range(10):
    json.dump({"schema_version":1,"intent":f"字卡579b{it}-2026-10-24","risk":"low","claims":cl},open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    out=run("knowledge-plan","capture","--file",p,"--format","json")
    if "PLAN_DUPLICATE" not in out:
        print("ok claims",len(cl)); break
    idx=int(re.search(r"claims\[(\d+)\]",out).group(1)); print("drop",cl[idx]["title"]); cl.pop(idx)
bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))