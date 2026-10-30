import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
F="【第567部「七部」】七＝从一加指示符（切、刻之初文）；字族二义：甲（甲胄、硬殼，穿甲状之逼窄）／桼（割樹取汁，漆之初文；與朱同源）／皂（橡實之房，黑色）。"
N="字形：古文字字形库未收。"
D=[("甲","jiǎ",F,"象護身硬殼（龜甲、甲蟲之甲）：鎧甲、甲胄；引申首位（天干第一）、指甲狀逼窄之物。","j「聚决」取「聚」：甲合而决。"),
("狎","xiá",F,"从犬甲聲：犬可習也（《說文》「犬可習也」），親近、輕忽。","x「续消」取「续」：犬習而续。"),
("鴨","yā",F,"从鳥甲聲：鶩也，俗謂之鴨（《說文》），嘴扁腳矮、趾間有蹼。","y「远渊」取「远」：水禽而远。"),
("呷","xiá",F,"从口甲聲：吸呷也（《說文》「吸呷也」），吸食聲；甲有斂藏義。","x取续消：吸斂而续。"),
("押","yā",F,"从手甲聲：署也、按也（《玉篇》《集韻》），簽署、壓按、拘禁。","y取远渊：按壓而远。"),
("匣","xiā",F,"从匚甲聲：匱也（《說文》「匱也」），收藏器物之箱。","x取续消：藏斂而续。"),
("柙","xiá",F,"从木甲聲：檻也，以藏虎兕（《說文》），關養禽獸之木籠。","x取续消：籠藏而续。"),
("鉀","jiǎ",F,"从金甲聲：鎧屬（《廣韻》「鎧屬」），鎧甲；盛酒銅扁壺。","j取聚决：甲堅而决。"),
("桼","qī",F,"从木兩側加點：割樹皮取汁（與「朱」同源），漆之初文（《說文》「木汁」）；引申赤黑、塗漆。","q「亲缺」取「亲」：汁黏而亲。"),
("漆","qī",F,"从水桼聲：水名（《說文》漆水），因岸盛產漆樹得名；又通「桼」，塗漆。","q取亲缺：水黏而亲。"),
("膝","xī",F,"从卩桼聲：脛頭卩也（《說文》），膝蓋；指其有窩如割漆之口（《釋名》「膝，伸也」）。","x取续消：屈伸而续。"),
("皂","zào",F,"从白从七：橡實之房（𠧪訛為白），櫟實曰皂斗；引申黑色（可染帛）。","z「凿总」取「总」：實聚而总。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"七部三支同取「切刻所成之殼、汁、實」一面：甲胄類（狎、鴨、呷、押、匣、柙、鉀）、取汁類（桼、漆、膝）、橡實類（皂）；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":567,"name":"七"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lqi2-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第567部「七部」（卷九十四 七）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡567b2026-10-24","risk":"low","claims":cl},open(r"intake\20261024-字卡567b.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261024-字卡567b.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))