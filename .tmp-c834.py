import json,subprocess,os,glob,re
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
F="【第580部「麗部」】麗（丽）＝象角沒有分杈的鹿形（約指麂子，皮柔可為衣帽），本義隱沒後另造「麂／𪊨」；轉義 配偶、附著（鹿喜獨居或雌雄同居）、美麗；音源為借音。"
N="字形：古文字字形库未收。"
D=[("麗","lì",F,"象無杈角之鹿形（麂子），引申配偶、附著、美麗、華麗。","l「拢离」取「离」：鹿行而离。"),
("儷","lì",F,"从人麗聲：偶也（《玉篇》），配偶、並列（儷辭）。","l取拢离：配對而离。"),
("酈","lì",F,"从邑麗聲：地名（《說文》「酈，南陽縣」），酈食其；姓。","l取拢离：邑分而离。"),
("驪","lí",F,"从馬麗聲：馬深黑色（《說文》「驪，馬深黑色」），驪龍。","l取拢离：馬黑而离。"),
("䕻","lì",F,"从艸麗聲：艸木相附麗而生（《說文》「䕻，艸木相附䕻而生」）。","l取拢离：草附而离。"),
("穲","lí",F,"从禾麗聲：禾名（《集韻》），苗之美者。","l取拢离：禾列而离。"),
("攦","lì",F,"从手麗聲：折也（《集韻》），擊、折斷。","l取拢离：手折而离。"),
("籭","shāi",F,"从竹麗聲：竹器（《說文》「籭，竹器也」），篩之或體，篩米去糠。","sh「失收」取「收」：篩分而收。"),
("纚","lí",F,"从糸麗聲：連續也（《說文》「纚，連續也」），繩索、纚纚。","l取拢离：絲連而离。"),
("釃","shī",F,"从酉麗聲：下酒也（《說文》「釃，下酒也」），濾酒。","sh取失收：酒濾而收。"),
("欐","lì",F,"从木麗聲：屋梁（《說文》「欐，屋梁也」），棟樑。","l取拢离：木架而离。"),
("曬","shài",F,"从日麗聲：暴也（《集韻》），日光曬物（俗作晒）。","sh取失收：日曝而收。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"麗部同取「附麗成偶」一面：麗鹿、儷偶、酈邑、驪黑馬、䕻附生、穲禾、攦折、籭篩、纚連、釃濾酒、欐梁、曬日；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":580,"name":"麗"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lli-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第580部「麗部」（卷九十五 離）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
p=r"intake\20261024-字卡580a.json"
for it in range(10):
    json.dump({"schema_version":1,"intent":f"字卡580a{it}-2026-10-24","risk":"low","claims":cl},open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    out=run("knowledge-plan","capture","--file",p,"--format","json")
    if "PLAN_DUPLICATE" not in out:
        print("ok claims",len(cl)); break
    idx=int(re.search(r"claims\[(\d+)\]",out).group(1)); print("drop",cl[idx]["title"]); cl.pop(idx)
bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))