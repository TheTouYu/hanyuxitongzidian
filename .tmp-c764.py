import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
FH="【第561部「乂部」】乂＝象交叉的傷痕形，或加刀為「刈」（《說文》「芟艸也」）；傷痕多為鞭笞所傷，引申治理、懲戒、才德過人；音源為痛聲。"
N="字形：古文字字形库未收。"
D=[("乂","yì",FH,"象交叉傷痕：芟艸也（《說文》「芟艸也」），割取；引申治理、懲戒、賢才。","y「续消」取「续」：割而续。"),
("刈","yì",FH,"从刀乂聲：芟艸也（《說文》），取也、殺也，收割。","y取续消：刀割而续。"),
("艾","ài",FH,"从艸乂聲：冰臺也（《說文》「冰臺也」），艾草；引申止、養、美。","ai「豁活」取「活」：草活而艾。"),
("䢃","yì",FH,"从辟乂聲：治也（《說文》「治也」），治理、安定。","y取续消：治而续。"),
("㣻","yì",FH,"从心乂聲：懲也（《說文》「懲也」），困患為戒。","y取续消：懲而续。"),
("䖊","yì",FH,"从虎乂聲：虎皃（《說文》「虎皃」），虎呲牙之狀。","y取续消：虎威而续。"),
("㲼","chà",FH,"从水乂聲：同汊，水歧流（《集韻》）。","ch「刺持」取「持」：水歧而持。"),
("𠮣","wú",FH,"从口乂聲：同「吾」，自我之稱（《集韻》）。","w「蒙末」取「蒙」：口蒙而吾。"),
("𤴧","yì",FH,"从疒乂聲：病也（《集韻》），瘡痍。","y取续消：病而续。"),
("鴱","ài",FH,"从鳥艾聲：鳥名（《說文》「鴱，鳥也」），巧婦鳥。","ai取豁活：鳥鳴而活。"),
("餀","hài",FH,"从食艾聲：食臭也（《說文》「食臭也」）。","h取豁活：食而活。"),
("哎","āi",FH,"从口艾聲：歎詞（《集韻》），哎喲。","ai取豁活：口張而活。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"乂系同取「交叉割取、懲治」一面：乂芟草、刈收、艾草、䢃治、㣻懲、䖊虎、㲼水歧、𠮣吾、𤴧病、鴱鳥、餀食臭、哎歎；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":561,"name":"乂"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lyi2-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第561部「乂部」（卷九十二 辛）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡561a2026-10-24","risk":"low","claims":cl},open(r"intake\20261024-字卡561a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261024-字卡561a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))