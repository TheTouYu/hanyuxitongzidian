import json,subprocess,os,glob
BS="【408 止部·是（二级）】是＝甲骨文从日止声，象太阳运行（《正字通》「与时通」）；引申正、直、正确；日升如提→移动提起；日行→移动、刮削、阻滞；日色→赤。字族衍义：②日行，表示移动、刮削、阻滞、安稳 ③日色，表示色赤。"
N="字形：古文字字形库未收。"
D=[
("遈","shí","《广韵》「流行皃」，《集韵》「行也」——行走貌。","日行族②之辵：以「辵」定其动，日行于天。","sh「失收」取「失」：行而逝去。"),
("徥","shì","《说文》「徥徥，行皃」，《方言》「細而有容謂之徥」；tǐ 止也。","日行族②之彳：以「彳」定其行，日移而步。","sh「失收」取「收」：行有所止。"),
("𡰖","dī","《说文》「𤿑不能行，為人所引，曰𡰖𡰡」——脚跛被牵引而行。","日行族②之尣：以「尣」（跛）定其困，日行而人不能行。","d「囤动」取「囤」：困而不前。"),
("偍","tí","《荀子》「難進曰偍」——行动迟缓。","日行族②之人：以「人」定其行，日行舒缓则人迟。","t「涂突」取「涂」：缓行如涂。"),
("䐎","tí","《集韵》「𦠓䐎，強脂也」——刮油。","日行族②之肉：以「肉」定其物，刮削去脂。","t「涂突」取「涂」：刮而涂去。"),
("㓳","dī","《广韵》「剅㓳，以刀解物」——以刀割开。","日行族②之刀：以「刀」定其动，刮削如日行。","d「囤动」取「动」：刀动而解。"),
("𦧧","shì","《类篇》「与舓同」——舔食。","日行族②之舌：以「舌」定其动，舐而移动。","sh「失收」取「收」：舌收而舐。"),
("堤","dī","《说文》「滯也，从土是聲」——筑土遏水；shí 堤封、总括。","日行族②之土：以「土」定其物，日行有阻则土遏水。","d「囤动」取「囤」：土囤而阻。"),
("寔","shí","《说文》「止也，从宀是聲」——止息、放置；《尔雅》「是也」，通「实」。","日行族②之宀：以「宀」定其处，日止而息。","sh「失收」取「收」：收止而实。"),
("㼵","dì","《玉篇》「小盆也」，《广韵》「小甕」。","日行族②之瓦：以「瓦」定其器，小器如日之圆。","d「囤动」取「囤」：器囤而盛。"),
("禔","zhī","《说文》「安福也，从示是聲」——安宁。","日行族②之示：以「示」定其福，日安则福。","zh「凿总」取「总」：福总而安。"),
("媞","shì","《说文》「諦也，一曰妍黠也，一曰江淮之間謂母曰媞」——审谛、妍巧、母亲。","日行族②之女：以「女」定其人，日明则审谛。","sh「失收」取「收」：审而收察。"),
]
def card(ch,p,Bx,Nx,a,b,c):
    return {"char":ch,"pinyin":p,"bus":[],"sections":[
      {"key":"bengen","label":"字根本义","text":Bx,"cites":[]},
      {"key":"zigen","label":"字形","text":Nx,"cites":[]},
      {"key":"xingpang","label":"形旁声旁","text":a,"cites":[]},
      {"key":"hengxiang","label":"横向对照","text":b,"cites":[]},
      {"key":"shengmu","label":"声母义","text":c,"cites":[]}]}
for t in D:
    ch,p,Bx = t[0],t[1],t[2]; a = t[3] if len(t)>3 else ""
    c = t[4] if len(t)>4 else ""
    b = "同取「日行」一面（移动、刮削、阻滞、安稳），形符各定落点；故声符给义、形符定落点。"
    json.dump(card(ch,p,Bx,N,a,b,c),open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("写卡",len(D))
ST={"遈":"《广韵》「流行皃」，《集韵》「行也」——行走貌。","徥":"《说文》「徥徥，行皃」；tǐ 止也。","𡰖":"《说文》「𤿑不能行，為人所引」——脚跛被牵引。","偍":"《荀子》「難進曰偍」——行动迟缓。","䐎":"《集韵》「𦠓䐎，強脂也」——刮油。","㓳":"《广韵》「剅㓳，以刀解物」——以刀割开。","𦧧":"《类篇》「与舓同」——舔食。","堤":"《说文》「滯也，从土是聲」——筑土遏水；shí 堤封、总括。","寔":"《说文》「止也，从宀是聲」——止息；通「实」。","㼵":"《玉篇》「小盆也」，《广韵》「小甕」。","禔":"《说文》「安福也，从示是聲」——安宁。","媞":"《说文》「諦也，一曰妍黠也」——审谛、妍巧；又母亲。"}
def B(ch): return "源自《系統漢語》第408部「止部」内二级字根是部（卷六十七 足）；字卡五步规程。"
cl=[{"id":f"bds-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{d[0]}（字卡）",
   "statement":f"{d[0]}（{d[1]}）：{ST[d[0]]}","boundary":B(d[0]),"permission":"public",
   "fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,d in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡408是部续2026-10-23","risk":"low","claims":cl},
          open(r"intake\20261023-字卡408是部续.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡408是部续.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    b=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",b,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",b,"--apply","--content-hash",h); run("bundle-apply",b,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",b,"err",v.get("errors"))

