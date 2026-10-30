import json,subprocess,os,glob,re
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
F="【第578部「𠦒部」】𠦒＝甲骨文象有長柄的網兜（田網），「畢」之初文；引申終盡、遮蔽、阻止、盡備；又因網形似箕，分化為畢、離、卓、禽；音源為用畢捕獵時的風聲（古畢、必通用）。"
N="字形：古文字字形库未收。"
D=[("𠦒","bān",F,"象長柄網兜形（《說文》作「箕屬」析形不確），畢之初文。","b「闭剥」取「闭」：網掩而闭。"),
("畢","bì",F,"从又持𠦒：田网也（《說文》），掩兔鳥→盡、完畢；又星宿名。","b取闭剥：網覆而闭。"),
("罼","bì",F,"从网畢聲：罔小而長柄（《玉篇》），兔罟。","b取闭剥：網密而闭。"),
("篳","bì",F,"从竹畢聲：藩落也（《說文》引《春秋傳》「篳門圭窬」），竹籬。","b取闭剥：籬遮而闭。"),
("蓽","bì",F,"从艸畢聲：以荊為戶（《玉篇》）；又蓽菎（羊蹄）、蓽茇（藥名）。","b取闭剥：草蔽而闭。"),
("㪤","bì",F,"从攴畢聲：㪤盡也（《說文》），終盡；又召使疾行。","b取闭剥：盡而闭。"),
("𨢡","bì",F,"从酉畢聲：搗榆醬也（《說文》），榆仁醬（可殺蟲下氣）。","b取闭剥：醬釀而闭。"),
("䟆","bì",F,"从走畢聲：止行也（《說文》），帝王出行清道（蹕）。","b取闭剥：禁止而闭。"),
("韠","bì",F,"从韋畢聲：蔽膝（《說文》「韠，蔽膝也」），胡服蔽膝。","b取闭剥：掩膝而闭。"),
("縪","bì",F,"从糸畢聲：冠縫也（《玉篇》），又止也（通「必」）。","b取闭剥：縫合而闭。"),
("嗶","bì",F,"从口畢聲：嗶嗶（《集韻》），聲也；嗶嘰（織物）。","b取闭剥：聲促而闭。"),
("㓖","bì",F,"从冫畢聲：寒也（《集韻》），風寒。","b取闭剥：寒收而闭。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"𠦒部同取「長柄網兜掩取、終盡遮蔽」一面：畢田網、罼兔罟、篳竹籬、蓽荊戶、㪤盡、𨢡榆醬、䟆清道、韠蔽膝、縪冠縫、嗶聲、㓖寒；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":578,"name":"𠦒"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lban-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第578部「𠦒部」（卷九十五 離）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
p=r"intake\20261024-字卡578a.json"
for it in range(10):
    json.dump({"schema_version":1,"intent":f"字卡578a{it}-2026-10-24","risk":"low","claims":cl},open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    out=run("knowledge-plan","capture","--file",p,"--format","json")
    if "PLAN_DUPLICATE" not in out:
        print("ok claims",len(cl)); break
    idx=int(re.search(r"claims\[(\d+)\]",out).group(1)); print("drop",cl[idx]["title"]); cl.pop(idx)
bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))