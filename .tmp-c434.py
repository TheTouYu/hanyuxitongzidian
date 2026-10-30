import json,subprocess,os,glob
BX=("【407 足部·胥（二级）】胥（𦙃𣆁xū）：从肉疋声——「肉」指肌肉，「疋」指腿，象意腿部肌肉。"
    "轉義：腿肉是动物身上最紧实精美的部分→比喻富有才智、靠走脚跑腿的下层小吏（《集韵》「胥，什長也，有才智者」）；小吏凡事亲历→全面、辅助、观察（《尔雅》「皆也」「相也」，《广韵》「助也」）。"
    "辯證：《说文》「蟹醢也」以蟹酱为本义不确——原稿谓蟹腿肉有硬壳不便吃，古人捣碎成酱，正取腿肉之意，故本义当是腿肉。字族衍义：①腿肉→精美、才智 ②腿行→善于走动 ③腿状→长条如腿之物 ④本应从「楚」→痛楚。")
N="字形：古文字字形库未收。"
D=[
("胥","xū",BX,N,"从肉疋声，象意腿部肌肉；《集韵》「胥，什長也，有才智者」；《尔雅》「皆也」「相也」——小吏、全面、辅助。","部头本字：肉定其质，疋定所从（腿）。","x「续消」取「续」：跑腿相继。"),
("蝑","xū",BX,N,"《说文》「蜙蝑也，从虫胥声」——蟖螽，以翅膀摩发声，古人以为其大腿相切摩而发声；xiè「蟹醢」。","腿肉族①之虫：以「虫」定其类，腿相切而鸣。","x「续消」取「续」：声续不绝。"),
("糈","xǔ",BX,N,"《说文》「糧也，从米胥声」；《玉篇》「祠神米」；《离骚》「懷椒糈而要之」——祭神精米。","腿肉族①之米：以「米」定其物，精米以享神。","x「续消」取「续」：祭续不绝。"),
("稰","xǔ",BX,N,"《字彙》「熟獲曰稰，即今晚稻」；《韻會補》「祭神米」；xū「禾子落皃」。","腿肉族①之禾：以「禾」定其类，晚稻精实。","x「续消」取「续」：禾续而熟。"),
("𧶳","shǔ",BX,N,"《類篇》「䝪，或作𧶳」——送财礼卜问。","腿肉族①之贝：以「贝」定其礼，卜问以财。","sh「失收」取「收」：财收而问。"),
("𥚩","xǔ",BX,N,"《说文》「祭具也，从示胥声」——祭品（精米享神）。","腿肉族①之示：以「示」定其礼，祭具。","x「续消」取「续」：祀续不绝。"),
("揟","xū",BX,N,"《说文》「取水沮也，从手胥声」——滤取水中渣滓；jū「取魚也」。","腿肉族①之手：以「手」定其动，漉而取之。","x「续消」取「续」：水续而漉。"),
("湑","xǔ",BX,N,"《说文》「莤酒也，一曰浚也，一曰露皃」——滤酒去渣、疏浚、露水；《玉篇》「清也」「美皃」。","腿肉族①之水：以「水」定其状，滤而清。","x「续消」取「消」：渣消而清。"),
("醑","xǔ",BX,N,"《集韵》「釃酒也」；《玉篇》「美酒也」；《正字通》「醑為頭酒」——滤过的美酒。","腿肉族①之酉：以「酉」定其类，头酒清美。","x「续消」取「续」：酒续而醇。"),
("諝","xū",BX,N,"《说文》「知也，从言胥声」；《正字通》「詐也」——才智、欺诈。","腿肉族①之言：以「言」定其声，才智之言。","x「续消」取「续」：言续而智。"),
("㥠","xū",BX,N,"《说文》「知也，从心胥声」——才智（心之明）。","腿肉族①之心：以「心」定其能，智由心出。","x「续消」取「续」：思续而明。"),
("縃","xū",BX,N,"《漢典》「同胥」，疑同「絮」——《釋名》「絮，胥也，胥久故解落也」。","腿肉族①之糸：以「糸」定其物，絮久而解。","x「续消」取「消」：絮久消散。"),
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
ST={"胥":"从肉疋声，象意腿部肌肉；《集韵》「胥，什長也，有才智者」——小吏、全面、辅助。","蝑":"《说文》「蜙蝑也，从虫胥声」——蟖螽，大腿相切摩而发声。","糈":"《说文》「糧也」；《玉篇》「祠神米」——祭神精米。","稰":"《字彙》「熟獲曰稰，即今晚稻」；《韻會補》「祭神米」。","𧶳":"《類篇》「䝪，或作𧶳」——送财礼卜问。","𥚩":"《说文》「祭具也，从示胥声」——祭品。","揟":"《说文》「取水沮也，从手胥声」——滤取水中渣滓。","湑":"《说文》「莤酒也，一曰浚也，一曰露皃」——滤酒、疏浚、露水。","醑":"《集韵》「釃酒也」；《玉篇》「美酒也」——滤过的美酒。","諝":"《说文》「知也，从言胥声」；《正字通》「詐也」——才智、欺诈。","㥠":"《说文》「知也，从心胥声」——才智。","縃":"《漢典》「同胥」；《釋名》「絮，胥也，胥久故解落也」。"}
def B(ch): return "源自《系統漢語》第407部「足部」内二级字根胥部（卷六十七 足）；字卡五步规程。"
cl=[{"id":f"bdf-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{d[0]}（字卡）",
   "statement":f"{d[0]}（{d[1]}）：{ST[d[0]]}","boundary":B(d[0]),"permission":"public",
   "fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,d in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡407胥部2026-10-23","risk":"low","claims":cl},
          open(r"intake\20261023-字卡407胥部.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡407胥部.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    b=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",b,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",b,"--apply","--content-hash",h); run("bundle-apply",b,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",b,"err",v.get("errors"))