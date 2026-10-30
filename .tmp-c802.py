import json,subprocess,os,glob,re
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
F="【第572部「歺部」·列支】列＝从刀从𡿪（𡿪指洗骨，骸骨腐後鬆散），从刀表切開使如散架之骸；引申行列、陳列；《說文》「分解也」。"
N="字形：古文字字形库未收。"
D=[("列","liè",F,"从刀从𡿪：分解也（《說文》），切開如散架骸骨；引申行列、位序、陳布。","l「拢离」取「离」：分解而离。"),
("裂","liè",F,"从衣列聲：繒餘也（《說文》），裁衣剩餘之邊角；引申坼破、分裂。","l取拢离：帛裂而离。"),
("蛚","liè",F,"从蟲列聲：蜻蛚（《說文》），蟋蟀之類。","l取拢离：蟲鳴而离。"),
("栵","liè",F,"从木列聲：栭也（《說文》「栭也」），小栗；又行次。","l取拢离：木列而离。"),
("烈","liè",F,"从火列聲：火猛也（《說文》「火猛也」），引申剛正、功業。","l取拢离：火猛而离。"),
("颲","liè",F,"从風列聲：烈風也（《說文》「烈風也」），暴風。","l取拢离：風疾而离。"),
("咧","liě",F,"从口列聲：咧開（《集韻》），嘴角向兩旁伸展。","l取拢离：口張而离。"),
("鴷","liè",F,"从鳥列聲：啄木也（《說文》），啄木鳥。","l取拢离：鳥啄而离。"),
("冽","liè",F,"从水列聲：寒也（《說文》「寒也」），水寒、清冽。","l取拢离：水寒而离。"),
("迾","liè",F,"从辵列聲：遮也（《說文》「遮也」），列隊遮止。","l取拢离：遮列而离。"),
("茢","liè",F,"从艸列聲：苕帚（《說文》），葦花可掃除。","l取拢离：草帚而离。"),
("例","lì",F,"从人列聲：比也（《說文》「比也」），條例、例證。","l取拢离：比列而离。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"列支同取「分解陳列」一面：列分、裂帛、蛚鳴、栵木、烈火、颲風、咧口、鴷啄、冽寒、迾遮、茢帚、例比；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":572,"name":"歺"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"llie-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第572部「歺部」（卷九十四 七）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
p=r"intake\20261024-字卡572b.json"
for it in range(10):
    json.dump({"schema_version":1,"intent":f"字卡572b{it}-2026-10-24","risk":"low","claims":cl},open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    out=run("knowledge-plan","capture","--file",p,"--format","json")
    if "PLAN_DUPLICATE" not in out:
        print("ok claims",len(cl)); break
    idx=int(re.search(r"claims\[(\d+)\]",out).group(1)); print("drop",cl[idx]["title"]); cl.pop(idx)
bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))