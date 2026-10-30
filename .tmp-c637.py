import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
FL="【第521部「良部」】良＝甲骨文象口之上下各有兩獠牙，為「狼」之初文；轉義狼崇拜→善美；辯證牙形小篆訛作「亡」，《說文》「从亯省亡聲」析形不確；音源為狼嚎聲。字族分「遊蕩／嚎叫／獠牙銳長／眼露凶光／狼尾狀」五面。"
N="字形：古文字字形库未收。"
D=[("㝗","lǎng",FL,"从宀良聲：屋宇空闊（《說文》「㝩也」）。","l「拢离」取「拢」：屋空而攏。"),
("郎","láng",FL,"从邑良聲：魯亭（《說文》），引申男子之稱、郎君。","l取拢离：邑聚而攏。"),
("廊","láng",FL,"从广郎聲：中堂兩旁之牆、堂下周屋（《說文》「東西序也」），引申走廊。","l取拢离：屋列而離。"),
("閬","làng",FL,"从門良聲：門高（《說文》），又空曠、寬明。","l取拢离：門高而離。"),
("朗","lǎng",FL,"从月良聲：明也（《說文》）——狼眼夜放綠光，故取明亮。","l取拢离：月明而朗。"),
("烺","lǎng",FL,"从火良聲：爣烺，火貌（《集韻》）。","l取拢离：火明而烺。"),
("莨","láng",FL,"从艸良聲：狼尾艸，似茅可覆屋（《說文》「艸也」）；又莨菪。","l取拢离：草叢而攏。"),
("稂","láng",FL,"从禾良聲：秕穀、惡草似莠（《說文》），穗如狼尾。","l取拢离：穗垂而離。"),
("粮","liáng",FL,"从米良聲：穀也（《集韻》），糧之或作——穗如狼尾。","l取拢离：穀聚而攏。"),
("娘","niáng",FL,"从女良聲：少女之號（《集韻》），引申母親（娘娘）。","n「纳弄」取「纳」：女少而納。"),
("駺","láng",FL,"从馬良聲：馬尾白（《玉篇》），吉駺文馬。","l取拢离：馬奔而離。"),
("埌","làng",FL,"从土良聲：墦埌為冢，壙埌為原野迥貌（《集韻》）。","l取拢离：原野而離。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同部諧聲字取「明亮」（朗／烺）、「狼尾草狀」（莨／稂／粮／駺）、「空闊」（㝗／郎／廊／閬／埌）、「女子」（娘）；只列本部字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":521,"name":"良"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"liang-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}（{p}）{xp}",
 "boundary":"源自《系統漢語》第521部「良部」（卷八十六 良）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡521b2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡521b.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡521b.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))