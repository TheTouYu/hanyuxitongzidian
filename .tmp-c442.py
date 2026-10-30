import json,subprocess,os,glob
BS=("【408 止部·是（二级）】是（昰𣆞shì）：甲骨文从日止声，象意太阳的运行，表示时间（《正字通》「與時通」）；西周金文在日下加「七」作「早」，指早晨上午。"
    "轉義：日光直射→正、直（《正字通》「正也、直也」）→正确、对、法则（《玉篇》「是非也」，《尔雅》「則也」）；太阳在空中移动→上提、移动（战国古文「七」或作「又」，日升如被提挽，分化作「提」）；日月同辉→月边。"
    "辯證：春秋后「早」或作「旦」，下面「一」与「止」合并同「正」，故《说文》「从日正」析形不确——「昰」所从「正」本从止从丁，表示太阳最大的时节。字族衍义：①日悬→提起、悬空。")
N="字形：古文字字形库未收。"
D=[
("是","shì",BS,N,"从日止声，象太阳运行表示时间；引申正、直、正确、法则。","部头本字：日定其象，止定其声。","sh「失收」取「收」：日收而正。"),
("提","tí",BS,N,"《说文》「挈也，从手是聲」——倒持、取出、由低往高由后向前；dī 提防。","日悬族①之手：以「手」定其动，日升如提。","t「涂突」取「突」：提而突上。"),
("匙","chí",BS,N,"《说文》「匕也，从匕是聲」——汤勺；shì 钥匙。","日悬族①之匕：以「匕」定其器，勺起如提。","ch「刺持」取「持」：勺持而举。"),
("鍉","dī",BS,N,"《集韵》「歃血器」；又唾器、箭镞、钥匙。","日悬族①之金：以「金」定其器，取水如提。","d「囤动」取「囤」：器囤而盛。"),
("褆","tí",BS,N,"《说文》「衣厚褆褆，从衣是聲」——衣厚貌（需提起才便行走）；又衣服端正貌。","日悬族①之衣：以「衣」定其物，厚衣需提。","t「涂突」取「突」：衣突而起。"),
("題","tí",BS,N,"《说文》「頟也，从頁是聲」——额头；《广韵》「書題」——题署。","日悬族①之页：以「页」定其处，额在最高。","t「涂突」取「突」：额突而高。"),
("踶","dì",BS,N,"《说文》「躛也，从足是聲」——踢；shì 牛展足；chí 踟蹰不前。","日悬族①之足：以「足」定其动，举足而踢。","d「囤动」取「动」：足动而踢。"),
("𧡨","tí",BS,N,"《说文》「顯也，从見是聲」——显明、视貌。","日悬族①之见：以「见」定其明，日显而见。","t「涂突」取「突」：光突而出。"),
("睼","tiàn",BS,N,"《说文》「迎視也，从目是聲」——迎着看、远视。","日悬族①之目：以「目」定其视，仰目迎日。","t「涂突」取「突」：目突而迎。"),
("趧","tí",BS,N,"《说文》「趧婁，四夷之舞，各自有曲，从走是聲」——踢踏之舞。","日悬族①之走：以「走」定其动，踏地而舞。","t「涂突」取「突」：足突而踏。"),
("翨","chì",BS,N,"《说文》「鳥之強羽猛者，从羽是聲」；《字彙》「與翅同」——翅。","日悬族①之羽：以「羽」定其物，翅展如提。","ch「刺持」取「持」：羽持而张。"),
("痔","zhì",BS,N,"《字彙》「下部病」——痔疮。","讹混族③之疒：以「疒」定其疾，止而不行成疾。","zh「凿总」取「凿」：病凿于下。"),
]
def card(ch,p,Bx,Nx,a,b,c):
    return {"char":ch,"pinyin":p,"bus":[],"sections":[
      {"key":"bengen","label":"字根本义","text":Bx,"cites":[]},
      {"key":"zigen","label":"字形","text":Nx,"cites":[]},
      {"key":"xingpang","label":"形旁声旁","text":a,"cites":[]},
      {"key":"hengxiang","label":"横向对照","text":b,"cites":[]},
      {"key":"shengmu","label":"声母义","text":c,"cites":[]}]}
for ch,p,Bx,Nx,a,b,c in D:
    json.dump(card(ch,p,Bx,Nx,a,b,c),open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("写卡",len(D))
ST={"是":"从日止声，象太阳运行表示时间；引申正、直、正确、法则。","提":"《说文》「挈也，从手是聲」——由低往高、由后向前。","匙":"《说文》「匕也，从匕是聲」——汤勺；又钥匙。","鍉":"《集韵》「歃血器」；又唾器、箭镞、钥匙。","褆":"《说文》「衣厚褆褆，从衣是聲」——衣厚貌。","題":"《说文》「頟也，从頁是聲」——额头；又题署。","踶":"《说文》「躛也，从足是聲」——踢。","𧡨":"《说文》「顯也，从見是聲」——显明。","睼":"《说文》「迎視也，从目是聲」——迎着看。","趧":"《说文》「趧婁，四夷之舞，从走是聲」——踢踏之舞。","翨":"《说文》「鳥之強羽猛者，从羽是聲」——翅。","痔":"《字彙》「下部病」——痔疮。"}
def B(ch): return "源自《系統漢語》第408部「止部」内二级字根是部（卷六十七 足）；字卡五步规程。"
cl=[{"id":f"bdn-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{d[0]}（字卡）",
   "statement":f"{d[0]}（{d[1]}）：{ST[d[0]]}","boundary":B(d[0]),"permission":"public",
   "fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,d in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡408是部2026-10-23","risk":"low","claims":cl},
          open(r"intake\20261023-字卡408是部.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡408是部.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    b=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",b,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",b,"--apply","--content-hash",h); run("bundle-apply",b,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",b,"err",v.get("errors"))