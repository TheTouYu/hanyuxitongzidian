import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
N="字形：古文字字形库未收。"
D=[("氱","yǎng","【第525部「昜部」】古「氧」字，从气昜聲，化學元素之舊譯。","从气昜聲：氧氣之舊譯。","y「圆容」取「圆」：氣周而充。",525),
("輰","yáng","【第525部「昜部」】昜＝从日从丂，日出呼號；字族取日升轉動一面。","从車昜聲：輰䡵，柳車（喪車）（《博雅》）。","y取圆容：車轉而周。",525),
("鸉","yáng","【第525部「昜部」】昜＝从日从丂，日出；字族取白亮一面。","从鳥昜聲：白鷢，似鷹而尾上白（《爾雅》）。","y取圆容：鳥白而圓。",525),
("量","liáng","【第525部「昜部」·量系（二级字根）】量＝从東昜聲：「東」為掏空之木鼓、即斗，「昜」為飛舉；象用斗稱量。轉義：稱輕重→測長短、商榷。辨證：《說文》「从重省、曏省聲」所據小篆已訛。字族二面：稱量／形近畺之訛。","从東（斗）昜聲：用斗稱量，引申稱輕重、度量。","l「拢离」取「离」：斗量而分。",525),
("糧","liáng","【第525部「昜部」·量系】量＝斗量，糧从米量聲，取稱量計功一面。","从米量聲：穀米；廩祿之穀，以酌量功次。","l取拢离：米量而分。",525),
("𤎲","hū","【第525部「昜部」·量系】此字楷化有誤，省去「鬲」與聲符「勹」；原从尞从東从勹在鬲中。","从火：火煨也（《篇海》）；原象以斗量物入鬲而炊。","h「豁活」取「活」：火煨而活。",525),
("𪋥","jīng","【第525部「昜部」·量系】量系字，形近「畺」而訛。","同「麠」：大麃，牛尾一角（《爾雅》）。","j「聚决」取「聚」：獸聚而角。",525),
("𡑆","jiāng","【第525部「昜部」·量系】量系字，形近「畺」而訛。","同「疆」：田界、疆土。","j取聚决：界聚而分。",525),
("昌","chāng","【第526部「昌部」】昌＝甲骨文从日从口：對日叫喚（古老拜日儀式），與「昜」同意；引申昌盛、美言。","从日从口：對日呼唱，引申昌盛、倡始。","ch「刺持」取「持」：日升而持。",526),
("唱","chàng","【第526部「昌部」】昌＝从日从口，對日呼唱；唱从口昌聲，取發聲一面。","从口昌聲：導也、發歌（《說文》）。","ch取刺持：歌發而持。",526),
("倡","chàng","【第526部「昌部」】昌＝對日呼唱；倡从人昌聲，取倡始、樂人一面。","从人昌聲：樂也、倡優、倡導（《說文》）。","ch取刺持：人倡而持。",526),
("娼","chāng","【第526部「昌部」】昌＝對日呼唱，引申歌樂；娼从女昌聲，取倡女一面。","从女昌聲：倡女、娼妓。","ch取刺持：女樂而持。",526)]
for ch,p,F0,xp,sm,bn in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同部同族諧聲字各取一面：量系取「斗量計功」（量／糧／𤎲）、形近畺之訛（𪋥／𡑆）；昌系取「對日呼唱」（昌／唱／倡／娼）；只列同部字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":bn,"name":"昜" if bn==525 else "昌"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lyang7-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}（{p}）＝{xp}",
 "boundary":("源自《系統漢語》第525部「昜部」"+("·量系" if ch in "量糧𤎲𪋥𡑆" else "")+"（卷八十八 昜）；字卡五步规程。") if bn==525 else "源自《系統漢語》第526部「昌部」（卷八十八 昜）；字卡五步规程。",
 "permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm,bn) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡525e2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡525e.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡525e.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))