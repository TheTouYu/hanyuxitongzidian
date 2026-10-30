import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
FY="【第525部「昜部」】昜＝从日从丂，象對日呼號、日出；轉義飛舉、乾旱搖盪；音源本丂聲。字族三面：日烈／日出／日升飛揚。"
N="字形：古文字字形库未收。"
D=[("敭","yáng",FY,"从手昜聲：飛舉也（《說文》），即「揚」之古文。","y「圆容」取「圆」：手揚而周。"),
("瑒","chàng",FY,"从玉昜聲：圭尺二寸有瓚，祠宗廟灌地之器（《說文》）。","ch「刺持」取「持」：奉圭而持。"),
("蕩","dàng",FY,"从水𦳝聲：河名湯河；又蕩滌、搖動（《釋名》）。","d「囤动」取「动」：水搖而動。"),
("踼","tàng",FY,"从足昜聲：跌踼，跌倒、抵拒（《說文》）；行不正。","t「涂突」取「突」：足跌而突。"),
("愓","dàng",FY,"从心昜聲：放也、平也（《說文》）；放逸不憂。","d取囤动：心放而動。"),
("盪","dàng",FY,"从皿湯聲：滌器之皿（《說文》），引申搖動、行。","d取囤动：滌盪而動。"),
("𥯕","dàng",FY,"从竹昜聲：大竹筩，笙簫之屬，可盛酒（《說文》）。","d取囤动：竹空而動。"),
("簜","dàng",FY,"从竹湯聲：大竹，可為幹（《說文》引《夏書》）。","d取囤动：竹大而動。"),
("碭","dàng",FY,"从石昜聲：文石、有花紋之石（《說文》）；又蕩溢振盪。","d取囤动：石文而動。"),
("腸","cháng",FY,"从肉昜聲：大小腸（《說文》）；《釋名》「暢也」，通暢胃氣。","ch取刺持：腸曲而持。"),
("𧀄","chàng",FY,"从艸畼聲：艸茂也（《說文》）。","ch取刺持：草盛而持。"),
("諹","yáng",FY,"从言昜聲：譽也、讙也（《玉篇》）；又謹也。","y取圆容：言揚而周。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同部諧聲字分三面：日烈（瑒／腸）、日出灼熱（敭／諹）、日升搖盪（蕩／踼／愓／盪／𥯕／簜／碭／𧀄）；只列本部字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":525,"name":"昜"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lyang5-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}（{p}）＝{xp}",
 "boundary":"源自《系統漢語》第525部「昜部」（卷八十八 昜）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡525c2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡525c.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡525c.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))