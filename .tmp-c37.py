import json,os,io,re,subprocess
D=r"web\public\cards"
def S(k,l,t): return {"key":k,"label":l,"text":t,"cites":[]}
X=("部頭夕：象彎月形，指月亮，與「月」同源。轉義夜晚（《說文》「莫也，从月半見」）、傾斜（《廣雅》「衺也」）、墓穴（穸）。"
   "音源：月因形借「缺」，夕因時借「亦」；夜黑易遭蛇咬故又通「也」；夜亦稱「冥」。字族衍義：①夜晚及夜間事物 ②音譯 ③形近「勺、夊、反」之訛。")
M=("部頭名：从口从夕，夜晚昏暗互不相見，自報姓名（《說文》「自命也…冥不相見，故以口自名」）。轉義名稱、旌表、辨明、大而成人。音源：義音同「冥」。字族衍義：①夜晚→朦朧不清。")
def card(ch,py,head,pang,lian,sm):
    return {"char":ch,"pinyin":py,"bus":["366.夕部"],"sources":["卷六十二  蛇.docx 366.夕部"],
            "sections":[S("bengen","字根（第366部：夕部）",head),S("xingpang","形旁·声旁",pang),
                        S("hengxiang","横向比较",lian),S("shengmu","声母义",sm)]}
rows=[
("𥝘","yǒu",X,"𥝘＝禾（形旁）＋夕（聲旁）。《海篇》「音酉，謂穀不成也」——穀不結實。","①夜物：𥝘（禾）穀不成｜秕（禾）秕｜酉（酉）酉。","喻母y，不系。"),
("𧖪","qíng",X,"𧖪＝血（形旁）＋夕（聲旁）。《字彙補》「巨靈切，音擎，見定也」。","①夜物：𧖪（血）見定｜定（宀）定｜擎（手）擎。","羣母q，「親缺」取「親」：血親相定。"),
("𡖋","yì",X,"𡖋（亦掖）＝夕（形旁）＋亦。酒官碑「南由市入為閽，北抵湖出為𡖋」；楊慎曰即古「亦」字，亦古「掖」字，通閽即掖門。","③訛變：𡖋（夕）亦｜亦（亠）亦｜掖（手）掖。","喻母y，不系。"),
("釸","xī",X,"釸（矽）＝金（形旁）＋夕（聲旁）。化學元素「硅」的舊稱，源於拉丁語 Silex（燧石、石英）音譯。","②音譯：釸（金）硅｜矽（石）同｜硒（石）硒。","心母x，「失收」取「失」。"),
("𢗇","zhuǒ",X,"𢗇（㣿）＝心（形旁）＋夕（聲旁）。《龍龕》「㣿的俗字，痛病也」。","③訛變：𢗇（心）痛病｜痛（疒）痛｜㣿（心）同。","照母zh，「鑿總」取「鑿」。"),
("𣏐","sháo",X,"𣏐（杓）＝木（形旁）＋夕（聲旁）。《龍龕》「杓誤，杓正，市若反，木杓也」——形近「勺」之訛。","③訛變：𣏐（木）木杓｜杓（木）杓｜勺（勹）勺。","審母sh，「失收」取「收」。"),
("芕","sháo",X,"芕（芍䒘）＝艸（形旁）＋夕（聲旁）。《本草綱目》「野芕草」；疑「芍」之訛，指荸薺、芍藥、蓮子；suī 同荽。","③訛變：芕（艸）野芕｜芍（艸）芍藥｜荽（艸）荽。","審母sh，「失收」取「收」。"),
("㐴","pān",X,"㐴（攀）＝乙（形旁）＋夕。 《玉篇》「俗攀字」；疑為「反」之訛。","③訛變：㐴（乙）攀｜攀（手）攀｜反（又）反。","滂母p，「拼辟」取「拼」。"),
("㶤","chǎo",X,"㶤＝火（形旁）＋夕。《龍龕》「炒的俗字」。","③訛變：㶤（火）炒｜炒（火）炒｜煼（火）同。","穿母ch，「刺持」取「刺」。"),
("佲","mǐng",M,"佲（𠋶姳）＝人（形旁）＋名（聲旁）。《類篇》「酩酊，醉甚，或作佲」；《正字通》「好也」。","①朦朧：佲（人）醉｜酩（酉）醉｜姳（女）好。","明母m，「蒙末」取「蒙」。"),
]
for ch,py,head,pang,lian,sm in rows:
    open(os.path.join(D,ch+".json"),"w",encoding="utf-8",newline="\n").write(json.dumps(card(ch,py,head,pang,lian,sm),ensure_ascii=False,indent=1))
print("cards",len(rows))
B="源自《系統漢語》卷六十二「蛇」部之「夕部」（第366部）；字卡五步规程。"
cl=[(f"zk-{326+i}",f"{ch}本義：{pang.split('。')[0]}",f"{ch}（{py}）：{pang} 橫向：{lian}")
    for i,(ch,py,head,pang,lian,sm) in enumerate(rows)]
draft={"schema_version":1,"intent":"字卡夕部第二10条入库 2026-10-23","risk":"low","claims":[]}
for cid,title,stmt in cl:
    draft["claims"].append({"id":cid,"node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":title,"statement":stmt,
      "boundary":B,"permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"})
fn="intake/20261023-字卡第三十四批.json"
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