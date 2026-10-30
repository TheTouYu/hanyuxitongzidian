import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
FX="【第529部「相部」】相＝从目从木，觀木度材（戴侗《六書故》），轉義省視、形貌、共與交互、輔助；音源借音，義同「向」。"
FS="【第530部「爽部」】爽（𠁊𠙠）＝甲骨文象人兩手各提大的器物之形：一表孔武有力、豪爽（《廣韻》「烈也、猛也」），二表所提為空疏之器（與「希」所从同）；轉義器物空疏→明亮（《說文》「明也」）；器物過大提時與兩足刮擦→傷、損（《廣雅》「傷也、敗也」）。音源借音：兩側有物相夾，義音同「相」。字族：①空明 ②刮擦。"
N="字形：古文字字形库未收。"
D=[("𧡮","shǎng",FX,"《字彙補》「信也」。","sh「失收」取「收」：信實而收。"),
("𠷹","shuǎng",FX,"同「爽」（《漢典》）；《廣雅》「爽，敗也」。","sh取失收：爽敗而收。"),
("𤭪","shuǎng",FX,"㼽之或體：半瓦（《集韻》）；又用碎瓦石沖刷去垢。","sh取失收：瓦碎而收。"),
("𤷼","xiāng",FX,"《玉篇》「𤷼疾也」。","x「续消」取「续」：疾連而續。"),
("𪂼","xiāng",FX,"《玉篇》音相，鳥名；《正字通》「鸉字之譌」。","x取续消：鳥名而續。"),
("爽","shuǎng",FS,"象人兩手提大器：孔武豪爽／器空粗疏；引申明亮、傷損。","sh取失收：氣爽而收。"),
("鷞","shuāng",FS,"从鳥爽聲：鷫鷞，西方候鳥，來時桑落霜降（《說文》）。","sh取失收：候鳥而收。"),
("慡","shuǎng",FS,"从心爽聲：性明也（《集韻》），性格爽朗。","sh取失收：心明而收。"),
("漺","shuǎng",FS,"从水爽聲：淨也、冷也（《玉篇》），水清皃。","sh取失收：水淨而收。"),
("塽","shuǎng",FS,"从土爽聲：地髙明處（《字彙》），通作爽。","sh取失收：土高而收。"),
("騻","shuǎng",FS,"从馬爽聲：驌驦，良馬名（《集韻》）。","sh取失收：馬駿而收。"),
("㼽","chuǎng",FS,"从瓦爽聲：用瓦石搓磨去垢（《說文》）；又半瓦。","ch「刺持」取「持」：磨擦而持。")]
for ch,p,F0,xp,sm in D:
    bn=529 if ch in "𧡮𠷹𤭪𤷼𪂼" else 530
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"相部餘字與爽系諧聲字分三面：空明（慡／漺／塽）／刮擦傷損（㼽／𤭪）／鳥馬之名（鷞／騻／𪂼）；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":bn,"name":"相" if bn==529 else "爽"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lshuang-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}（{p}）＝{xp}",
 "boundary":"源自《系統漢語》第529－530部（卷八十八 昜）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡530a2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡530a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡530a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))