import json,subprocess,os,glob
BZ=("【才部·𢦏声】「𢦏（𢦒）」从戈才声：「才」指花果之梗，从戈表用戈割取，本义采摘花果；转义伤害（《说文》「伤也」，祖才切）。字族衍义：①指梗，表示承载 ②指采摘，表示受伤害之后的剩余。")
BX=("【才部·卂声】「卂」甲骨文本从水才声，与「𡿧」同源，指水灾，是「汛」的初文，指雨季江河水位暴涨；转义迅速（《玉篇》「疾飞也，亦作迅」）。辯證：西周金文将「水」置于右上角，小篆遂演变得近似「飛」字无羽毛，故《说文》「疾飞也，从飛而羽不见」析形不确。字族衍义：指迅疾。")
BR=("【才部·再声】「再」甲骨文从丙才声：「丙」指柄，「才」指花果之梗（其实也是柄）；因丙亦可指器物上的孔，从才表明是梗一般的柄。转义：由柄之连接器物，引申两次、重复、连续（《玉篇》「两也、重也、仍也」）。辯證：小篆已看不出才声，《说文》「一举而二也，从冓省」析形不确。字族衍义：表示覆载。")
N="字形：古文字字形库未收；原稿才部有「▲花的结构图」「▲桃花汛期的壶口瀑布」可参。"
D=[
("訊","xùn",BX,"从言卂声，《说文》「问也」思晋切——询问；甲金文均不从卂，从「幺」从「人」或「允」从「口」，象意捆而问罪。","卂族之问：以「言」定其动，疾问如汛至。","x「续消」取「续」：诘问连连。"),
("軐","xiàn",BX,"《广韵》「转軐，车迹也」；xìn《玉篇》「车也」。","卂族之车：以「车」定其物，车过留迹。","x「续消」取「续」：车迹延连。"),
("扟","shēn",BX,"从手卂声，《说文》「从上挹也」所臻切——从上面舀取或摘取；《广韵》「从上择取物也」。","卂族之取：以「手」定其动，自上而下取，正与采摘同。","sh「失收」取「收」：收取而上。"),
("蝨","shī",BX,"从䖵卂声，《说文》「啮人虫」所栉切；《六书正讹》「卂即迅字，疾也，虱行疾」——虱子。","卂族之虫：以「䖵」定其类，行疾如汛。","sh「失收」取「收」：附而收血。"),
("煢","qióng",BX,"从卂营省声，《说文》「回疾也」——鸟回转疾飞；《方言》「清也」，清急；《玉篇》「单也、无兄弟也、无所依也、忧思也」。","卂族之孤：以回转疾飞之状定「无依」，声转而义孤。","q「亲缺」取「缺」：孤缺无依。"),
("侢","dài",BR,"《字海》「同戴」——再声之借为戴。","再族之借：字形相借，义随戴。","d「囤动」取「囤」：顶囤于首。"),
("𨚵","zài",BZ,"从邑𢦏声，《说文》「故国，在陈留」作代切——古国名。","𢦏族②之地：以「邑」定其国。","z「凿总」取「总」：邑总其民。"),
("𥅰","zāi",BZ,"《集韵》引《博雅》「𥅰𥉻，视也」，一曰睽也——两眼视线不能集中同视一物。","𢦏族②之视：以「目」定其病，割裂而视不一。","z「凿总」取「凿」：目凿而睽。"),
("𦳦","zāi",BZ,"《玉篇》「草也」；《广韵》「𦳦莳」——草名。","𢦏族②之草：以「艸」定其类。","z「凿总」取「总」：草总生。"),
("䵧","zài",BZ,"《集韵》「染也」——以染料渍之。","𢦏族②之染：以「黑」定其色，割取草木以染。","z「凿总」取「总」：色总于布。"),
("烖","zāi",BZ,"从火𢦏声，《说文》「天火曰烖」祖才切，或从宀火、籀文从𡿧——火灾；《正字通》「凡五行沴气害物者皆曰灾」。","𢦏族②之灾：以「火」定其害，割取之余而遭焚。","z「凿总」取「凿」：火凿而焚。"),
("胾","zì",BZ,"从肉𢦏声，《说文》「大脔也」侧吏切；《正字通》「切肉曰胾」——大块的切肉。","𢦏族②之肉：以「肉」定其物，割而大块，正是「割取」之遗。","z「凿总」取「凿」：刀凿而分。"),
]
def card(ch,p,Bx,a,b,c):
    return {"char":ch,"pinyin":p,"bus":[],"sections":[
      {"key":"bengen","label":"字根本义","text":Bx,"cites":[]},
      {"key":"zigen","label":"字形","text":N,"cites":[]},
      {"key":"xingpang","label":"形旁声旁","text":a,"cites":[]},
      {"key":"hengxiang","label":"横向对照","text":b,"cites":[]},
      {"key":"shengmu","label":"声母义","text":c,"cites":[]}]}
for ch,p,Bx,a,b,c in D:
    json.dump(card(ch,p,Bx,a,b,c),open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("写卡",len(D))
ST={"訊":"《说文》「问也，从言卂声」；甲金文不从卂，从幺从人，象意捆而问罪。","軐":"《广韵》「转軐，车迹也」；《玉篇》「车也」。","扟":"《说文》「从上挹也，从手卂声」——从上面舀取或摘取。","蝨":"《说文》「啮人虫，从䖵卂声」；《六书正讹》「卂即迅字，虱行疾」。","煢":"《说文》「回疾也」；《玉篇》「单也、无兄弟也、无所依也、忧思也」。","侢":"《字海》「同戴」。","𨚵":"《说文》「故国，在陈留，从邑𢦏声」。","𥅰":"《集韵》引《博雅》「视也」，一曰睽也——两眼视线不能集中。","𦳦":"《玉篇》「草也」；《广韵》「𦳦莳」。","䵧":"《集韵》「染也」。","烖":"《说文》「天火曰烖，从火𢦏声」——火灾；《正字通》「凡五行沴气害物者皆曰灾」。","胾":"《说文》「大脔也，从肉𢦏声」；《正字通》「切肉曰胾」——大块切肉。"}
cl=[{"id":f"bzk-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{d[0]}（字卡）",
   "statement":f"{d[0]}（{d[1]}）：{ST[d[0]]}","boundary":"源自《系統漢語》第400部「才部」（卷六十六 采）；字卡五步规程。","permission":"public",
   "fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,d in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡400才部清完2026-10-23","risk":"low","claims":cl},
          open(r"intake\20261023-字卡400才部清完.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡400才部清完.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    b=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",b,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",b,"--apply","--content-hash",h); run("bundle-apply",b,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",b,"err",v.get("errors"))