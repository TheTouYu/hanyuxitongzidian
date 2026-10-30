import json,subprocess,os,glob,re
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
F="【第571部「力部」】力＝耒之初文（有弧度的樹杈，上加橫木踏足，即「耒」，犁之初文）；引申功勞、力量、能力；《說文》「象人筋之形」析形不確；音源為耒耕時與泥土的摩擦聲。"
N="字形：古文字字形库未收。"
D=[("力","lì",F,"象耒形（曲木加橫木）：耒之初文，引申功勞、力量、能力、費力。","l「拢离」取「离」：耒土而离。"),
("勒","lè",F,"从革力聲：馬頭絡銜也（《說文》），約束、鐫刻；引申以法令控制。","l取拢离：銜勒而离。"),
("扐","lè",F,"从手力聲：筮法以蓍草奇零之數夾指間（《說文》），指間、餘數。","l取拢离：指夾而离。"),
("肋","lèi",F,"从肉力聲：脅骨也（《說文》），《釋名》「肋，勒也，檢勒五臟」。","l取拢离：肋骨而离。"),
("竻","lè",F,"从竹力聲：竹根（《集韻》），在地橫鑽如犁地；又刺竹可作藩籬。","l取拢离：根鑽而离。"),
("劫","jié",F,"从力从去：以力脅止曰劫（《說文》）；本指犁地前拉後扶如爭奪。","j「聚决」取「聚」：力脅而决。"),
("筋","jīn",F,"从力从肉从竹：肉之力也（《說文》），附骨之韌帶；疑本指竹索。","j取聚决：筋韌而决。"),
("阞","lè",F,"从阜力聲：地理也（《說文》），地的脈理、裂開。","l取拢离：地脈而离。"),
("朸","lè",F,"从木力聲：木之理也（《說文》），樹木紋理；又縣名。","l取拢离：木紋而离。"),
("泐","lè",F,"从水从阞：水石之理也（《說文》），石因風化遇水而裂。","l取拢离：石裂而离。"),
("玏","lè",F,"从玉力聲：玪𤨙，石之次玉者（《說文》）。","l取拢离：石潤而离。"),
("鰳","lè",F,"从魚勒聲：鰳魚（《正字通》），狀如鰣魚、腹下有硬刺。","l取拢离：魚刺而离。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"力部①指用耒（勒銜、扐筮、肋脅、竻竹根、劫爭、筋韌、阞地脈、朸木理、泐石裂、玏石玉、鰳魚）；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":571,"name":"力"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lli2-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第571部「力部」（卷九十四 七）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
p=r"intake\20261024-字卡571a.json"
for it in range(8):
    json.dump({"schema_version":1,"intent":f"字卡571a{it}-2026-10-24","risk":"low","claims":cl},open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    out=run("knowledge-plan","capture","--file",p,"--format","json")
    if "PLAN_DUPLICATE" not in out:
        print("ok claims",len(cl)); break
    idx=int(re.search(r"claims\[(\d+)\]",out).group(1)); print("drop",cl[idx]["title"]); cl.pop(idx)
bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))