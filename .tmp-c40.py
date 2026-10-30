import json,os,io,re,subprocess
D=r"web\public\cards"
def S(k,l,t): return {"key":k,"label":l,"text":t,"cites":[]}
J=("部頭㞕（屑）：金文从尸从夕，象人夜裏摸黑緩行（《廣韻》「動進皃」）；小篆从䏌則同「佾」（集體舞列，人多列齊動作難展）。"
   "轉義：細小、瑣碎、恭敬、辛勞、不得已、偷偷摸摸。字族衍義：多指細小。")
Q=("部頭䏌（xì）：本「八月」合體，从月（夕）象月之圓缺、分上弦下弦循環；轉義舞蹈行列有序，分化作「佾」。辯證：《說文》「从肉八聲」因肉月形近而誤。")
def card(ch,py,head,pang,lian,sm):
    return {"char":ch,"pinyin":py,"bus":["366.夕部"],"sources":["卷六十二  蛇.docx 366.夕部"],
            "sections":[S("bengen","字根（第366部：夕部）",head),S("xingpang","形旁·声旁",pang),
                        S("hengxiang","横向比较",lian),S("shengmu","声母义",sm)]}
rows=[
("𠋱","xiè",J,"𠋱（僁）＝人（形旁）＋屑（聲旁）。《集韻》引《說文》「聲也」，一曰僁僁呻吟也——聲音小而連續。","細小：𠋱（人）細聲｜僁（人）同｜呻（口）呻。","心母x，「失收」取「失」。"),
("𡎮","sù",J,"𡎮＝土（形旁）＋屑（聲旁）。《正字通》「細塵」。","細小：𡎮（土）細塵｜塵（土）塵｜屑（尸）屑。","心母s，「失收」取「收」。"),
("𡟩","xiè",J,"𡟩＝女（形旁）＋屑（聲旁）。《集韻》「小皃」。","細小：𡟩（女）小貌｜小（小）小｜屑（尸）屑。","心母x，「失收」取「失」。"),
("𢞜","xiè",J,"𢞜＝心（形旁）＋屑（聲旁）。《集韻》「憂也」。","細小：𢞜（心）憂｜憂（心）憂｜屑（尸）屑。","心母x，「失收」取「失」。"),
("𤸮","sù",J,"𤸮＝疒（形旁）＋屑（聲旁）。《集韻》「蘇骨切，音窣，𤸮𤺐，癡皃」——痴呆貌。","細小：𤸮（疒）癡｜癡（疒）癡｜屑（尸）屑。","心母s，「失收」取「收」。"),
("𧜔","xiè",J,"𧜔＝衣（形旁）＋屑（聲旁）。《龍龕》「俗，先結、子對二反」；疑即「衱」之異體（衣領）。","細小：𧜔（衣）衣領｜衱（衣）衱｜屑（尸）屑。","心母x，「失收」取「失」。"),
("洕","yìn",Q,"洕＝水（形旁）＋䏌（聲旁）。《玉篇》「小水」；《康典》「小水文」。","行列：洕（水）小水｜肸（十）聲布｜佾（人）舞列。","喻母y，不系。"),
]
for ch,py,head,pang,lian,sm in rows:
    open(os.path.join(D,ch+".json"),"w",encoding="utf-8",newline="\n").write(json.dumps(card(ch,py,head,pang,lian,sm),ensure_ascii=False,indent=1))
print("cards",len(rows))
B="源自《系統漢語》卷六十二「蛇」部之「夕部」（第366部）；字卡五步规程。"
cl=[(f"zk-{356+i}",f"{ch}本義：{pang.split('。')[0]}",f"{ch}（{py}）：{pang} 橫向：{lian}")
    for i,(ch,py,head,pang,lian,sm) in enumerate(rows)]
draft={"schema_version":1,"intent":"字卡夕部余7条入库 2026-10-23","risk":"low","claims":[]}
for cid,title,stmt in cl:
    draft["claims"].append({"id":cid,"node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":title,"statement":stmt,
      "boundary":B,"permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"})
fn="intake/20261023-字卡第三十七批.json"
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