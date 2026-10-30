import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
FU="【第528部「上部」】上（丄）＝甲骨文从「一」上加指示符號，指物體的上面（《說文》「高也……指事也」）；轉義往上、登升；位處諸物之上（君也）；以為上（尊崇）。音源借音：物之上敞開，義音同「尚」。字族衍義：①指高處、往上 ②象意含往上義。"
N="字形：古文字字形库未收。"
D=[("上","shàng",FU,"从「一」上加指示符號，指物體的上面（《說文》「高也」）；引申往上、登升、君上、尊崇。","sh「失收」取「收」：物上而收。"),
("𨑗","shàng",FU,"疑「上」之繁文（《戰國古文》），鄂君舟節讀上。","sh取失收：行之而上。"),
("圵","dàng",FU,"《海篇》音蕩，高田；與南北字不同。","d「囤动」取「囤」：田高而囤。"),
("仩","cháng",FU,"《字彙補》與「長」同，帶頭的人、孟也進也。","ch「刺持」取「持」：人長而持。"),
("忐","tǎn",FU,"《五音集韻》忐忑，心虛、怯懼——提心吊膽。","t「涂突」取「涂」：心懸而突。"),
("忑","tè",FU,"忐忑連文，心上下不定、怯懼。","t取涂突：心下而突。"),
("𠮵","màng",FU,"《篇海》「問而不答」。","m「蒙末」取「蒙」：問而不答。"),
("𠮳","yīng",FU,"應喚語也，同「應」，呼應聲（《字彙補》）。","y「柔锐」取「柔」：應聲而柔。"),
("𠧕","hé",FU,"《字彙補》音和。","h「豁活」取「活」：和而活。"),
("𠧛","bó",FU,"同「百」，古字；地名（《字彙補》）。","b「闭剥」取「闭」：數聚而閉。"),
("𣥌","huàn",FU,"同「幻」（《字彙補》）。","h取豁活：幻而活。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"上部字分兩面：指高處往上（上／𨑗／圵／仩）與象意含往上（忐／忑）；餘為同音借用或訛體，各標所出。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":528,"name":"上"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lshangt-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}（{p}）＝{xp}",
 "boundary":"源自《系統漢語》第528部「上部」（卷八十八 昜）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡528a2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡528a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡528a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))