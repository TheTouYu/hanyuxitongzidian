import json,subprocess,os,glob
B=("部首其（𠀠𠵶𠔋𠥩箕丌亓亣jī）：商代甲骨文本象箕形；周代中期金文開始在下面加「丌」以表聲兼表意（指其淺平如丌）；戰國古文或从竹从丌，表示竹製；後或寫同「几」。"
   "《說文》「簸也」。轉義：箕主用於盛裝，故引申作代詞（他/它/她、那、那些）；又作語氣助詞。箕之編織紋路呈螺旋狀，引申指週期（借作期）；由編結緊密引申指密謀（與基同）。"
   "字族衍義：①箕狀（盤踞、面具）②箕紋形（周繞、交會）③博棋（欺、謀）。")
N="字形：古文字字形庫未收；原稿該部有「▲玉箕（漢）」「▲銀絲網格木圍棋盤（遼）」等圖，可參。"
D=[
("其","qí",B,"部頭本字：甲骨文象箕形，金文加丌表聲兼意，後借作代詞與語氣詞。","全族之根：與基、棋、琪、淇、旗、綦、騏、期、麒、萁同出一形，各以形符定落點。","q「親缺」取「親」：箕聚物而相親。"),
("基","jī",B,"从土其聲，《說文》「牆始也」（居之切），建築物的根腳；《方言》「基，據也，在下，物所依據也」。","①組之根：土在下承物，正是「箕之淺平在下」。","j「聚決」取「聚」：土聚成基。"),
("祺","qí",B,"从示其聲，《說文》「吉也」（渠之切），吉祥；籀文从基。","①組：以示定落點——基立則吉。","q「親缺」取「親」：神親而降吉。"),
("棋","qí",B,"从木其聲，《說文》「博棊也」（渠之切），比賽的棋具；jī 又作根柢、根基。","②組之要：棋局縱橫交會，正取「箕紋周繞交會」；一形兼根柢義，是兩面同源。","q「親缺」取「親」：子與子相親。"),
("琪","qí",B,"从玉其聲，《集韻》玉屬；《爾雅》「東方之美者，有醫無閭之珣玗琪」；或書作𤦢。","②組：玉之紋理美如棋格，以玉定落點。","q「親缺」取「親」：玉相親而成美。"),
("淇","qí",B,"从水其聲，《說文》「水，出河內共北山，東入河」（渠之切），即淇河；源出棋子山，中段有天然太極圖。","②組：水行周繞，如箕紋之旋，以水定落點。","q「親缺」取「親」：水流相親。"),
("旗","qí",B,"从㫃其聲，《說文》「熊旗五遊，以象罰星，士卒以為期」（渠之切）；《釋名》「熊虎為旗，軍將所建」。","②組：旗上紋章與行列相期會，以㫃定落點。","q「親缺」取「親」：眾期於旗下。"),
("綦","qí",B,"从糸其聲，《說文》「帛蒼艾色」（渠之切），未嫁女所服；《儀禮》注「綦，屨系也，所以拘止屨」。","②組：絲縷交織成文，又以繫屨取「拘止」。","q「親缺」取「親」：絲相交而親。"),
("騏","qí",B,"从馬其聲，《說文》「馬青驪，文如博棊也」（渠之切），馬身紋路交錯如棋盤。","②組之顯例：紋如棋格，取「交會」一面。","q「親缺」取「親」：紋相交而親。"),
("期","qī",B,"从月其聲，《說文》「會也」（渠之切），約會；《玉篇》當也、要也、時也、契約也；《廣韻》周年。","②組：日月相會為期，箕紋周而復始為週期。","q「親缺」取「親」：日月相親而會。"),
("麒","qí",B,"从鹿其聲，《說文》「仁獸也，麋身牛尾一角」（渠之切）；《正字通》引張捐「牡曰麒，牝曰麟」。","②組：麟身有棋狀紋，兼①組面具之象（方相蒙倛）。","q「親缺」取「親」：瑞獸相親。"),
("萁","qí",B,"从艸其聲，《說文》「豆莖也」（渠之切），豆稈；《韻會》菜似蕨；古以萁草織箭服。","①組：豆莖叢生而盤，以艸定落點。","q「親缺」取「親」：莖葉相依。"),
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
ST={"其":"甲骨文象箕形，金文加丌表声兼意，后借作代词与语气词；《说文》「簸也」。","基":"《说文》「墙始也」，建筑物的根脚；《方言》「基，据也，在下，物所依据也」。","祺":"《说文》「吉也」，吉祥；籀文从基。","棋":"《说文》「博棊也」，比赛棋具；jī 又作根柢、根基。","琪":"《集韵》玉属；《尔雅》「东方之美者，有医无闾之珣玗琪」。","淇":"《说文》「水，出河内共北山，东入河」，即淇河。","旗":"《说文》「熊旗五游，以象罚星，士卒以为期」；《释名》「熊虎为旗，军将所建」。","綦":"《说文》「帛苍艾色」，未嫁女所服；《仪礼》注「綦，屦系也，所以拘止屦」。","騏":"《说文》「马青骊，文如博棊也」，马身纹路交错如棋盘。","期":"《说文》「会也」，约会；《玉篇》当也、要也、时也、契约也。","麒":"《说文》「仁兽也，麋身牛尾一角」。","萁":"《说文》「豆茎也」，豆秆；《韵会》菜似蕨。"}
cl=[]
BK="源自《系統漢語》第394部「其部」；字卡五步规程。"
for i,(ch,p,Bx,a,b,c) in enumerate(D,1):
    cl.append({"id":f"bt9-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡）",
      "statement":f"{ch}（{p}）：{ST[ch]}","boundary":BK,"permission":"public",
      "fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"})
json.dump({"schema_version":1,"intent":"字卡394其部2026-10-23","risk":"low","claims":cl},
          open(r"intake\20261023-字卡394其部.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡394其部.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    b=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",b,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",b,"--apply","--content-hash",h); run("bundle-apply",b,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",b,"err",v.get("errors"))