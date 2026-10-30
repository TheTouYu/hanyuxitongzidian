import json,subprocess,os,glob
B4=("部首其（jī）：甲骨文象箕形，周中期金文下加「丌」表聲兼表意，戰國或从竹；《說文》「簸也」。轉義：箕主盛裝→代詞；編紋螺旋→週期；編結緊密→密謀。"
    "字族衍義：①箕狀（盤踞、面具）②箕紋形（周繞、交會）③博棋（欺、謀）。")
B5=("部首斯（𣂕sī）：从斤其聲——斤指斧頭，其指箕；箕本用竹篾柳條等細長物編成，以斧斫之自然散成細條；《說文》「析也」，引《詩》「斧以斯之」，息移切。"
    "轉義：由箕之被劈開引申分散分開分離（《廣雅》裂也分也、《爾雅》離也）、盡與全部（《集韻》盡也）、近指此也；由散成一條條引申指束髮帛巾（纚，或作縰、斯）。字族衍義：多指破裂、離析、分散。")
N="字形：古文字字形庫未收；原稿該部有插圖可參。"
D=[
("僛","qī",B4,"从人欺聲，《說文》「醉舞皃」，引《詩》「屢舞僛僛」（去其切）；《集韻》「不能自正也」。","③組：醉舞歪斜不能自正，正「欺」之引申，以人定落點。","q「親缺」取「缺」：身不正而缺。"),
("諆","qī",B4,"从言其聲，《說文》「諆，欺也」（去其切）；《廣韻》謀也。","③組：以言定落點——以言相欺。","q「親缺」取「缺」：言虛而缺。"),
("唭","qì",B4,"从口其聲，《集韻》「唭㘈，無聞見也」，一曰紿也（欺），一曰笑皃。","③組：無所聞見而受欺，以口定落點。","q「親缺」取「缺」：耳缺而聲不至。"),
("猉","qí",B4,"从犬其聲，《集韻》「汝南謂犬子為猉」。","①組：犬子盤踞如箕，以犬定落點。","q「親缺」取「親」：犬子相親。"),
("䶞","qí",B4,"从齒其聲，《廣雅》「齧也」。","①組：齒參差如箕紋，以齒定落點。","q「親缺」取「缺」：齒缺而齧。"),
("剘","qí",B4,"从刀其聲，《篇海》「克也，割截也」；《字彙》信也。","③組：割截即「析」，以刀定落點。","q「親缺」取「缺」：刀缺而割。"),
("斯","sī",B5,"部頭本字：从斤（斧）其（箕），以斧斫箕而散成細條，《說文》「析也」，引《詩》「斧以斯之」。","斯部之根：澌（水盡）、𤺊（散聲）、凘（冰流）、𧪷（悲聲）、撕（手裂）皆取「分散」。","s「失收」取「失」：散而失其形。"),
("澌","sī",B5,"从水斯聲，《說文》「水索也」（息移切），水盡；《方言》「澌，盡也」，引申凡物竭盡。","主組：以水定落點——分流而盡。","s「失收」取「失」：水失而盡。"),
("𤺊","xī",B5,"从疒斯聲，《說文》「散聲」（先稽切）；《方言》「披散也，東齊聲散曰𤺊，秦晉聲變曰𤺊，器破而不殊其音亦謂之𤺊」。","主組之要：聲音破裂而散，正是「析」在聲上的落點，以疒定類。","x「續消」取「消」：聲消而散。"),
("凘","sī",B5,"从仌斯聲，《說文》「流仌也」（息移切），冰消而流散；《風俗通》「冰流曰凘，冰解曰冸」。","主組：冰解而散流，以仌定落點。","s「失收」取「失」：冰失其形。"),
("𧪷","xī",B5,"从言斯省聲，《說文》「悲聲也」（先稽切）——撕心裂肺、聲音嘶啞。","主組：悲聲破裂，以言定落點。","x「續消」取「消」：聲嘶而消。"),
("撕","sī",B5,"从手斯聲，《集韻》「斯，析也。或从手」——用手使薄片裂開或離開附著處；xī 提撕，警覺也。","主組：以手定落點——手裂之析，最直。","s「失收」取「失」：手撕而失其連。"),
]
def card(ch,p,Bx,a,b,c):
    return {"char":ch,"pinyin":p,"bus":[],"sections":[
      {"key":"bengen","label":"字根本義","text":Bx,"cites":[]},
      {"key":"zigen","label":"字形","text":N,"cites":[]},
      {"key":"xingpang","label":"形旁声旁","text":a,"cites":[]},
      {"key":"hengxiang","label":"横向对照","text":b,"cites":[]},
      {"key":"shengmu","label":"声母义","text":c,"cites":[]}]}
for ch,p,Bx,a,b,c in D:
    json.dump(card(ch,p,Bx,a,b,c),open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("写卡",len(D))
ST={"僛":"《说文》「醉舞皃」，引《诗》「屡舞僛僛」；《集韵》「不能自正也」。","諆":"《说文》「諆，欺也」；《广韵》谋也。","唭":"《集韵》「唭㘈，无闻见也」，一曰绐也（欺），一曰笑皃。","猉":"《集韵》「汝南谓犬子为猉」。","䶞":"《广雅》「啮也」。","剘":"《篇海》「克也，割截也」；《字彙》信也。","斯":"从斤（斧）其（箕），以斧斫箕而散成细条，《说文》「析也」，引《诗》「斧以斯之」。","澌":"《说文》「水索也」，水尽；《方言》「澌，尽也」，引申凡物竭尽。","𤺊":"《说文》「散声」；《方言》「披散也，东齐声散曰𤺊，秦晋声变曰𤺊」。","凘":"《说文》「流仌也」，冰消而流散；《风俗通》「冰流曰凘，冰解曰冸」。","𧪷":"《说文》「悲声也」——撕心裂肺、声音嘶哑。","撕":"《集韵》「斯，析也。或从手」——用手使薄片裂开或离开附着处。"}
cl=[]
for i,(ch,p,Bx,a,b,c) in enumerate(D,1):
    BK="源自《系統漢語》第394部「其部」；字卡五步规程。" if i<=6 else "源自《系統漢語》第395部「斯部」；字卡五步规程。"
    cl.append({"id":f"btb-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡）",
      "statement":f"{ch}（{p}）：{ST[ch]}","boundary":BK,"permission":"public",
      "fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"})
json.dump({"schema_version":1,"intent":"字卡394尾395斯部2026-10-23","risk":"low","claims":cl},
          open(r"intake\20261023-字卡394尾395头.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡394尾395头.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    b=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",b,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",b,"--apply","--content-hash",h); run("bundle-apply",b,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",b,"err",v.get("errors"))