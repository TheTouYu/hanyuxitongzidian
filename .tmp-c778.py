import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
F="【第567部「七部」】七＝从一加指示符（切刻之初文）；甲支＝从甲（硬殼、逼窄），本批皆甲支余字。"
N="字形：古文字字形库未收。"
D=[("𦾏","xiá",F,"从艸甲聲：花葉重多皃（《集韻》）。","x「续消」取「续」：葉多而续。"),
("𢘉","xiá",F,"从心甲聲：樂也、喜也（《玉篇》《廣韻》）。","x取续消：喜而续。"),
("𣢗","xiā",F,"从欠甲聲：鼻息（《集韻》「𣢗𣢗，鼻息」）。","x取续消：息微而续。"),
("䛅","xiá",F,"从言甲聲：多言也（《玉篇》），或作嗑。","x取续消：言多而续。"),
("笚","dā",F,"从竹甲聲：竹相擊也（《玉篇》）；或省作筪，竹名。","d「囤动」取「囤」：竹擊而囤。"),
("翈","xiá",F,"从羽甲聲：翮上短羽（《廣韻》），羽瓣。","x取续消：羽短而续。"),
("閘","yā",F,"从門甲聲：開閉門也（《說文》）；今指船閘（水門）。","y「远渊」取「远」：門閉而远。"),
("庘","yā",F,"从广甲聲：壞屋（《集韻》）；一曰豕屋。","y取远渊：屋壞而远。"),
("舺","xiá",F,"从舟甲聲：䒀舺，舟也（《集韻》）。","x取续消：舟小而续。"),
("胛","jiǎ",F,"从肉甲聲：背胛（《廣韻》），肩胛骨。","j「聚决」取「聚」：骨合而决。"),
("岬","jiǎ",F,"从山甲聲：山旁也（《玉篇》），兩山之間；今指突入海之尖形陸地。","j取聚决：山夾而决。"),
("䆘","yā",F,"从穴甲聲：入衇刺穴（《說文》），針刺穴位。","y取远渊：刺穴而远。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"皆甲支：甲為硬殼、逼窄，故草木多貌、言多、羽短、門閉、山夾皆取「逼窄而合」一面；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":567,"name":"七"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lqi3-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第567部「七部」（卷九十四 七）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡567c2026-10-24","risk":"low","claims":cl},open(r"intake\20261024-字卡567c.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261024-字卡567c.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))