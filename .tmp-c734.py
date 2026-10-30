import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
FH="【第551部「亦部」】亦＝从大（人）腋下加兩點，指腋下，為「腋」之初文；借為「也」，另造夜／腋／掖／液諸字。"
N="字形：古文字字形库未收。"
D=[("亦","yì",FH,"从大（正面人形）腋下加两点，指腋下（《说文》「人之臂亦也」）；借为副词「也」。","y 喻母「续消」取「续」：气续而消。"),
("夜","yè",FH,"从夕亦聲：舍也（《說文》「夜，舍也。天下休舍也」），與「夕」同源。","y取续消：日消而续。"),
("腋","yè",FH,"从肉夜聲：人之臂亦也（《說文》「臂下也」），胳肢窩。","y取续消：臂下气续。"),
("掖","yè",FH,"从手夜聲：以手持人臂（《說文》「以手持人臂投地也」），扶掖、掖門。","y取续消：手扶而续。"),
("液","yè",FH,"从水夜聲：津也（《說文》「津也」），流體。","y取续消：水续而消。"),
("奕","yì",FH,"从大亦聲：大也（《說文》「大也」），美盛、奕奕。","y取续消：大而续。"),
("帟","yì",FH,"从巾亦聲：在上曰帟（《說文》「在上曰帟」），小幕。","y取续消：幕覆而续。"),
("弈","yì",FH,"从廾亦聲：圍棋也（《說文》「圍棊也」）。","y取续消：局续而消。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"亦系同取「腋下兩點、旁出」一面：夜舍、腋臂下、掖持臂、液津、奕大、帟幕、弈棋；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":551,"name":"亦"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lyi-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第551部「亦部」（卷九十一 火）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡551a2026-10-24","risk":"low","claims":cl},open(r"intake\20261024-字卡551a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261024-字卡551a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))