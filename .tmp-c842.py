import json,subprocess,os,glob,re
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
F="【第582部「小部」·肖支】肖＝从肉小聲（骨肉相似），引申像、似；其字族多从肖聲，取「細小、相似、散盡、高遠」諸面。"
N="字形：古文字字形库未收。"
D=[("銷","xiāo",F,"从金肖聲：鑠金也（《說文》「銷，鑠金也」），熔化、消歇。","x「续消」取「消」：金化而消。"),
("霄","xiāo",F,"从雨肖聲：雨䨘也（《說文》），雲霄、高空。","x取续消：氣高而消。"),
("悄","qiǎo",F,"从心肖聲：憂也（《說文》「悄，憂也」），又悄然（靜）。","x取续消：心憂而消。"),
("逍","xiāo",F,"从辵肖聲：逍遙（《集韻》），優游自得。","x取续消：行遠而消。"),
("硝","xiāo",F,"从石肖聲：硝石（《集韻》），硝石、芒硝。","x取续消：石散而消。"),
("琑","suǒ",F,"从玉肖聲：瑣之或體（《集韻》），細碎、鎖。","s「失收」取「收」：碎小而收。"),
("娋","shào",F,"从女肖聲：小娋（《集韻》），女小而美。","sh取失收：女小而收。"),
("睄","qiáo",F,"从目肖聲：小視也（《集韻》），瞧之或體。","q「亲缺」取「亲」：視近而亲。"),
("潲","shào",F,"从水肖聲：雨濺也（《集韻》），潲水、雨斜打。","sh取失收：水濺而收。"),
("痟","xiāo",F,"从疒肖聲：酸痟，頭痛（《說文》「痟，酸痟，頭痛」），消渴病。","x取续消：病瘦而消。"),
("削","xiāo",F,"从刀肖聲：析也（《說文》「削，析也」），削刮、刪削。","x取续消：削薄而消。"),
("鞘","qiào",F,"从革肖聲：刀室也（《集韻》），刀鞘、鞭鞘。","q取亲缺：刀藏而亲。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"肖支同取「細小、相似、消盡、高遠」一面：銷化金、霄雲、悄憂、逍遊、硝石、琑碎、娋小、睄視、潲濺、痟瘦、削析、鞘藏；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":582,"name":"小"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lxiao2-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第582部「小部」（卷九十六 雀）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
p=r"intake\20261024-字卡582b.json"
for it in range(10):
    json.dump({"schema_version":1,"intent":f"字卡582b{it}-2026-10-24","risk":"low","claims":cl},open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    out=run("knowledge-plan","capture","--file",p,"--format","json")
    if "PLAN_DUPLICATE" not in out:
        print("ok claims",len(cl)); break
    idx=int(re.search(r"claims\[(\d+)\]",out).group(1)); print("drop",cl[idx]["title"]); cl.pop(idx)
bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))