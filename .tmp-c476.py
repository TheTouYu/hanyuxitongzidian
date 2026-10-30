import json,subprocess,os,glob
BS="【413 寺部（原属它部，从又从之）】寺＝从又从之（「又」或作「寸」，指手；「之」指往），象意手所及处，表示握持（此义分化如「持」，《说文》「握也」）。手所及处意味着脚没动、活动范围只在手能触到的地方，故也可表示待着不动（分化如「待」）。转义：由站着不动引申指近侍、宦官、官衙寺庙；由握持引申指积蓄、储备（「庤」）。字族衍义：①指待着不动，表示直立、挺立、不进 ②指握持，表示储备、积蓄、依仗。"
N="字形：古文字字形库未收。"
D=[
("持","chí","《说文》「握也」——握持、坚持。","握持族②之手：以「手」定其动，手所及处即握。","ch「刺持」取「持」：持而不放。"),
("恃","shì","《说文》「赖也」——依赖；「心不明」亦作恃。","握持族②之心：以「心」定其恃，所持即所赖。","sh「失收」取「收」：收心而赖。"),
("邿","shī","《说文》「附庸国，在东平亢父邿亭」——古国名，在今山东济宁东南。","握持族②之邑：以「邑」定其地，小国附庸如手持。","sh「失收」取「收」：地收而附。"),
("洔","zhǐ","《说文》「水暂益，且止，未减也」——水滞留；《集韵》「水中高土」。","不动族①之水：以「水」定其物，水停如人待。","zh「凿总」取「凿」：水凿而滞。"),
("偫","zhì","《说文》「待也」——积蓄储备以待用；《玉篇》「与庤同」。","握持族②之人：以「人」定其事，储人以待。","zh「凿总」取「总」：总储而待。"),
("庤","zhì","《说文》「储置屋下也」——储藏放置在屋下。","握持族②之广：以「广」定其处，屋下所储。","zh「凿总」取「总」：总置于屋。"),
("䝰","zhì","《类篇》「畜财也」——蓄积财物。","握持族②之貝：以「貝」定其物，财所蓄。","zh「凿总」取「总」：财总而蓄。"),
("𪗺","chī","《字汇》「牛食草也」——牛反刍：先粗咽，卧时吐出细嚼，故有储存意。","握持族②之齒：以「齒」定其动，草储于胃而返嚼。","ch「刺持」取「持」：草持而返。"),
("𨨲","chí","《字汇》「梵语鍕𨨲，此云双口澡灌」——净瓶（军持）。","握持族②之金：以「金」定其器，手持而灌。","ch「刺持」取「持」：持瓶而灌。"),
]
def card(ch,p,Bx,Nx,a,b,c):
    return {"char":ch,"pinyin":p,"bus":[],"sections":[
      {"key":"bengen","label":"字根本义","text":Bx,"cites":[]},
      {"key":"zigen","label":"字形","text":Nx,"cites":[]},
      {"key":"xingpang","label":"形旁声旁","text":a,"cites":[]},
      {"key":"hengxiang","label":"横向对照","text":b,"cites":[]},
      {"key":"shengmu","label":"声母义","text":c,"cites":[]}]}
b="同取寺部「手握之／所持以待」一面，形符各定其落点；故声符给义、形符定落点。"
for ch,p,Bx,a,c in D:
    json.dump(card(ch,p,BS,N,a,b,c),open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("写卡",len(D))
def B(ch): return "源自《系統漢語》第413部「寺部」（卷六十七 足）；字卡五步规程。"
cl=[{"id":f"bdc-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{t[0]}（字卡）",
   "statement":f"{t[0]}（{t[1]}）：{t[2]}","boundary":B(t[0]),"permission":"public",
   "fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,t in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡413寺部b2026-10-23","risk":"low","claims":cl},
          open(r"intake\20261023-字卡413寺部b.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡413寺部b.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))