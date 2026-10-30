import json,subprocess,os,glob,re
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
F="【第581部「豊部」】豊（lǐ）＝从壴从朋（玉），象禮物（朋、玉）堆疊如鼓；與「豐」同源而側重不同（豐从壴朋聲＝繁飾之鼓，豊从朋壴聲＝堆疊之禮）；轉義 眾而有序；音源本壴聲，義音同「麗」。"
N="字形：古文字字形库未收。"
D=[("豊","lǐ",F,"从壴从朋：行禮之器也（《玉篇》），禮物堆疊；引申眾而有序。","l「拢离」取「离」：禮列而离。"),
("體","tǐ",F,"从骨豊聲：總十二屬也（《說文》），身體；《釋名》「體，第也」（骨肉毛血大小相次第）。","t「涂突」取「突」：骨節而突。"),
("禮","lǐ",F,"从示从豊（豊亦聲）：履也，所以事神致富（《說文》），祭神求福→禮儀、禮物。","l取拢离：禮序而离。"),
("𥴡","lǐ",F,"从竹豊聲：竹名（《廣韻》），似苦竹而細軟，肌薄有文理。","l取拢离：竹列而离。"),
("䪆","tǐ",F,"从韋豊聲：䪆𩋪，軟貌（《廣韻》），柔軟。","t取涂突：皮軟而突。"),
("醴","lǐ",F,"从酉豊聲：酒一宿孰也（《說文》），甜酒；醴泉（美泉可養老）。","l取拢离：酒釀而离。"),
("澧","lǐ",F,"从水豊聲：水名（《說文》「出南陽雉衡山」），湖南澧水。","l取拢离：水行而离。"),
("鱧","lǐ",F,"从魚豊聲：鱯也（《說文》），烏鱧（黑魚）；古人謂其夜仰首向北斗「有自然之禮」。","l取拢离：魚伏而离。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"豊部同取「堆疊有序」一面：體骨節、禮事神、𥴡竹理、䪆柔軟、醴甜酒、澧水、鱧黑魚（首戴北斗之禮）；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":581,"name":"豊"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lli3-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第581部「豊部」（卷九十五 離）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
p=r"intake\20261024-字卡581a.json"
for it in range(10):
    json.dump({"schema_version":1,"intent":f"字卡581a{it}-2026-10-24","risk":"low","claims":cl},open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    out=run("knowledge-plan","capture","--file",p,"--format","json")
    if "PLAN_DUPLICATE" not in out:
        print("ok claims",len(cl)); break
    idx=int(re.search(r"claims\[(\d+)\]",out).group(1)); print("drop",cl[idx]["title"]); cl.pop(idx)
bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))