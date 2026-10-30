import json,subprocess,os,glob,re
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
F="【第587部「幺部」】幺＝象蠶吐絲（兩股相交）；幼支＝从力幺聲：少也（《說文》），引申 嫩弱、精微、柔曲；本批取「半乾蜷曲、地不平、面醜頸僵」等柔曲細弱一面。"
N="字形：古文字字形库未收。"
D=[("㶭","yǒu",F,"从火幼聲：㶭炄，欲乾（《集韻》）；半乾而蜷曲。","y「续消」取「续」：火乾而续。"),
("𠢢","yǒu",F,"从力幼聲：𠢢𥍳，輭也（《集韻》），柔弱。","y取续消：力弱而续。"),
("𡛙","yǎo",F,"从女幼聲：偠㒟，美皃（《集韻》）；𡛙嫪，不順。","y取续消：女柔而续。"),
("𣧥","yǒu",F,"从歹幼聲：𣧥𣧊，欲死（《集韻》），扭曲掙扎。","y取续消：殘而续。"),
("𥁒","yào",F,"从皿幼聲：器中不平（《集韻》）。","y取续消：器凹而续。"),
("𥑑","ào",F,"从石幼聲：石不平也（《正字通》），通作凹。","a「隔估」取「隔」：石凹而隔。"),
("坳","ào",F,"从土幼聲：地不平也（《說文新附》），地窊下；轉角處亦名坳。","a取隔估：地凹而隔。"),
("𥬓","yào",F,"从竹幼聲：竹節（《篇海》）。","y取续消：竹節而续。"),
("𩈏","yǒu",F,"从面幼聲：𩈏𩈸，面醜（《集韻》）；又面曲。","y取续消：面曲而续。"),
("𩑴","yào",F,"从頁幼聲：頸不隨也（《集韻》），頸項轉動不自如。","y取续消：頸僵而续。"),
("𩢒","yǎo",F,"从馬幼聲：馬驂也（《字彙》），駕在車兩旁的馬。","y取续消：馬傍而续。"),
("𪊛","yōu",F,"从鹿幼聲：同麀（《字彙》），牝鹿。","y取续消：鹿牝而续。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"幼支余字同取「柔曲、细弱、不平」一面：㶭半乾、𠢢柔弱、𡛙美皃、𣧥欲死、𥁒器凹、𥑑石凹、坳地凹、𥬓竹節、𩈏面曲、𩑴頸僵、𩢒驂馬、𪊛牝鹿；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":587,"name":"幺"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lyao3-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第587部「幺部」（卷九十六 雀）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
p=r"intake\20261024-字卡587c.json"
for it in range(10):
    json.dump({"schema_version":1,"intent":f"字卡587c{it}-2026-10-24","risk":"low","claims":cl},open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    out=run("knowledge-plan","capture","--file",p,"--format","json")
    if "PLAN_DUPLICATE" not in out:
        print("ok claims",len(cl)); break
    idx=int(re.search(r"claims\[(\d+)\]",out).group(1)); print("drop",cl[idx]["title"]); cl.pop(idx)
bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))