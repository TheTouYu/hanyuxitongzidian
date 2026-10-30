import json,subprocess,os,glob,re
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
F1="【第576部「來部」·麥支】麥＝从來从夊（倒止），秋種夏熟之芒穀；字族取「麥實、麥皮、麥屑、煮麥」諸面。"
F2="【第577部「制部」】制＝甲骨文从木从刀，象給樹木整枝／砍樹／加工木頭，引申禁止、約束、法度、決斷；春秋金文改从「未」；音源为借音（義音同丯，古制、丯通用）。"
N="字形：古文字字形库未收。"
D=[("麳","lái",F1,"从麥來聲：小麥（《說文》「麳，小麥」），或作䅘。","l「拢离」取「离」：麥穗而离。"),
("麩","fū",F1,"从麥夫聲：小麥皮屑（《說文》「麩，小麥屑皮也」）。","f「附分」取「附」：皮附而分。"),
("麵","miàn",F1,"从麥丏聲：麥屑（《說文》作「麪」），麵食。","m「蒙末」取「末」：屑細而末。"),
("麷","fēng",F1,"从麥豐聲：煮麥也（《說文》「麷，煮麥也」）。","f取附分：麥煮而分。"),
("萊","lái",F1,"从艸來聲：蔓華也（《說文》），藜；又萊田（荒地）。","l取拢离：草蔓而离。"),
("賚","lài",F1,"从貝來聲：賜也（《說文》「賚，賜也」），賞賜。","l取拢离：賜與而离。"),
("棶","lái",F1,"从木來聲：木名（《集韻》），棶木。","l取拢离：木列而离。"),
("騋","lái",F1,"从馬來聲：馬七尺為騋（《說文》），高壯之馬。","l取拢离：馬馳而离。"),
("制","zhì",F2,"从刀从未：裁也（《說文》），整枝→禁止、約束、法度、決斷。","zh「凿总」取「总」：裁斷而总。"),
("製","zhì",F2,"从衣制聲：裁衣也（《說文》「製，裁也」），制作。","zh取凿总：裁衣而总。"),
("淛","zhè",F2,"从水制聲：江名（《集韻》），浙江，取潮曲折倒流。","zh取凿总：水曲而总。"),
("掣","chè",F2,"从手制聲：掣曳也（《爾雅》），牽引、抽掣。","ch「刺持」取「持」：牽引而持。")]
for ch,p,F0,xp,sm in D:
    num=576 if "第576部" in F0 else 577
    nm="來" if num==576 else "制"
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"麥支取「穗、皮、屑、煮」一面：麳、麩、麵、麷、萊、賚、棶、騋；制支取「裁斷、牽引」一面：制、製、淛、掣；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":num,"name":nm}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lmai-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":f"源自《系統漢語》第{576 if '第576部' in F0 else 577}部「{'來' if '第576部' in F0 else '制'}部」（卷九十四 七）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
p=r"intake\20261024-字卡576c.json"
for it in range(10):
    json.dump({"schema_version":1,"intent":f"字卡576c{it}-2026-10-24","risk":"low","claims":cl},open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    out=run("knowledge-plan","capture","--file",p,"--format","json")
    if "PLAN_DUPLICATE" not in out:
        print("ok claims",len(cl)); break
    idx=int(re.search(r"claims\[(\d+)\]",out).group(1)); print("drop",cl[idx]["title"]); cl.pop(idx)
bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))