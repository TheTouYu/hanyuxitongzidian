import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
F="【509 鼎部】鼎＝象鼎形，三足兩耳、下空生火，兼具鍋與灶；《說文》「三足兩耳，和五味之寶器也」，禹收九牧之金鑄鼎，故為重器、權威、鼎立。"
G="【510 典部】典＝从冊从𠬞：冊指書簡，𠬞指兩手捧簡冊，象意①尊奉典籍、②常法制度；本義典籍、法則（《說文》「五帝之書也」）。"
N="字形：古文字字形库未收。"
D=[("鼎","dǐng",F,"本部部首字：三足兩耳之煮器→寶器、權威、鼎立。","d「囤动」取「囤」：鼎囤食物。"),
("貞","zhēn",F,"从卜貝（一說从鼎省）：卜問吉凶曰貞（《說文》「卜問也」），假借為正、堅。","zh「凿总」取「凿」：龜甲鑿而問。"),
("偵","zhēn",F,"从人貞聲：暗中察看（「偵察」），取貞之察問。","zh取凿：伺察如鑿。"),
("楨","zhēn",F,"从木貞聲：築牆時立的木柱（《說文》「剛木也」），引申楨幹。","zh取凿：木立如凿。"),
("禎","zhēn",F,"从示貞聲：吉祥（《說文》「祥也」）。","zh取凿：兆鑿而祥。"),
("幀","zhēn",F,"从巾貞聲：畫幅（「裝幀」），取貞之正、定。","zh取凿：幅正而張。"),
("湞","zhēn",F,"从水貞聲：水名（湞水）。","zh取凿：水激而鑿。"),
("典","diǎn",G,"本部部首字：兩手捧簡冊→典籍、常法、典禮。","d「囤动」取「囤」：冊囤而尊。"),
("腆","tiǎn",G,"从肉典聲：豐厚（《說文》「設膳腆腆也」），引申靦腆。","t「涂突」取「涂」：肉厚而涂。")]
cl=[]
for i,(ch,p,F0,xp,sm) in enumerate(D,1):
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"鼎部取「重器、權威」一面，典部取「簡冊、常法」一面；形符各定落點。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
    cl.append({"id":f"lcx-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
      "boundary":"源自《系統漢語》第509－510部（卷八十三 鼎）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"})
json.dump({"schema_version":1,"intent":"字卡510a2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡510a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡510a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out, "cards:", len(cl))
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))