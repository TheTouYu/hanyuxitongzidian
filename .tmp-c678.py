import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
FY="【第532部「𨛜部」】𨛜（𠨍）＝甲骨文从兩個相對的跪跽之人，象意相向，為「嚮」的初文（《集韻》「面也」）；轉義兩人相對歇息→親密、侍奉（卿），同一地域之人（鄉）。辯證：戰國古文將跪人形訛作「邑」，小篆承之，《說文》分釋𠨍、𨛜、鄉、卿皆不確；卿、鄉同源，象兩人對食。音源借音：因相對義音同「向」。字族：①相對對食、面對親密 ②對食美味、回聲。"
N="字形：古文字字形库未收。"
D=[("𨛜","xiàng",FY,"甲骨文从两跪跽之人相对，象相向，嚮之初文；引申亲密、乡党。","x「续消」取「续」：相對而續。"),
("鄉","xiāng",FY,"从𨛜皀聲：本指共同飲食的氏族部落，引申行政單位（萬二千五百家為鄉）。","x取续消：眾向而續。"),
("卿","qīng",FY,"从卯皀聲：古代高級官員之稱（《說文》「章也」），秦漢後君呼臣、夫呼妻。","q「亲缺」取「亲」：對食而親。"),
("巷","xiàng",FY,"从𨛜从共：里中道（《說文》），直為街、曲為巷。","x取续消：里道而續。"),
("嚮","xiàng",FY,"从鄉从向：面也，與向通用；又響應、享受。","x取续消：面向而續。"),
("饗","xiǎng",FY,"从食从鄉：鄉人相聚宴飲（《說文》），設盛禮飯賓。","x取续消：宴饗而續。"),
("薌","xiāng",FY,"从艸鄉聲：穀氣（《說文》），亦作香。","x取续消：穀香而續。"),
("曏","xiàng",FY,"从日鄉聲：不久以前（《說文》）；又頃刻，即「晌」。","x取续消：日移而續。"),
("膷","xiāng",FY,"从肉鄉聲：牛羹（《廣韻》），牛之美者、香也。","x取续消：肉香而續。"),
("響","xiǎng",FY,"从音鄉聲：聲也（《說文》），回聲相應。","x取续消：聲應而續。"),
("蠁","xiǎng",FY,"从虫鄉聲：知聲蟲（《說文》），即地蛹、蠛蠓。","x取续消：蟲應聲而續。"),
("𤩬","xiǎng",FY,"从玉鄉聲：珦之或體，玉也（《集韻》）。","x取续消：玉潤而續。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"𨛜系諧聲字分兩面：相對面對（鄉／卿／巷／嚮／𤩬）與對食回聲（饗／薌／曏／膷／響／蠁）；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":532,"name":"𨛜"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lxunj-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"字卡（第532部𨛜）：{xp}",
 "boundary":"源自《系統漢語》第532部「𨛜部」（卷八十八 昜）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡532a2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡532a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡532a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))