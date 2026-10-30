import json,subprocess,os,glob
BB=("【407 足部·步（二级）】步（歨歩𡵯𣥶𣥕𣥗bù）：象一前一后两脚印形，象意徒步行走（《说文》「行也，从止𣥂相背」）。"
    "也可视为止的二叠表脚印多（三叠为歮、四叠为歰），或象许多人行走（分化作徙）、行走艰难（分化作歰）、走得快（分化作奔）。"
    "轉義：步间距离→六尺（《玉篇》「六尺為步」）；步行之状→缓慢徐行（《释名》「徐行曰步」）；赤足印常见泥泞沙滩→停船码头（《正字通》「水際渡頭曰步」）；行之所至→地步、时运；循脚印可追踪→跟随、步韵。"
    "音源：音源字，源自脚步声；义音通「甫」（《周礼》郑注「故書酺或為步」）。字族衍义：①步行→踩踏徒步 ②脚印之状→宽扁 ③形近「乞」之讹。")
N="字形：古文字字形库未收。"
D=[
("步","bù",BB,N,"象一前一后两脚印，象意徒步行走；《玉篇》「六尺為步」；《释名》「徐行曰步」。","部头本字：两止相背，前后相随。","b「闭剥」取「闭」：两趾开合。"),
("荹","bù",BB,N,"《说文》「亂艸，从艸步聲」；《玉篇》「牛馬草，亂藁也」——牛马踩过的乱草。","踩踏族①之艸：以「艸」定其境，足踏草乱。","b「闭剥」取「剥」：踏而剥乱。"),
("踄","bù",BB,N,"《说文》「蹈也，从足步聲」——步行、践踏。","踩踏族①之足：以「足」定其动，践而蹈之。","b「闭剥」取「剥」：足剥于地。"),
("涉","shè",BB,N,"《说文》「徒行厲水也，从沝从步」；《尔雅》「繇膝以上為涉」——徒步过河；又经历、泛览。","踩踏族①之水：以「水」定其境，步而入水。","sh「失收」取「失」：涉水失足。"),
("捗","bù",BB,N,"《集韵》「捗攎，收斂也」；zhì「打也」——收敛乱草、击打。","踩踏族①之手：以「手」定其动，收而聚之。","b「闭剥」取「剥」：手剥而收。"),
("埗","bù",BB,N,"同「埠」，方言指码头。","踩踏族①之土：以「土」定其处，水际渡头。","b「闭剥」取「闭」：土闭水际。"),
("𩣝","bù",BB,N,"《玉篇》「習馬，今作步」——遛马。","踩踏族①之马：以「马」定其类，牵马缓行。","b「闭剥」取「闭」：马闭而驯。"),
("㻉","bù",BB,N,"《篇海》「㻉瑤，美玉」；《释名》「步摇上有垂珠，步則摇動也」——步摇首饰。","踩踏族①之玉：以「玉」定其物，行一步则摇。","b「闭剥」取「剥」：珠剥而摇。"),
("陟","zhì",BB,N,"《说文》「登也，从𨸏从步」；《广韵》「升也、進也」——登升，与「降」相对（步之趾朝上故为升）。","踩踏族①之阜：以「阜」定其势，步而上升。","zh「凿总」取「凿」：足凿而登。"),
("騭","zhì",BB,N,"《说文》「牡馬也，从馬陟聲」；《玉篇》「定也、升也」；《六书统》「乘馬登山也」——公马、登升、安定。","踩踏族①之马：以「马」定其类，乘马登山。","zh「凿总」取「凿」：蹄凿而登。"),
("㾟","bù",BB,N,"《集韵》「復病」——病复发。","踩踏族①之疒：以「疒」定其疾，病去而复。","b「闭剥」取「闭」：病闭而伏。"),
("䑰","bù",BB,N,"《集韵》「舟也」；《方言》「艇短而深謂之䑰」——短而深的小船。","踩踏族①之舟：以「舟」定其形，水深而艇短。","b「闭剥」取「闭」：舟闭而藏。"),
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
ST={"步":"《说文》「行也，从止𣥂相背」——象一前一后两脚印；《玉篇》「六尺為步」。","荹":"《说文》「亂艸，从艸步聲」——牛马踩过的乱草。","踄":"《说文》「蹈也，从足步聲」——步行践踏。","涉":"《说文》「徒行厲水也，从沝从步」——徒步过河；又经历。","捗":"《集韵》「捗攎，收斂也」。","埗":"同「埠」，方言指码头。","𩣝":"《玉篇》「習馬，今作步」——遛马。","㻉":"《篇海》「㻉瑤，美玉」；又步摇首饰（步则摇动）。","陟":"《说文》「登也，从𨸏从步」——登升，与降相对。","騭":"《说文》「牡馬也，从馬陟聲」；《六书统》「乘馬登山也」。","㾟":"《集韵》「復病」——病复发。","䑰":"《方言》「艇短而深謂之䑰」——短而深的小船。"}
def B(ch): return "源自《系統漢語》第407部「足部」内二级字根步部（卷六十七 足）；字卡五步规程。"
cl=[{"id":f"bdh-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{d[0]}（字卡）",
   "statement":f"{d[0]}（{d[1]}）：{ST[d[0]]}","boundary":B(d[0]),"permission":"public",
   "fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,d in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡407步部2026-10-23","risk":"low","claims":cl},
          open(r"intake\20261023-字卡407步部.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡407步部.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    b=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",b,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",b,"--apply","--content-hash",h); run("bundle-apply",b,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",b,"err",v.get("errors"))