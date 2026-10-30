import json,subprocess,os,glob
B=("部頭丌（jī）：象低矮平整的托盤形——可獨立為器以端送小物，也可只是器皿的底座，故多作表示平整的音義符號組合新字；《說文》「下基也，薦物之丌，象形」，讀若箕，居之切。"
   "音源：借音字，義音同「己」（堆疊物體之意）——《詩·王風》鄭箋「其，或作記，或作己，讀聲相似」，《釋文》「其，音記」。"
   "字族衍義：①指丌用，表示薦物、根基 ②同「其」，指箕或箕狀物 ③同「其」，指紋路交織，表示交彙交叉 ④形近「斤」之訛。")
N="字形：古文字字形庫未收；原稿該部有「▲鎏金麒麟印紐（唐）」「▲《祭神》（清 陳枚）」二圖，可參。"
D=[
("丌","jī","部首字本身：象低矮平整的托盤，薦物之器（《說文》下基也）。","本部主字：與亓（上加一橫）、㚦（女）同取「薦物、根基」，餘字各以形符定落點。","j「聚決」取「聚」：托而聚物。"),
("亓","qí","从丌上加一，本同丌，《集韻》「其，辭也、豈也，古作丌、亓」——上面可以薦物。","①組：丌之加筆，仍是薦物之器，兼作虛詞「其」。","q「親缺」取「親」：承物相親。"),
("㚦","jī","从女丌聲，《正字通》「古文姬」——《說文》黃帝居姬水以為姓；《廣雅》基也（根本根基）。","①組：以女定落點，姓與根基二義並存。","j「聚決」取「聚」：族聚成基。"),
("䢋","jì","从辵从丌，丌亦聲，《說文》「古之遒人，以木鐸記詩言」（居吏切），讀與記同。","①組：徐鍇謂「遒人行而求之，故从辵；丌，薦而進之于上也」——采詩而薦，正是根基之義的延伸。","j「聚決」取「聚」：采而聚之。"),
("𢗏","qí","从心丌聲，即惎：《說文》「毒也」，一曰教也、意也；《廣雅》志也，《廣韻》謀也。","①組：心蓄根基之謂，以心定落點。","q「親缺」取「親」：心親而謀。"),
("𥘕","qí","从示丌聲，即祺：《說文》「吉也」，一曰祥也；籀从基。","①組：以示定落點——根基既立則吉。","q「親缺」取「親」：神親而降祥。"),
("𥫶","jī","从竹丌聲，即箕：《說文》「簸也」，一曰星名。","②組：箕形如丌而盛物，以竹定落點。","j「聚決」取「聚」：簸而聚穀。"),
("𧿄","qí","从足亓聲，即踑：《集韻》「跡也」；jī 為㠱，《說文》「長踞也」——席地伸腳而坐，其形如箕。","②組：箕踞之形，以足定落點。","q「親缺」取「親」：足相親而坐。"),
("𦨘","qí","从舟亓聲，《博雅》「䑴艃，舟也」。","②組：舟形中凹如箕，以舟定落點。","q「親缺」取「親」：舟與水相親。"),
("䭶","qí","从馬亓聲，即騏：《說文》「馬青驪，文如博棊也」。","③組：馬紋交織如棋盤，以馬定落點——正取「交彙交叉」一面。","q「親缺」取「親」：紋相交而親。"),
]
def card(ch,p,a,b,c):
    return {"char":ch,"pinyin":p,"bus":[],"sections":[
      {"key":"bengen","label":"字根本義","text":B,"cites":[]},
      {"key":"zigen","label":"字形","text":N,"cites":[]},
      {"key":"xingpang","label":"形旁声旁","text":a,"cites":[]},
      {"key":"hengxiang","label":"横向对照","text":b,"cites":[]},
      {"key":"shengmu","label":"声母义","text":c,"cites":[]}]}
for ch,p,a,b,c in D:
    json.dump(card(ch,p,a,b,c),open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("写卡",len(D))
BK="源自《系統漢語》第391部「丌部」；字卡五步规程。"
ST={"丌":"象低矮平整的托盘，荐物之器，《说文》「下基也」。","亓":"丌上加一横，本同丌，兼作虚词「其」。","㚦":"古文姬——黄帝居姬水以为姓；《广雅》「基也」，根本根基。","䢋":"古之遒人摇木铎沿途采记诗言，荐而进之于上。","𢗏":"即惎，《说文》「毒也」，一曰教也、意也；《广韵》谋也。","𥘕":"即祺，《说文》「吉也」，一曰祥也；籀文从基。","𥫶":"即箕，《说文》「簸也」，一曰星名。","𧿄":"即踑，《集韵》「迹也」；又㠱「长踞也」，席地伸脚如箕。","𦨘":"《博雅》「䑴艃，舟也」，舟形中凹如箕。","䭶":"即騏，《说文》「马青骊，文如博棊也」，马纹交织如棋盘。"}
cl=[{"id":f"bt6-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{d[0]}（字卡）",
     "statement":f"{d[0]}（{d[1]}）：{ST[d[0]]}",
     "boundary":BK,"permission":"public","fact_classes":["evidence_scope"],
     "duplicate_resolution":"create_distinct_with_boundary"} for i,d in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡391丌部2026-10-23","risk":"low","claims":cl},
          open(r"intake\20261023-字卡391丌部.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡391丌部.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    b=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",b,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",b,"--apply","--content-hash",h); run("bundle-apply",b,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",b,"err",v.get("errors"))
else: print(out[-300:])