import json,subprocess,os,glob,re
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
F1="【第571部「力部」·耒支／耤支】耒＝手耕曲木；耤＝持耒耕作（借助、踐踏、狼藉）。"
F2="【第572部「歺部」】歺（歹）＝象中空而破裂的骨形（从半冎），殘骨；引申垂死、不好、死亡；音源為刮骨聲。"
N="字形：古文字字形库未收。"
D=[("䣂","lèi",F1,"从邑耒聲：今桂陽耒陽縣（《說文》），湖南耒陽市，傳說神農在此創耒。","l「拢离」取「离」：邑分而离。"),
("洡","lěi",F1,"从水耒聲：耒陽縣（《集韻》），又浸染。","l取拢离：水染而离。"),
("銇","lèi",F1,"从金耒聲：鑽也（《廣韻》），平版具。","l取拢离：鑽金而离。"),
("𠛨","chì",F1,"从刀丯聲：割聲（《篇海》），剨之或體（耒本从丯）。","ch「刺持」取「刺」：割裂而刺。"),
("𥨱","qiè",F1,"从穴竊省：俗竊字（《正字通》），偷竊。","q「亲缺」取「亲」：私取而亲。"),
("筙","lái",F1,"从竹來聲：古同箂（《漢典》），竹名，疑訛字。","l取拢离：竹列而离。"),
("𥅦","lèi",F1,"从目耒聲：目不正也（《集韻》），俗睞字。","l取拢离：目斜而离。"),
("𤁏","zī",F1,"从水耤聲：同資（《漢典》），水名。","z「凿总」取「总」：水聚而总。"),
("𤅔","jù",F1,"从水沮聲：同沮（《字海》），濕潤。","j「聚决」取「聚」：水聚而决。"),
("躤","jí",F1,"从足耤聲：踐也（《集韻》），踐踏。","j取聚决：足踏而决。"),
("歺","è",F2,"从半冎：中空破裂之殘骨（《說文》「𠛱骨之殘也」），引申垂死、不好（俗作歹）、死亡。","e「?」取骨声。"),
("𣧻","càn",F2,"从歺从肉：禽獸所食餘也（《說文》），殘餘。","c「刺持」取「持」：殘餘而持。"),
("𣧚","shí",F2,"从歺从十：義闕（《字彙補》），同𣧻。","sh「失收」取「收」：餘骨而收。"),
("㱛","chuǎn",F2,"从歺从歹：殘也、盡也（《字彙》），古布字。","ch取刺持：殘盡而持。")]
for ch,p,F0,xp,sm in D:
    num=571 if "第571部" in F0 else 572
    nm="力" if num==571 else "歺"
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"耒／耤支取「耕作所出」（邑、水、金、割、竊、竹、目、水、足）；歺部取「殘骨」（殘餘、義闕、殘盡）；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":num,"name":nm}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"llei2-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":f"源自《系統漢語》第{571 if '第571部' in F0 else 572}部「{'力' if '第571部' in F0 else '歺'}部」（卷九十四 七）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
p=r"intake\20261024-字卡572a.json"
for it in range(10):
    json.dump({"schema_version":1,"intent":f"字卡572a{it}-2026-10-24","risk":"low","claims":cl},open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    out=run("knowledge-plan","capture","--file",p,"--format","json")
    if "PLAN_DUPLICATE" not in out:
        print("ok claims",len(cl)); break
    idx=int(re.search(r"claims\[(\d+)\]",out).group(1)); print("drop",cl[idx]["title"]); cl.pop(idx)
bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))