import json,subprocess,os,glob,re
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
F="【第569部「黍部」】黍＝禾穗長而粒散，黏者可釀酒；字族多以「黎」表音，義取離（色黃黑）、黏滯、犁耕。"
N="字形：古文字字形库未收。"
D=[("痢","lì",F,"从疒利聲：瀉痢也（《玉篇》），痢疾，濕熱積滯所致。","l「拢离」取「离」：瀉下而离。"),
("黧","lí",F,"从黑利聲：黑而黃也（《廣韻》），面色黧黑。","l取拢离：色黑而离。"),
("睝","lí",F,"从目黎聲：目閉也（《集韻》）。","l取拢离：目合而离。"),
("䴻","lí",F,"从麥黎聲：𪌈䴻，餅也（《廣韻》），乾糧。","l取拢离：餅實而离。"),
("鬁","lì",F,"从髟利聲：鬎鬁（《漢典》），禿髮瘡，狀如被犁過之地。","l取拢离：髮落而离。"),
("鋫","lí",F,"从金利聲：鑗，黑金也（《集韻》），或作鋫。","l取拢离：金黑而离。"),
("琍","lí",F,"从玉利聲：同「璃」（《篇海類編》），玻璃。","l取拢离：玉莹而离。"),
("唎","lì",F,"从口利聲：聲也（《玉篇》），梵書呪語多唎字。","l取拢离：聲細而离。"),
("峲","lǐ",F,"从山利聲：峛字之譌（《正字通》），山逐行也。","l取拢离：山列而离。"),
("筣","lì",F,"从竹利聲：笓筣，織竹為障（《集韻》），籬笆。","l取拢离：竹編而离。"),
("𢤂","lí",F,"从心黎聲：恨也（《說文》），一曰怠也。","l取拢离：心怠而离。"),
("𠠍","lí",F,"从刀黎聲：直破也（《玉篇》）。","l取拢离：破直而离。"),
("𥌛","lí",F,"从目黎聲：視也（《集韻》）。","l取拢离：視察而离。"),
("𧬠","chī",F,"从言黎聲：䜉之譌（《字彙補》），相問不知答曰誺。","ch「刺持」取「持」：問答而持。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"黍部余字同取「黎（離）之黏、黑、分」一面：痢瀉、黧黑、睝閉、䴻餅、鬁禿、鋫黑金、琍璃、唎聲、峲山、筣籬、𢤂怠、𠠍破、𥌛視、𧬠問答；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":569,"name":"黍"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lshu2-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第569部「黍部」（卷九十四 七）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
p=r"intake\20261024-字卡569c.json"
for it in range(8):
    json.dump({"schema_version":1,"intent":f"字卡569c{it}-2026-10-24","risk":"low","claims":cl},open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    out=run("knowledge-plan","capture","--file",p,"--format","json")
    if "PLAN_DUPLICATE" not in out:
        print("ok claims",len(cl)); break
    idx=int(re.search(r"claims\[(\d+)\]",out).group(1)); print("drop",cl[idx]["title"]); cl.pop(idx)
bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))