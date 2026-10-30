import json,subprocess,os,glob
B=("部頭幾（几㡬jī）：从戍、𢆶聲——「𢆶」指微小，「戍」指持戈守衛，象意細微卻十分重要的事物，表示要害、關鍵（《法言》「為政有幾」，李軌注「幾，要也」）。"
   "轉義：①細微的跡象、苗頭預兆 ②臨界點→危險、危機、終盡（《說文》「微也，殆也」）③器物上的凹凸線紋。"
   "辯證：商金文本从「威」从「𢆶」，象意細微卻具威力，西周演變作「戍」。字族衍義：①細微卻重要 ②細微而連續。")
N="字形：古文字字形庫未收；原稿該條前後無獨立插圖。"
def card(ch,py_,xp,hx,sm):
    return {"char":ch,"pinyin":py_,"bus":[],"sections":[
      {"key":"bengen","label":"字根本義","text":B,"cites":[]},
      {"key":"zigen","label":"字形","text":N,"cites":[]},
      {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
      {"key":"hengxiang","label":"横向对照","text":hx,"cites":[]},
      {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]}
D=[
("僟","jī","从人幾聲，《說文》精謹也（巨衣切），精詳謹嚴；《集韻》深練於事曰僟。","①細微卻重要組：與幾、機同取「微而要」——人事之精微者。","j「聚決」取「聚」：精聚而後謹。"),
("𧗓","jī","从血幾聲，《說文》以血有所刏塗祭也（渠稀切），割傷出血塗於新器之血祭。","①組：血祭之要，與幾同取「要」。","x「續消」取「續」：血續而塗。"),
("嘰","jī","从口幾聲，《說文》小食也（居衣切），小口小口地吃；《集韻》唏也、哀歎。","②細微而連續組：與穖（穗粒相續）、䟇（碎步）同取「微而連」——小食即一口接一口。","j「聚決」取「聚」：粒粒聚食。"),
("𥼘","qí","从米，《集韻》小食也，或从口。","②組：與嘰同取「小食」，以米定落點。","q「親缺」取「缺」：食少而缺。"),
("䟇","jī／xī","从走幾聲，《說文》走也（居衣切），當指碎步走。","②組：與嘰同取「微而連」，以走定落點——一步步碎走。","j「聚決」取「聚」：步聚而行。"),
("𩴪","qí","从鬼幾聲，《說文》鬼俗也（居衣切）；《淮南傳》「吳人鬼，越人𩴪」，奉信鬼之風俗。","①組：俗之幽微者，與幾（幾微）通。","q「親缺」取「缺」：幽缺而事鬼。"),
("𧰙","qí","从豈幾聲，《說文》㡮也、訖事之樂也（渠稀切）；古代燕饗將畢所奏之樂。","①組：樂之終於將畢——正合「幾」之「終盡、臨界」。","q「親缺」取「缺」：樂將缺而止。"),
]
for ch,p,a,b,c in D:
    json.dump(card(ch,p,a,b,c),open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("写卡",len(D))
# claims
Bd="源自《系統漢語》第387部「幾部」；字卡五步规程。"; K="topic-zika-shizi"
stm={"僟":"僟 jī：从人幾聲，《說文》精謹也（巨衣切），精詳謹嚴；《集韻》深練於事曰僟。",
"𧗓":"𧗓 jī：从血幾聲，《說文》以血有所刏塗祭也（渠稀切），割傷出血塗於新器之血祭。",
"嘰":"嘰 jī：从口幾聲，《說文》小食也（居衣切），小口小口地吃；《集韻》唏也、哀歎。",
"𥼘":"𥼘 qí：从米，《集韻》小食也，或从口。",
"䟇":"䟇 jī／xī：从走幾聲，《說文》走也，當指碎步走。",
"𩴪":"𩴪 qí：从鬼幾聲，《說文》鬼俗也；《淮南傳》「吳人鬼，越人𩴪」，奉信鬼之風俗。",
"𧰙":"𧰙 qí：从豈幾聲，《說文》㡮也、訖事之樂也；古代燕饗將畢所奏之樂。",}
cl=[{"id":f"bs-{i:03d}","node":"hanzi-yinyuan","topic_id":K,"title":f"{ch}（字卡）","statement":st,
     "boundary":Bd,"permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"}
    for i,(ch,st) in enumerate(stm.items(),1)]
json.dump({"schema_version":1,"intent":"字卡387幾部餘7字2026-10-23","risk":"low","claims":cl},
          open(r"intake\20261023-字卡387餘.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡387餘.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    files=sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)
    b=os.path.basename(files[-1])[:-5]
    st=json.loads(run("bundle-status",b,"--format","json")); h=st["bundles"][0]["content_hash"]
    run("bundle-approve",b,"--apply","--content-hash",h); run("bundle-apply",b,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",b,"err",v.get("errors"))