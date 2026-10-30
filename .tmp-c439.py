import json,subprocess,os,glob
BF=("【407 足部·奔（二级）】奔（犇逩𧿣𠬼𢍃𡗲𧾭𣦴𥝯𧾜bēn）：从夭从歮——「夭」象人甩开臂膀快跑之形，「歮」为止的三叠、表脚印杂乱，象意狂跑急驰（《广韵》「奔走也」）。"
    "轉義：狂跑多因急变→逃跑、流亡、失败（《释名》「奔，變也，有急變奔赴之也」；《玉篇》「以罪走出他國曰𢍃」）；全力以赴势不可挡→竭尽全力、走向、投靠（奔命、投奔）。"
    "辯證：因「卉」与「歮」形近，战国古文讹作卉、小篆从之，故《说文》「从夭，賁省聲」析形不确。音源：音源字，源自奔跑声；因纷乱义而义音同「分」（《淮南子》高注「奔月，或作坌肉」）。字族衍义：①奔跑→疾速、乱 ②形近「本、𦱠、羍」之讹。")
N="字形：古文字字形库未收。"
D=[
("奔","bēn",BF,N,"从夭从歮，象人甩臂狂跑、脚印杂乱；《释名》「有急變奔赴之也」——逃跑、投奔。","部头本字：夭定其势，歮定其乱。","b「闭剥」取「闭」：气闭而疾。"),
("捹","bèn",BF,N,"《集韵》「手亂皃」——手忙乱。","疾速族①之手：以「手」定其动，手乱而急。","b「闭剥」取「剥」：手剥而乱。"),
("渀","bēn",BF,N,"《字彙補》「與奔音義同」；bèn 入水貌——奔、入水。","疾速族①之水：以「水」定其势，水奔而入。","b「闭剥」取「剥」：水剥岸疾。"),
("逩","bēn",BF,N,"《正字通》「疾走，義同𢍃」；bèn「投向、掙扎」——奔走、投奔。","疾速族①之辵：以「辵」定其行，疾走而去。","b「闭剥」取「闭」：行闭而疾。"),
("𪑖","bēn",BF,N,"《玉篇》「黑𪑖也」；《集韵》「黑也」——黑色。","疾速族①之黑：以「黑」定其色，奔而蒙尘。","b「闭剥」取「闭」：色闭而暗。"),
("喯","pèn",BF,N,"《龍龕》「俗，正作噴」；bēn 打喯儿，说话中的短暂间歇。","疾速族①之口：以「口」定其声，气喷而断。","p「拼辟」取「辟」：气辟而出。"),
("餴","fēn",BF,N,"《玉篇》「半蒸飯也」；《集韵》「一蒸飯也」——米半熟漉出再蒸。","疾速族①之食：以「食」定其法，一蒸而半。","f「附分」取「分」：米分而蒸。"),
("𨁼","bēn",BF,N,"《集韵》「奔，《說文》『走也』，一曰堂上謂之步、門外謂之趍、中廷謂之走、大路謂之𢍃」——大路上跑。","疾速族①之足：以「足」定其行，大路疾走。","b「闭剥」取「剥」：足剥而疾。"),
("𩣺","bēn",BF,N,"《玉篇》「馬走皃」——马奔跑之貌。","疾速族①之马：以「马」定其类，马走如飞。","b「闭剥」取「闭」：蹄闭而疾。"),
("錛","bēn",BF,N,"《集韵》「平木器」——锛子，削平木料的平头斧（用时向下向内砍）。","疾速族①之金：以「金」定其器，向下猛砍。","b「闭剥」取「剥」：斧剥木皮。"),
("倴","bèn",BF,N,"《龍龕》「俗音奔」，同奔；bèn 用同「笨」。","讹混族②之人：以「人」定其状，奔而笨拙。","b「闭剥」取「闭」：人闭而拙。"),
("𡍋","bèn",BF,N,"《漢典》「同笨」——愚笨。","讹混族②之土：以「土」定其质，土厚而钝。","b「闭剥」取「闭」：土闭而钝。"),
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
ST={"奔":"《广韵》「奔走也」——从夭从歮，人甩臂狂跑、脚印杂乱。","捹":"《集韵》「手亂皃」。","渀":"《字彙補》「與奔音義同」；又入水貌。","逩":"《正字通》「疾走，義同𢍃」。","𪑖":"《集韵》「黑也」。","喯":"《龍龕》「俗，正作噴」。","餴":"《玉篇》「半蒸飯也」——米半熟再蒸。","𨁼":"《集韵》「奔，《說文》『走也』」。","𩣺":"《玉篇》「馬走皃」。","錛":"《集韵》「平木器」——锛子。","倴":"《龍龕》「俗音奔」；又用同「笨」。","𡍋":"《漢典》「同笨」。"}
def B(ch): return "源自《系統漢語》第407部「足部」内二级字根奔部（卷六十七 足）；字卡五步规程。"
cl=[{"id":f"bdk-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{d[0]}（字卡）",
   "statement":f"{d[0]}（{d[1]}）：{ST[d[0]]}","boundary":B(d[0]),"permission":"public",
   "fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,d in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡407奔部2026-10-23","risk":"low","claims":cl},
          open(r"intake\20261023-字卡407奔部.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡407奔部.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    b=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",b,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",b,"--apply","--content-hash",h); run("bundle-apply",b,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",b,"err",v.get("errors"))