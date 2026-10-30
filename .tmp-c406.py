import json,subprocess,os,glob
B=("部首其（jī）：甲骨文象箕形，周中期金文下加「丌」表聲兼表意（淺平如丌），戰國或从竹；《說文》「簸也」。"
   "轉義：箕主盛裝→代詞（他/它/那）；編紋呈螺旋→週期（借作期）；編結緊密→密謀（與基同）。"
   "字族衍義：①箕狀（盤踞、面具）②箕紋形（周繞、交會）③博棋（欺、謀）。")
N="字形：古文字字形庫未收；原稿該部有「▲玉箕（漢）」「▲銀絲網格木圍棋盤（遼）」等圖，可參。"
D=[
("𤪌","qí",B,"从玉綦聲，《說文》「弁飾，往往冒玉也」，徐鍇謂「綴玉于武冠，若棊子之列布」——皮帽上列玉如棋子。","②組之顯例：玉列如棋布，以玉定落點。","q「親缺」取「親」：玉相親而列。"),
("稘","jī",B,"从禾其聲，《說文》「復其時也」，引《虞書》「稘三百有六旬」，即「期」，取禾之生長週期。","②組：禾一年一熟而復，正週期之義，以禾定落點。","j「聚決」取「聚」：禾聚而成實。"),
("簊","jī",B,"从竹其聲，《玉篇》「居其切，音基」，竹名。","①組：竹之為箕者，以竹定類。","j「聚決」取「聚」：竹聚成叢。"),
("帺","qí",B,"从巾其聲，《集韻》引《說文》「帛蒼艾色」，未嫁女所服；jì 又繫也。","②組：布帛紋色如箕紋，以巾定落點。","q「親缺」取「親」：帛相親而文。"),
("粸","qí",B,"从米其聲，《集韻》「餅屬，亦作𪍀」。","①組：餅形圓扁如箕，以米定落點。","q「親缺」取「親」：米相親成餅。"),
("蜝","qí",B,"从虫其聲，《集韻》「彭蜝，蟲名，似蠏而小，不可食」；蜞為水蛭（螞蟥），通作蜝。","①組：蟲形盤踞如箕，以虫定落點。","q「親缺」取「親」：蟲聚而親。"),
("䳢","qí",B,"从鳥其聲，《集韻》「小鴈」，或指鵂鶹（貓頭鷹）。","①組：鳥蹲踞如箕，以鳥定落點。","q「親缺」取「親」：鳥群相親。"),
("錤","jī",B,"从金其聲，《廣韻》「鎡錤，大鉏」——大鋤，指其寬大如箕。","①組：器形寬大如箕，以金定落點。","j「聚決」取「聚」：鋤聚土。"),
("䑴","qí",B,"从舟其聲，《博雅》「䑴艃，舟也」。","①組：舟中凹如箕，以舟定落點。","q「親缺」取「親」：舟水相親。"),
("惎","jì",B,"从心其聲，《說文》「毒也」，引《周書》「來就惎惎」（渠記切）；《廣雅》志也，《廣韻》謀也。","③組：博棋者以謀相毒，以心定落點。","j「聚決」取「決」：謀決於心。"),
("諅","jì",B,"从言其聲，《說文》「忌也」，引《周書》「上不諅于凶德」；jī 謀也。","③組：以言定落點——以言相忌。","j「聚決」取「決」：言出而決。"),
("欺","qī",B,"从欠其聲，《說文》「詐欺也」（去其切）。","③組之要：博棋以詐取勝，故欺从「其」；欠（張口出氣）定其落點。","q「親缺」取「缺」：言缺而不實。"),
]
def card(ch,p,a,b,c):
    return {"char":ch,"pinyin":p,"bus":[],"sections":[
      {"key":"bengen","label":"字根本義","text":B,"cites":[]},
      {"key":"zigen","label":"字形","text":N,"cites":[]},
      {"key":"xingpang","label":"形旁声旁","text":a,"cites":[]},
      {"key":"hengxiang","label":"横向对照","text":b,"cites":[]},
      {"key":"shengmu","label":"声母义","text":c,"cites":[]}]}
for ch,p,_B,a,b,c in D:
    json.dump(card(ch,p,a,b,c),open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("写卡",len(D))
ST={"𤪌":"《说文》「弁饰，往往冒玉也」，徐锴谓「缀玉于武冠，若棊子之列布」。","稘":"《说文》「复其时也」，引《虞书》「稘三百有六旬」，即「期」。","簊":"《玉篇》「居其切，音基」，竹名。","帺":"《集韵》引《说文》「帛苍艾色」，未嫁女所服；jì 又系也。","粸":"《集韵》「饼属，亦作𪍀」。","蜝":"《集韵》「彭蜝，虫名，似蠏而小，不可食」；蜞为水蛭，通作蜝。","䳢":"《集韵》「小鴈」，或指鵂鶹（猫头鹰）。","錤":"《广韵》「鎡錤，大鉏」——大锄，指其宽大如箕。","䑴":"《博雅》「䑴艃，舟也」。","惎":"《说文》「毒也」，引《周书》「来就惎惎」；《广韵》谋也。","諅":"《说文》「忌也」，引《周书》「上不諅于凶德」；jī 谋也。","欺":"《说文》「诈欺也」。"}
cl=[]
BK="源自《系統漢語》第394部「其部」；字卡五步规程。"
for i,(ch,p,_B,a,b,c) in enumerate(D,1):
    cl.append({"id":f"bta-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡）",
      "statement":f"{ch}（{p}）：{ST[ch]}","boundary":BK,"permission":"public",
      "fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"})
json.dump({"schema_version":1,"intent":"字卡394其部尾2026-10-23","risk":"low","claims":cl},
          open(r"intake\20261023-字卡394其部尾.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡394其部尾.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    b=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",b,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",b,"--apply","--content-hash",h); run("bundle-apply",b,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",b,"err",v.get("errors"))