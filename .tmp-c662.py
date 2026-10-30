import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
FZ="【第527部「向部」·訛字組】向族末組，皆形近舟、冏、咼或同音通用者，須標訛源。"
FS="【第527部「向部」·尚系（二级字根）】尚＝从八向聲：「八」分開、分別，「向」打開窗戶，為「敞」之初文（《集韻》「開也、露也」）。轉義：開窗使明→推崇、薦舉、尊奉、佐助、增加；所明有限→庶幾、差不多；開窗出於人為控制→主宰、掌控。字族三面：敞開敞亮／推舉罩覆／來回反復。"
N="字形：古文字字形库未收。"
D=[("𥥩","xiàng",FZ,"《韻海》與向同；俗音阿（《正字通》）。","x「续消」取「续」：向之俗體。",527,"向"),
("𥀾","xiàng",FZ,"《篇海類編》音嚮，應指鼓聲。","x取续消：聲應而續。",527,"向"),
("𤍀","xiǎng",FZ,"《龍龕》俗音嚮。","x取续消：火應而續。",527,"向"),
("銄","xiǎng",FZ,"《正字通》「餉字之譌」，饋贈；或同扃。","x取续消：饋而續。",527,"向"),
("晑","xiǎng",FZ,"《篇海》明也；又𣅻音扃。","x取续消：日明而續。",527,"向"),
("逈","jiǒng",FZ,"同「迥」，遠也（《廣韻》）。","j「聚决」取「聚」：遠而聚望。",527,"向"),
("𥿧","xiǎng",FZ,"《字彙》綿也；《正字通》疑「絅」之訛。","x取续消：絲綿而續。",527,"向"),
("䚁","chēn",FZ,"「舟譌从向」，「𧡬」之訛，私出頭視（《廣韻》）。","ch「刺持」取「持」：探視而持。",527,"向"),
("𧥁","xī",FZ,"「觹」之俗，角錐，童子佩以解結（《龍龕》）。","x取续消：錐解而續。",527,"向"),
("𧙹","hè",FZ,"《龍龕》「《舊藏》作禍」，「禍」之訛。","h「豁活」取「活」：禍及而活。",527,"向"),
("尚","shàng",FS,"从八向聲：開窗，敞之初文；引申推崇、佐助、庶幾、主宰。","sh「失收」取「收」：窗開而收。",527,"向")]
for ch,p,F0,xp,sm,bn,bnm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"向部末組各標訛源（𥥩＝向／銄＝餉／𥿧＝絅／䚁＝𧡬／𧙹＝禍）；尚系諧聲字分敞開、推舉罩覆、來回反復三面，形符各定落點。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":bn,"name":bnm}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lxiang2-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}（{p}）＝{xp}",
 "boundary":"源自《系統漢語》第527部「向部」（卷八十八 昜）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm,bn,bnm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡527b2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡527b.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡527b.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))