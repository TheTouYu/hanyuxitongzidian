import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
FT="【第527部「向部」·堂系（二级字根）】堂＝从土尚聲，用土築成的高臺、空闊殿堂；字族三面：堂之空（顯明空闊）／堂之高（撐起抵距）／堂之聲（鼓鐘之聲）。"
FD="【第527部「向部」·當系（二级字根）】當（当）＝从田尚聲：「田」為田界，「尚」為敞開、相對，本義田與田相值（《說文》「田相值也」）；轉義對等相值→承受擔任→正當、應當；又借為「嘗」之省，表曾經。字族三面：相值對當／承受擔任／器物之中。"
N="字形：古文字字形库未收。"
D=[("𨎋","táng",FT,"从車堂聲：大車（《玉篇》）；又音 chēng，小車轅。","t「涂突」取「涂」：車行而突。"),
("𨟐","táng",FT,"从邑㙶聲：地名（《說文》），在今江蘇南京北。","t取涂突：邑名而突。"),
("闛","táng",FT,"从門堂聲：闛闛，盛皃（《說文》）；又鼓聲、天門（閶闔）。","t取涂突：門盛而突。"),
("𡠠","táng",FT,"从女堂聲：㜍，女字（《集韻》），人名用字。","t取涂突：借聲為名。"),
("㑽","táng",FT,"从人堂聲：傏，大也、盛也（《集韻》）。","t取涂突：人盛而突。"),
("𤛋","táng",FT,"从牛堂聲：牛名（《集韻》），野牛，角可為器。","t取涂突：牛壯而突。"),
("當","dāng",FD,"从田尚聲：田與田相值（《說文》）；引申承受、擔任、正當、應當；又表曾經。","d「囤动」取「囤」：田值而囤。"),
("檔","dàng",FD,"从木當聲：橫木、木牀（《集韻》）；引申檔案、檔次。","d取囤动：木橫而囤。"),
("璫","dāng",FD,"从玉當聲：瓦當、耳飾（《說文》「華飾也」）。","d取囤动：玉當而囤。"),
("襠","dāng",FD,"从衣當聲：袴襠（《玉篇》），褲之中縫。","d取囤动：衣當而囤。"),
("鐺","dāng",FD,"从金當聲：鋃鐺、鐵鍋（《說文》「鋃鐺也」）。","d取囤动：金當而囤。"),
("擋","dǎng",FD,"从手當聲：遮也、攔也（《正字通》）。","d取囤动：手當而囤。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"堂系餘字補齊（𨎋／𨟐／闛／𡠠／㑽／𤛋）；當系諧聲字分三面：相值對當（當／擋）／承受擔任（襠）／器物之中（檔／璫／鐺）；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":527,"name":"向"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"ldang-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}（{p}）＝{xp}",
 "boundary":"源自《系統漢語》第527部「向部」（卷八十八 昜，堂系／當系）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡527f2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡527f.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡527f.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))