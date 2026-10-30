import json,subprocess,os,glob
BZ=("【才部·𢦏声】「𢦏（𢦒）」从戈才声：「才」指花果之梗，从戈表用戈割取，本义采摘花果；转义伤害（《说文》「伤也」）。字族衍义：①指梗，表示承载 ②指采摘，表示受伤害之后的剩余。")
BR=("【才部·再声】「再（𠕂𠕅）」甲骨文从丙才声：「丙」指柄，「才」指花果之梗（其实也是柄）；因「丙」也可指器物上的孔，从「才」表明是梗一般的柄而已。转义：由柄之连接器物，引申指两次、重复、连续（《玉篇》「两也、重也、仍也」）。辯證：小篆已看不出「才」声，故《说文》「一举而二也，从冓省」析形不确。字族衍义：表示覆载。")
BX=("【才部·卂声】「卂」甲骨文本从水才声，与「𡿧」同源，指水灾，是「汛」的初文，指雨季江河水位暴涨（《广韵》「水貌」）。转义：由暴涨引申迅速（《玉篇》「疾飞也，亦作迅」）。辯證：西周金文将「水」置于右上角，小篆遂演变得近似「飛」字无羽毛，故《说文》「疾飞也，从飛而羽不见」析形不确。字族衍义：指迅疾。")
N="字形：古文字字形库未收；原稿才部有「▲花的结构图」「▲《种竹斋》局部」「▲桃花汛期的壶口瀑布」可参。"
D=[
("儎","zài",BZ,"《汉典》「运载的货物；运载、承受」——载之名词化。","𢦏族①之实：以「人」定其负，人所载者为儎。","z「凿总」取「总」：总载于身。"),
("哉","zāi",BZ,"从口𢦏声，《说文》「言之间也」祖才切——语间虚词，表疑问反问感叹；《尔雅》「哉，始也」。","𢦏族①之语：以「口」定其用，语间停顿处即「始」。","z「凿总」取「总」：总语而发。"),
("渽","zāi",BZ,"《集韵》「水名。《禹贡》蒙山溪，大渡水东南至南安入渽」——今四川大渡河的古称。","𢦏族①之地：以「水」定其名。","z「凿总」取「总」：众水总汇。"),
("賳","zāi",BZ,"《字彙》「货也，财也」——货物财货。","𢦏族①之富：以「贝」定其质，所载之财。","z「凿总」取「总」：总聚其财。"),
("栽","zài",BZ,"从木𢦏声，《说文》「筑墙长版也」昨代切；zāi《正字通》「移植也。又稚曰栽，长曰树」——移植幼苗。","𢦏族①之植：以「木」定其物，栽而承其生。","z「凿总」取「凿」：凿土而植。"),
("戴","dài",BZ,"从異𢦏声，《说文》「分物得增益曰戴」都代切；《小尔雅》「覆也」、《释名》「载也，载之于头也」——载之于头。","𢦏族①之最：以「異」定其首，载物于顶即戴。","d「囤动」取「囤」：物囤于首。"),
("瀻","dài",BZ,"《集韵》「酒不清」——酒上面浮有酒糟。","𢦏族②之浊：以「水」定其状，割取之余而浊。","d「囤动」取「囤」：糟囤于面。"),
("襶","dài",BZ,"《集韵》「褦襶，不晓事」；《篇海》引魏程晓诗「今世褦襶子，触热到人家」——当暑而盛服请见，不通事理。","𢦏族②之状：以「衣」定其形，长衣不通世故。","d「囤动」取「囤」：衣囤其身。"),
("酨","zài",BZ,"从酉𢦏声，《说文》「酢浆也」徒奈切——醋、坏了的酒；《玉篇》「释米汁也」。","𢦏族②之味：以「酉」定其质，酿败而酸。","z「凿总」取「凿」：酸凿其味。"),
("𩯰","jié",BZ,"从髟截声，《说文》「束发少也」子结切——应指剪发；jì《集韵》「露髻曰𩯰」。","𢦏族②之发：以「髟」定其处，截而短。","j「聚决」取「决」：决断而截。"),
("洅","zài",BR,"从水再声，《说文》「雷震洅洅也」作代切——雷声震动。","再族之直：以「水」状其声，雷一再震。","z「凿总」取「凿」：雷凿而震。"),
("迅","xùn",BX,"从辵卂声，《说文》「疾也」息进切——疾速。","卂族之直：以「辵」定其动，水暴涨之疾。","x「续消」取「续」：疾行不断。"),
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
ST={"儎":"《汉典》「运载的货物；运载、承受」。","哉":"《说文》「言之间也」——语间虚词；《尔雅》「哉，始也」。","渽":"《集韵》水名，《禹贡》大渡水入渽——今大渡河古称。","賳":"《字彙》「货也，财也」。","栽":"《说文》「筑墙长版也」；又「移植也，稚曰栽，长曰树」。","戴":"《说文》「分物得增益曰戴」；《释名》「载也，载之于头也」——载之于头。","瀻":"《集韵》「酒不清」——酒面浮糟。","襶":"《集韵》「褦襶，不晓事」——暑日盛服请见，不通世故。","酨":"《说文》「酢浆也」——醋、坏酒。","𩯰":"《说文》「束发少也」——剪发；又「露髻曰𩯰」。","洅":"《说文》「雷震洅洅也」——雷声震动。","迅":"《说文》「疾也，从辵卂声」——疾速。"}
cl=[{"id":f"bzj-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{d[0]}（字卡）",
   "statement":f"{d[0]}（{d[1]}）：{ST[d[0]]}","boundary":"源自《系統漢語》第400部「才部」（卷六十六 采）；字卡五步规程。","permission":"public",
   "fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,d in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡400才部𢦏支余再支卂支2026-10-23","risk":"low","claims":cl},
          open(r"intake\20261023-字卡400才部余支.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡400才部余支.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    b=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",b,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",b,"--apply","--content-hash",h); run("bundle-apply",b,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",b,"err",v.get("errors"))