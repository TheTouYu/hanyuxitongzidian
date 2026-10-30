import json,subprocess,os,glob
BS="【413 寺部（原属它部，从又从之）】寺＝从又从之（「又」或作「寸」，指手；「之」指往），象意手所及处，表示握持（此义分化如「持」，《说文》「握也」）。手所及处意味着脚没动、活动范围只在手能触到的地方，故也可表示待着不动（分化如「待」，《说文》「竢也」）。转义：由站着不动引申指近侍（「侍」）、宦官（寺人）、官衙寺庙（《广韵》「司也、嗣也、官也」，sì）。由握持引申指积蓄、储备（「庤」）。字族衍义：①指待着不动，表示直立、挺立、不进 ②指握持，表示储备、积蓄、依仗。"
N="字形：古文字字形库未收。"
D=[
("侍","shì","《说文》「承也」；《六书故》「陪侧也」；《广雅》「使也」——承奉、陪侍。","不动族①之人：以「人」定其人，站而承奉。","sh「失收」取「收」：收身而侍。"),
("歭","chí","《说文》「䠧也」——踯躅不前；《集韵》「与峙通，供具也」。","不动族①之止：以「止」定其行，止而不前。","ch「刺持」取「持」：持足而止。"),
("㭙","zhé","《说文》「槌也」；《玉篇》「槌横木也」——搭架用的木桩。","不动族①之木：以「木」定其物，直立如桩。","zh「凿总」取「凿」：木凿而立。"),
("特","tè","《说文》「朴特，牛父也」；《韵会》「挺立曰特」；《增韵》「一牲曰特」——公牛、独、挺立。","不动族①之牛：以「牛」定其类，公牛独立挺然。","t「涂突」取「突」：突出而立。"),
("痔","zhì","《说文》「后病也」——痔疮，寄生肛门四周，宜站、坐则疼，故从寺。","不动族①之疒：以「疒」定其类，宜立而不宜坐。","zh「凿总」取「凿」：病凿于下。"),
("畤","zhì","《说文》「天地五帝所基址，祭地」——祭祀场所；《字汇补》「凡土高处曰畤」。","不动族①之田：以「田」定其地，高土而立祭。","zh「凿总」取「总」：诸神总祭。"),
("秲","shì","《广韵》「与莳同」——插秧；zhì「秲𥣬，稻名」。","不动族①之禾：以「禾」定其物，插秧须立。","sh「失收」取「收」：秧收于田。"),
("鼭","shí","《玉篇》「鼠名」——疑即土拨鼠，能直立，故从寺。","不动族①之鼠：以「鼠」定其物，直立如人。","sh「失收」取「收」：鼠收而立。"),
("跱","zhì","《类篇》「跱䠧，行不进」；《博雅》「止也」——立止。","不动族①之足：以「足」定其行，足止而立。","zh「凿总」取「凿」：足凿而立。"),
("峙","zhì","《广韵》「峻峙，屹立也」——直立、耸立；《龙龛》「住也」。","不动族①之山：以「山」定其形，山立而峙。","zh「凿总」取「总」：山总而峙。"),
("待","dài","《说文》「竢也」——等候；《广雅》「逗也」。","不动族①之彳：以「彳」定其行，行而止待。","d「囤动」取「囤」：囤步而待。"),
("等","děng","《说文》「齐简也，寺，官曹之等平也」——齐、类、比、辈。","握持族②之竹：以「竹」定其物，简齐如手持平。","d「囤动」取「囤」：囤齐而等。"),
]
def card(ch,p,Bx,Nx,a,b,c):
    return {"char":ch,"pinyin":p,"bus":[],"sections":[
      {"key":"bengen","label":"字根本义","text":Bx,"cites":[]},
      {"key":"zigen","label":"字形","text":Nx,"cites":[]},
      {"key":"xingpang","label":"形旁声旁","text":a,"cites":[]},
      {"key":"hengxiang","label":"横向对照","text":b,"cites":[]},
      {"key":"shengmu","label":"声母义","text":c,"cites":[]}]}
b="同取寺部「手所及处／立而不动」一面，形符各定其落点；故声符给义、形符定落点。"
for ch,p,Bx,a,c in D:
    json.dump(card(ch,p,BS,N,a,b,c),open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("写卡",len(D))
def B(ch): return "源自《系統漢語》第413部「寺部」（卷六十七 足）；字卡五步规程。"
cl=[{"id":f"bdc-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{t[0]}（字卡）",
   "statement":f"{t[0]}（{t[1]}）：{t[2]}","boundary":B(t[0]),"permission":"public",
   "fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,t in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡413寺部2026-10-23","risk":"low","claims":cl},
          open(r"intake\20261023-字卡413寺部.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡413寺部.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))