import json,subprocess,os,glob
BS="【412 志部（原属它部，从心从㞢）】志＝从心从㞢：「心」指思想、心思，「㞢」指灵芝、表示有，象意心里所萌生的理想和愿望（《玉篇》「意也、慕也」）。转义：由心里所想，引申指标志、记号、记录（《尔雅》「骨镞不翦羽谓之志」；《集韵》「识，记也，或作志」，旗也或作织、旘、帜）。辯證：因「㞢、之」相混，而志缺乏战国前字形可参照，难肯定从㞢还是从之；「之」声亦可通（《说文》「意也，从心之声」）。但引申指标记、记号、旗帜，与芝草多长在树上、如在树上作记号的特征暗合。字族衍义：①指标志、记号、记忆 ②指芝状，表示芝形、繁盛。"
N="字形：古文字字形库未收。"
D=[
("誌","zhì","《说文》「记志也」；《正字通》「凡史传记事之文曰志」——记载。","记号族①之言：以「言」定其体，记之以言。","zh「凿总」取「凿」：言凿而记。"),
("娡","zhì","《广韵》「有莘氏女，鲧娶之，谓之女娡」——女子人名。","记号族①之女：以「女」定其人，以志为名。","zh「凿总」取「总」：名字总记。"),
("梽","zhì","梽木山，地名，在湖南邵阳。","记号族①之木：以「木」定其地，以木为记。","zh「凿总」取「总」：木聚成山。"),
("痣","zhì","《集韵》「黑子也，又通作志」——黑痣。","记号族①之疒：以「疒」定其类，身上之记如痣。","zh「凿总」取「凿」：黑点如凿。"),
("綕","zhī","《玉篇》「綕，古文织字」——织。","芝盛族②之糸：以「糸」定其物，织缕如芝丛。","zh「凿总」取「总」：丝总而织。"),
("鋕","zhì","《类篇》「铭也」——铭刻。","记号族①之金：以「金」定其器，刻铭为记。","zh「凿总」取「凿」：金凿而铭。"),
("䓌","zhì","《唐韵》「远志，药草，本作志」——远志，取根皮入药，能增强记忆，故名。","芝盛族②之艸：以「艸」定其物，药草以志为名。","zh「凿总」取「总」：草总而药。"),
("覟","zhì","《集韵》「审视也」；《玉篇》「明见也」。","记号族①之见：以「见」定其视，审视而记。","zh「凿总」取「凿」：目凿而审。"),
("𢂴","zhì","《玉篇》「同帜」——旗帜。","记号族①之巾：以「巾」定其物，帜为目见之记。","zh「凿总」取「总」：布总而成帜。"),
("𢙺","zhì","《玉篇》「忘也」——忘记。","记号族①之心：以「心」定其事，忘则记失。","zh「凿总」取「凿」：心凿而空。"),
]
def card(ch,p,Bx,Nx,a,b,c):
    return {"char":ch,"pinyin":p,"bus":[],"sections":[
      {"key":"bengen","label":"字根本义","text":Bx,"cites":[]},
      {"key":"zigen","label":"字形","text":Nx,"cites":[]},
      {"key":"xingpang","label":"形旁声旁","text":a,"cites":[]},
      {"key":"hengxiang","label":"横向对照","text":b,"cites":[]},
      {"key":"shengmu","label":"声母义","text":c,"cites":[]}]}
b="同取志部「心里所萌生／标记记号」一面，形符各定其落点；故声符给义、形符定落点。"
for ch,p,Bx,a,c in D:
    json.dump(card(ch,p,BS,N,a,b,c),open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("写卡",len(D))
def B(ch): return "源自《系統漢語》第412部「志部」（卷六十七 足）；字卡五步规程。"
cl=[{"id":f"bdc-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{t[0]}（字卡）",
   "statement":f"{t[0]}（{t[1]}）：{t[2]}","boundary":B(t[0]),"permission":"public",
   "fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,t in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡412志部2026-10-23","risk":"low","claims":cl},
          open(r"intake\20261023-字卡412志部.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡412志部.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))