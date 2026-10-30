import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
FH="【第550部「火部」】火＝象火焰上騰；部内字族 耿／煩／赤／焦／麃／熯／難，皆以火為義源而各有取面。"
N="字形：古文字字形库未收。"
D=[("熯","hàn",FH,"从火堇聲：乾皃（《說文》「乾皃」），以火烘乾。","h「豁活」取「豁」：火烘而豁。"),
("傼","hàn",FH,"从人堇聲：人也（《說文》「人也」），姓。","h取豁活：人而豁。"),
("艱","jiān",FH,"从堇艮聲：土難治也（《說文》「土難治也」），艱難。","j「聚决」取「聚」：難聚而决。"),
("暵","hàn",FH,"从日堇聲：乾也（《說文》「乾也」），晒乾。","h取豁活：日晒而豁。"),
("漢","hàn",FH,"从水堇聲：漾也（《說文》「漾也」），水名、漢族。","h取豁活：水流而豁。"),
("歎","tàn",FH,"从欠堇聲：吟也（《說文》「吟也」），嘆息。","t「涂突」取「突」：氣突而吟。"),
("難","nán",FH,"从鳥堇聲：鳥也（《說文》「鳥也」），借為艱難。","n「纳弄」取「纳」：鳥纳而弄。"),
("攤","tān",FH,"从手難聲：開也（《集韻》），攤開、攤派。","t取涂突：手開而突。"),
("癱","tān",FH,"从疒難聲：風病（《集韻》），癱瘓。","t取涂突：病而突。"),
("灘","tān",FH,"从水難聲：水灘（《集韻》），水淺多石。","t取涂突：水突而淺。"),
("儺","nuó",FH,"从人難聲：行人節也（《說文》「行人節也」），驅疫之儺。","n取纳弄：行節而弄。"),
("戁","nǎn",FH,"从心難聲：敬也（《說文》「敬也」），恐懼。","n取纳弄：心敬而弄。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"熯／難系同取「火乾、艱阻」一面：熯烘、傼人、艱難、暵晒、漢水、歎吟、難鳥、攤開、癱病、灘水、儺節、戁敬；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":550,"name":"火"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lhuo5-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第550部「火部」（卷九十一 火）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡550e2026-10-24","risk":"low","claims":cl},open(r"intake\20261024-字卡550e.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261024-字卡550e.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))