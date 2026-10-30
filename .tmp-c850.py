import json,subprocess,os,glob,re
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
F="【第583部「巢部」】巢＝从木上有西（西＝鸟窝），樹上有鳥窩形；字族五面：鳥巢之狀／高、抄掠／小／吵鬧／形近之訛。"
N="字形：古文字字形库未收。"
D=[("𣝞","jiāo",F,"从木巢聲：蒜束（《玉篇》），蒜苔（頂端花苞鼓如巢）。","j「聚决」取「聚」：束聚而决。"),
("𡏮","cháo",F,"从土巢聲：𡏮陽，地名（《康典》），傍有巢父墓。","ch「刺持」取「持」：地聚而持。"),
("𥕘","cháo",F,"从石巢聲：壘石為巢而居（《集韻》），附國之民。","ch取刺持：石壘而持。"),
("𩍀","suǒ",F,"从革巢聲：革鎖也（《集韻》）。","s「失收」取「收」：革固而收。"),
("𡻝","cháo",F,"从山巢聲：嶚𡻝，山高皃（《集韻》）。","ch取刺持：山高而持。"),
("䟁","xiāo",F,"从走巢聲：起也（《玉篇》）；又競走（《集韻》）。","x「续消」取「消」：走疾而消。"),
("𩫥","cáo",F,"从高巢聲：高足（《玉篇》）、高皃（《集韻》）。","c「刺持」取「持」：高立而持。"),
("㑿","zhào",F,"从人巢聲：長皃（《廣韻》）；又小也（《康典》）。","zh「凿总」取「总」：長而总。"),
("𨢪","chào",F,"从酉巢聲：醉𨢪也（《玉篇》），醉態。","ch取刺持：醉而持。"),
("𨄓","cháo",F,"从足巢聲：行捷也（《集韻》）。","ch取刺持：行捷而持。"),
("𦸛","cháo",F,"从艸巢聲：𦸛麥，艸名（《集韻》）；一說巢菜即野豌豆。","ch取刺持：草蔓而持。"),
("𤍒","zhāo",F,"从火巢聲：然也（《集韻》），燃燒。","zh取凿总：火燃而总。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"巢部同取「鳥巢之狀、高、抄掠」一面：𣝞蒜束、𡏮地名、𥕘石巢、𩍀革鎖、𡻝山高、䟁競走、𩫥高足、㑿長貌、𨢪醉、𨄓行捷、𦸛巢菜、𤍒燃；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":583,"name":"巢"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lchao2-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第583部「巢部」（卷九十六 雀）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
p=r"intake\20261024-字卡583b.json"
for it in range(10):
    json.dump({"schema_version":1,"intent":f"字卡583b{it}-2026-10-24","risk":"low","claims":cl},open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    out=run("knowledge-plan","capture","--file",p,"--format","json")
    if "PLAN_DUPLICATE" not in out:
        print("ok claims",len(cl)); break
    idx=int(re.search(r"claims\[(\d+)\]",out).group(1)); print("drop",cl[idx]["title"]); cl.pop(idx)
bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))