import json,subprocess,os,glob,re
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
F="【第578部「𠦒部」】𠦒＝長柄網兜，畢之初文；字族多从畢聲，取「掩取、終盡、蔽塞」諸面。"
N="字形：古文字字形库未收。"
D=[("㮿","bì",F,"从木畢聲：木名（《集韻》），可為器。","b「闭剥」取「闭」：木實而闭。"),
("𤹝","bì",F,"从疒畢聲：病也（《集韻》），腳氣之疾。","b取闭剥：疾閉而闭。"),
("𡻞","bì",F,"从山畢聲：山貌（《集韻》），山勢連延。","b取闭剥：山蔽而闭。"),
("𥛘","bì",F,"从示畢聲：祭名（《集韻》），禱祀。","b取闭剥：祭閉而闭。"),
("鏎","bì",F,"从金畢聲：鐵也（《集韻》），金屬器。","b取闭剥：金堅而闭。"),
("𡠚","bì",F,"从女畢聲：女字（《集韻》），女子名用字。","b取闭剥：女静而闭。"),
("襅","bì",F,"从衣畢聲：蔽膝之衣（《集韻》），與韠同。","b取闭剥：衣掩而闭。"),
("㻫","bì",F,"从玉畢聲：佩刀下飾（《說文》作「珌」），玉飾。","b取闭剥：玉飾而闭。"),
("鷝","bì",F,"从鳥畢聲：鳥名（《集韻》），似雉。","b取闭剥：鳥掩而闭。"),
("熚","bì",F,"从火畢聲：火貌（《集韻》），火光。","b取闭剥：火爆而闭。"),
("滭","bì",F,"从水畢聲：泉湧出貌（《集韻》），滭沸。","b取闭剥：泉湧而闭。"),
("饆","bì",F,"从食畢聲：饆饠（《集韻》），餅屬。","b取闭剥：食裹而闭。"),
("彃","bì",F,"从弓畢聲：射也（《說文》「彃，射也」），弓射。","b取闭剥：弓張而闭。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"畢聲諸字同取「掩取、蔽塞」一面：㮿木、𤹝病、𡻞山、𥛘祭、鏎金、𡠚女、襅衣、㻫玉、鷝鳥、熚火、滭泉、饆餅、彃射；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":578,"name":"𠦒"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lban2-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第578部「𠦒部」（卷九十五 離）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
p=r"intake\20261024-字卡578b.json"
for it in range(10):
    json.dump({"schema_version":1,"intent":f"字卡578b{it}-2026-10-24","risk":"low","claims":cl},open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    out=run("knowledge-plan","capture","--file",p,"--format","json")
    if "PLAN_DUPLICATE" not in out:
        print("ok claims",len(cl)); break
    idx=int(re.search(r"claims\[(\d+)\]",out).group(1)); print("drop",cl[idx]["title"]); cl.pop(idx)
bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))