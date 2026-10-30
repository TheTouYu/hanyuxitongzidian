import json,os,io,re,subprocess
D=r"web\public\cards"
def S(k,l,t): return {"key":k,"label":l,"text":t,"cites":[]}
Y=("部頭易：早期甲骨文象傾盞向另一器皿灌注液體之形；後減省分化為二——傾盞倒出之狀為「易」（施與、賜給），受注之形為「益」（增益、盈滿），兩字同源。"
   "轉義：由傾盞倒出→相似、轉換、改變（《玉篇》「象也、異也、轉也、變也」）、侵奪、開始；由灌注之簡→容易、平易。"
   "辯證：西周晚期金文盞形已失，《說文》「蜥易，蝘蜓，守宮也，象形」以蜥蜴為本義不確；「裼」本為脫衣之狀，因改易而楷化。音源：借音字，義音同「也」（《詩》「我心易也」《韓詩》作施）。字族衍義：①改易→轉換賜予 ②簡易→直接快捷。")
def card(ch,py,pang,lian,sm):
    return {"char":ch,"pinyin":py,"bus":["367.易部"],"sources":["卷六十二  蛇.docx 367.易部"],
            "sections":[S("bengen","字根（第367部：易部）",Y),S("xingpang","形旁·声旁",pang),
                        S("hengxiang","横向比较",lian),S("shengmu","声母义",sm)]}
rows=[
("易","yì","易＝傾盞注液之象意，本義傾注（施與）；引申轉換、改變、容易。","改易：易（皿）傾注｜益（皿）受注｜換（手）換。","喻母y（零聲母），不系。"),
("痬","yì","痬＝疒（形旁）＋易（聲旁）。《說文》「脈痬也」發狂之病（義即癔），陣發反復；或指傳染病。","①改易：痬（疒）狂病｜癔（疒）癔｜疫（疒）疫。","喻母y，不系。"),
("晹","yì","晹＝日（形旁）＋易（聲旁）。《說文》「日覆雲暫見也」；《廣韻》「日無光」——雲開暫現。","①改易：晹（日）暫見｜暘（日）日出｜昜（日）同。","喻母y，不系。"),
("緆","xī","緆（裼）＝糸（形旁）＋易（聲旁）。《說文》「細布也」細麻布；《釋名》「治也，治其麻使滑易也」——捶擊曝曬使白。","①改易：緆（糸）細布｜裼（衣）脫衣｜錫（金）白錫。","心母x，「失收」取「失」。"),
("錫","xì","錫＝金（形旁）＋易（聲旁）。《說文》「銀鉛之間也」——熔點低、早被利用，與銅共創青銅時代；質軟延展好。","①改易：錫（金）錫｜鉛（金）鉛｜銅（金）銅。","心母x，「失收」取「失」。"),
("惕","tì","惕（悐）＝心（形旁）＋易（聲旁）。《說文》「敬也」——指神色的改變；《玉篇》「憂也、疾也、懼也」。","①改易：惕（心）警惕｜悐（心）同｜懼（心）懼。","透母t，「涂突」取「突」：心忽驚動。"),
("鬄","dí","鬄（髢剔）＝髟（形旁）＋易（聲旁）。《說文》「髲也」假髮；tì 剃也、與剔同。","①改易：鬄（髟）假髮／剃｜髢（髟）髢｜剃（刀）剃。","透母t，「涂突」取「突」：剃而去之。"),
("𩮜","tì","𩮜＝髟＋刀（形旁）＋易（聲旁）。《說文》「鬀髮也」——用刀除髮。","①改易：𩮜（髟刀）剃髮｜鬄（髟）髢｜剃（刀）剃。","透母t，「涂突」取「突」。"),
("䯜","tì","䯜＝骨（形旁）＋易（聲旁）。《說文》「骨間黃汁也」——骨髓，色或紅或黃，隨年齡而變。","①改易：䯜（骨）骨髓｜髓（骨）髓｜骹（骨）骹。","透母t，「涂突」取「突」。"),
("賜","cì","賜＝貝（形旁）＋易（聲旁）。《說文》「予也」給與；《玉篇》「惠也、施也、空盡也」——正承「傾盞倒出」之施與。","①改易：賜（貝）賜予｜施（㫃）施｜貺（貝）貺。","心母c，「失收」取「失」。"),
]
for ch,py,pang,lian,sm in rows:
    open(os.path.join(D,ch+".json"),"w",encoding="utf-8",newline="\n").write(json.dumps(card(ch,py,pang,lian,sm),ensure_ascii=False,indent=1))
print("cards",len(rows))
B="源自《系統漢語》卷六十二「蛇」部之「易部」（第367部）；字卡五步规程。"
cl=[(f"zk-{363+i}",f"{ch}本義：{pang.split('。')[0]}",f"{ch}（{py}）：{pang} 橫向：{lian}")
    for i,(ch,py,pang,lian,sm) in enumerate(rows)]
draft={"schema_version":1,"intent":"字卡易部首10条入库 2026-10-23","risk":"low","claims":[]}
for cid,title,stmt in cl:
    draft["claims"].append({"id":cid,"node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":title,"statement":stmt,
      "boundary":B,"permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"})
fn="intake/20261023-字卡第三十八批.json"
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