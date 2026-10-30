import json,os,io,re,subprocess
D=r"web\public\cards"
def S(k,l,t): return {"key":k,"label":l,"text":t,"cites":[]}
J=("部頭㞕（屑）：西周金文从尸从夕，「尸」象人蹲踞，「夕」指夜晚——象意人在夜晚摸黑探索、緩緩行進之狀（《廣韻》「動進皃」）。"
   "另解：依小篆从「䏌」，則實同「佾」——一種集體舞蹈（《月令章句》「天子八佾，諸侯六佾，大夫四佾，佾，列也，每佾八人」），人眾列齊，動作難以施展，與夜行摸索同理。"
   "轉義：由黑夜小心行進→細小、瑣碎、恭敬、辛勞（《玉篇》「絜也、碎也、勞也、敬也」）、不得已、偷偷摸摸（《方言》「獪也」）。字族衍義：多指細小。")
def card(ch,py,pang,lian,sm):
    return {"char":ch,"pinyin":py,"bus":["366.夕部"],"sources":["卷六十二  蛇.docx 366.夕部"],
            "sections":[S("bengen","字根（第366部：夕部·㞕族）",J),S("xingpang","形旁·声旁",pang),
                        S("hengxiang","横向比较",lian),S("shengmu","声母义",sm)]}
rows=[
("㞕","xiè","㞕＝尸（蹲踞之人）＋夕（夜），象夜裏摸黑緩行。引申細小、瑣碎、恭敬、辛勞、偷偷摸摸；隸作「屑」。","細小：㞕（尸夕）碎｜屑（尸）同｜瑣（玉）瑣。","心母x，「失收」取「失」：暗中摸索而失。"),
("𣕋","xiè","𣕋（柣榍楔）＝木（形旁）＋㞕（聲旁）。《說文》「限也」門檻；《正字通》「俗楔字」——木楔。","細小：𣕋（木）門限／楔｜閾（門）閾｜楔（木）楔。","心母x，「失收」取「失」。"),
("𪙑","qiè","𪙑＝齒（形旁）＋屑（聲旁）。《說文》「齒差也」上下牙相摩切；《玉篇》「治骨也」啃骨。","細小：𪙑（齒）相摩｜齧（齒）咬｜切（刀）切。","清母q，「親缺」取「缺」：齒相缺而摩。"),
("糏","xiè","糏（𪍛）＝米（形旁）＋屑（聲旁）。《廣韻》「米麥破也」；《集韻》「米粉」「舂餘也」——碎屑。","細小：糏（米）碎米｜屑（尸）屑｜麨（麥）麥屑。","心母x，「失收」取「失」。"),
("碿","sù","碿＝石（形旁）＋屑（聲旁）。《正字通》「磨也，一曰碎石也，當讀如屑」——碎石、磨。","細小：碿（石）碎石｜砂（石）砂｜磨（石）磨。","心母s，「失收」取「收」。"),
("𦵱","xiè","𦵱＝艸（形旁）＋屑（聲旁）。《集韻》「艸名」。","細小：𦵱（艸）草名｜艸（艸）草｜屑（尸）屑。","心母x，「失收」取「失」。"),
("𦞚","xiè","𦞚（𦚡）＝肉（形旁）＋屑（聲旁）。《博雅》「脂也」，一曰臆中脂——脂肪、胸中脂。","細小：𦞚（肉）脂｜脂（肉）脂｜肪（肉）肪。","心母x，「失收」取「失」。"),
("㨝","xiē","㨝＝手（形旁）＋屑（聲旁）。《集韻》「挺出物也，一曰揲也」——挺出、數取。","細小：㨝（手）挺出｜揲（手）揲｜挾（手）挾。","心母x，「失收」取「失」。"),
("㣯","xiè","㣯＝彳（形旁）＋屑（聲旁）。《集韻》「撇㣯，衣服婆娑皃」「㣰㣯，揺也」——衣擺婆娑、搖動。","細小：㣯（彳）婆娑｜撇（手）撇｜搖（手）搖。","心母x，「失收」取「失」。"),
("㴮","xiè","㴮（㴽泧）＝水（形旁）＋屑（聲旁）。《集韻》「瀎㴽，水皃」——水流動之狀。","細小：㴮（水）細流｜瀎（水）水貌｜屑（尸）屑。","心母x，「失收」取「失」。"),
]
for ch,py,pang,lian,sm in rows:
    open(os.path.join(D,ch+".json"),"w",encoding="utf-8",newline="\n").write(json.dumps(card(ch,py,pang,lian,sm),ensure_ascii=False,indent=1))
print("cards",len(rows))
B="源自《系統漢語》卷六十二「蛇」部之「夕部」（第366部·㞕族）；字卡五步规程。"
cl=[(f"zk-{346+i}",f"{ch}本義：{pang.split('。')[0]}",f"{ch}（{py}）：{pang} 橫向：{lian}")
    for i,(ch,py,pang,lian,sm) in enumerate(rows)]
draft={"schema_version":1,"intent":"字卡夕部㞕族10条入库 2026-10-23","risk":"low","claims":[]}
for cid,title,stmt in cl:
    draft["claims"].append({"id":cid,"node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":title,"statement":stmt,
      "boundary":B,"permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"})
fn="intake/20261023-字卡第三十六批.json"
io.open(fn,"w",encoding="utf-8",newline="\n").write(json.dumps(draft,ensure_ascii=False,indent=1))
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
def run(*a):
    p=subprocess.run([r"D:\系统汉字\tools\pkc.cmd",*a],cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",errors="replace",env=env)
    return p.stdout+p.stderr
pid=re.search(r'pln_[0-9a-f]+',run("knowledge-plan","capture","--file",fn,"--format","json")).group(0); print("PLAN",pid)
b=re.search(r'bnd_[0-9a-f]+',run("knowledge-plan","finalize",pid,"--format","json")).group(0); print("BUNDLE",b)
h=re.search(r'"content_hash":\s*"([0-9a-f]{64})"',run("bundle-status",b,"--format","json")).group(1); print("HASH",h)
run("bundle-approve",b,"--apply","--content-hash",h)
print("applied", '"applied": true' in run("bundle-apply",b,"--apply","--content-hash",h))