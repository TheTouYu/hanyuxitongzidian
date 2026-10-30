import json,subprocess,os,glob,docx
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
N="字形：古文字字形库未收。"
D=[("焻","chàng","【第526部「昌部」·形近訛字】昌部末組，皆形近而訛者。","从火昌聲：氣也、火氣（《字彙補》）；《舊藏》作「煱」音瓜，俗訛。","ch「刺持」取「持」：火氣而持。","源自《系統漢語》第526部「昌部」（卷八十八 昜）；字卡五步规程。"),
("𢛝","jiān","【第526部「昌部」·形近訛字】《篇海》因𢙶字而譌，六書無此字。","「惷」字之譌（《正字通》），舊音姦，非。","j「聚决」取「聚」：心亂而聚。","源自《系統漢語》第526部「昌部」（卷八十八 昜）；字卡五步规程。"),
("𣮑","jié","【第526部「昌部」·形近訛字】《龍龕》同睫、𣭶、𣮍。","睫毛；大約「𣯥」字之訛。","j取聚决：毛聚而列。","源自《系統漢語》第526部「昌部」（卷八十八 昜）；字卡五步规程。"),
("𥛼","cáo","【第526部「昌部」·形近訛字】《字彙補》同「䄚」。","祭也、佑也，一曰祭豕先（《集韻》）；「䄚」字之訛。","c「刺持」取「持」：祭而持。","源自《系統漢語》第526部「昌部」（卷八十八 昜）；字卡五步规程。"),
("向","xiàng","【第527部「向部」】向＝从宀从口：「宀」屋子，「口」窗戶，本義為窗（《玉篇》「窻也」）。轉義：窗朝一方→朝向、方向；引申嚮往。字族分面：敞開（敞）／土臺（堂）／田值（當）／暗黑（黨）／手掌（掌）等。","从宀从口：屋之窗，引申朝向、方向。","x「续消」取「续」：向而續。","源自《系統漢語》第527部「向部」（卷八十八 昜）；字卡五步规程。")]
for ch,p,F0,xp,sm,bd in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"昌部訛字組各標訛源（焻＝煱／𢛝＝惷／𣮑＝睫／𥛼＝䄚）；向部諧聲字分敞開、土臺、田值、暗黑、手掌諸面，形符各定落點。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    bn=526 if ch not in "向" else 527
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":bn,"name":"昌" if bn==526 else "向"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lchang2-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}（{p}）＝{xp}",
 "boundary":bd,"permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm,bd) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡526b2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡526b.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡526b.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))
f=r"D:\字谱智能体\卷八十八  昜.docx"
ps=[p.text.strip() for p in docx.Document(f).paragraphs if p.text.strip()]
for i,t in enumerate(ps[121:200],121): print(i,t[:58])