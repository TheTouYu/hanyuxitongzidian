import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
FZ="【第534部「爿部」·臧系】臧＝从臣从戕（戈），以戈守臣（家奴），《說文》「善也」；引申藏匿（臧／藏通用）。"
FC="【第534部「爿部」·倉系】倉＝象穀倉形（上為蓋、下為口），《說文》「穀藏也」；引申藏、寒、聲。"
N="字形：古文字字形库未收。"
D=[("臧","zāng",FZ,"从臣从戈：善也（《說文》），以戈守臣→善；通藏。","z「凿总」取「凿」：守而实。"),
("藏","cáng",FZ,"从艸臧聲：《說文》「匿也」，戰國古文从宀醬聲（密放醬菜之所）。","c「刺持」取「持」：藏而持。"),
("臟","zàng",FZ,"从肉臧聲：五臟也（《正字通》），胸內器官總稱，藏精藏神。","z取凿总：藏而实。"),
("贓","zāng",FZ,"从貝臧聲：納賄曰贓（《廣韻》），非理所得財物。","z取凿总：藏赃而实。"),
("㵴","cáng",FZ,"从水臧聲：沒也（《集韻》），沉沒。","c取刺持：潛藏而持。"),
("倉","cāng",FC,"象穀倉形：穀藏也（《說文》）；引申藏、寒、聲。","c取刺持：藏穀而持。"),
("艙","cāng",FC,"从舟倉聲：船中載人貨的空間。","c取刺持：船倉而持。"),
("滄","cāng",FC,"从水倉聲：寒也（《說文》），又滄海。","c取刺持：水寒而持。"),
("凔","cāng",FC,"从仌倉聲：寒也（《說文》）。","c取刺持：冰寒而持。"),
("鎗","chēng",FC,"从金倉聲：鐘聲也（《說文》），又鼎類、酒器、兵器。","ch「刺持」取「持」：鐘振而持。"),
("愴","chuàng",FC,"从心倉聲：傷也（《說文》），悲傷。","ch取刺持：心傷而持。"),
("戧","qiāng",FC,"从戈倉聲：傷也（《說文》），又撑也、逆也。","q「亲缺」取「亲」：刃親而缺。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"臧系言藏守（臧／藏／臟／贓／㵴），倉系言仓藏及由仓所生（倉／艙／滄／凔／鎗／愴／戧）；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":534,"name":"爿"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lzang-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"字卡（第534部臧倉系）：{xp}",
 "boundary":"源自《系統漢語》第534部「爿部」（卷八十九 象）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡534zang2026-10-24","risk":"low","claims":cl},open(r"intake\20261024-字卡534zang.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261024-字卡534zang.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))