import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
F="【第534部「爿部」·壯系】壯＝从士爿聲，《說文》「大也」；爿（床）为声，取「床板长大平整」之义；转义壮盛、壮年。"
N="字形：古文字字形库未收。"
D=[("壯","zhuàng",F,"从士爿聲：大也（《說文》），人體高大、年富力強。","z「凿总」取「凿」：体壮如凿实。"),
("莊","zhuāng",F,"从艸从壯：草盛貌（《玉篇》），引申莊敬、六達之道（莊／庄）。","z取凿总：草壮而总。"),
("奘","zàng",F,"从大从壯，壯亦聲：駔大也（《說文》），粗大、健。","z取凿总：大而总。"),
("裝","zhuāng",F,"从衣壯聲：裹也（《說文》），包裹、行囊、裝束、假裝。","z取凿总：衣裹而总。"),
("匨","zāng",F,"臧之古作：善也（《說文》），又通藏（匿也）。","z取凿总：藏而总。"),
("銺","zàng",F,"《集韻》「鈴聲」；《正字通》以为譌字。","z取凿总：铃振而总。"),
("焋","zhuàng",F,"《集韻》「實米于甑」；今炊粉餈謂之焋糕。","z取凿总：蒸實而总。"),
("梉","zhuāng",F,"《集韻》「木名，似豫章」，其小似桃，生七年乃知。","z取凿总：木坚而总。"),
("糚","zhuāng",F,"妝之或作：飾也（《說文》），粉饰。","z取凿总：飾而总。"),
("㮜","zāng",F,"《字彙》「木版盛物也」，木板做成的盛器。","z取凿总：版盛而总。"),
("狀","zhuàng",F,"从犬爿聲：犬形也（《說文》），狗的样子；引申描摹、陳述、文書。","zh「刺持」取「持」：犬形而持。"),
("妝","zhuāng",F,"从女牀省聲：飾也（《說文》），女子以花飾容。","zh取刺持：女飾而持。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"壯系同取「长大、盛实」一面：壯言人体、莊言草盛、奘言粗大、裝言包裹、狀言犬形；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":534,"name":"爿"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lzhuang-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"字卡（第534部壯系）：{xp}",
 "boundary":"源自《系統漢語》第534部「爿部」（卷八十九 象）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡534z2026-10-24","risk":"low","claims":cl},open(r"intake\20261024-字卡534z.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261024-字卡534z.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))