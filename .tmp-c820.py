import json,subprocess,os,glob,re
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
F1="【第576部「來部」·脊支】脊＝从𠦬（背肉）从肉，背中縫（《說文》「背呂也」），象肋骨相連；引申山脊、理。"
F2="【第576部「來部」·𠩺支】𠩺＝从攵从𠩺（犂地起土），治也、理也；引申福、理、寡婦。"
N="字形：古文字字形库未收。"
D=[("脊","jǐ",F1,"从𠦬从肉：背呂也（《說文》），背脊；引申山脊、條理。","j「聚决」取「聚」：骨聚而决。"),
("膌","jí",F1,"从肉脊聲：瘦也（《說文》「膌，瘦也」），瘦瘠。","j取聚决：肉瘦而决。"),
("鯽","jì",F1,"从魚脊聲：魚名（《說文》），鯽魚。","j取聚决：魚聚而决。"),
("塉","jí",F1,"从土脊聲：薄土也（《說文》「塉，薄土也」），瘠薄之地。","j取聚决：土薄而决。"),
("嵴","jí",F1,"从山脊聲：山脊（《集韻》），山頂脊線。","j取聚决：山高而决。"),
("蹐","jí",F1,"从足脊聲：小步也（《說文》引《詩》「不敢不蹐」）。","j取聚决：步小而决。"),
("鶺","jí",F1,"从鳥脊聲：鶺鴒（《集韻》），水鳥。","j取聚决：鳥飛而决。"),
("釐","lí",F2,"从里𠩺聲：家福也（《說文》），理也、福也；又度量單位。","l「拢离」取「离」：理析而离。"),
("嫠","lí",F2,"从女𠩺聲：無夫也（《說文》「無夫也」），寡婦。","l取拢离：女寡而离。"),
("剺","lí",F2,"从刀𠩺聲：剝也（《說文》「剺，剝也」），劃開。","l取拢离：刀劃而离。"),
("漦","chí",F2,"从水𠩺聲：順流也（《說文》），魚涎、唾沫。","ch「刺持」取「刺」：水滲而刺。"),
("犛","lí",F2,"从牛𠩺聲：牛名（《說文》），犛牛（牦牛）。","l取拢离：牛行而离。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"脊支取「背脊相連、瘠薄」一面：脊、膌、鯽、塉、嵴、蹐、鶺；𠩺支取「治地起土、理析」一面：釐、嫠、剺、漦、犛；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":576,"name":"來"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"llai3-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第576部「來部」（卷九十四 七）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
p=r"intake\20261024-字卡576b.json"
for it in range(10):
    json.dump({"schema_version":1,"intent":f"字卡576b{it}-2026-10-24","risk":"low","claims":cl},open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    out=run("knowledge-plan","capture","--file",p,"--format","json")
    if "PLAN_DUPLICATE" not in out:
        print("ok claims",len(cl)); break
    idx=int(re.search(r"claims\[(\d+)\]",out).group(1)); print("drop",cl[idx]["title"]); cl.pop(idx)
bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))