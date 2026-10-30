import json,os,io,re,subprocess
D=r"web\public\cards"
def S(k,l,t): return {"key":k,"label":l,"text":t,"cites":[]}
H=("部頭世（丗㔺卋）：象枝葉之形，指草木的葉子，是「枼（葉）」的初文（《正字通》引鄭樵「枼卽葉字」）。"
   "轉義：葉春發秋落→更迭（《廣韻》「代也」，父子相代為一世）、年歲、時代、一生。"
   "辯證：《說文》「三十年為一世，从卅而曳長之」析形不確；世義與「三十」無直接關係（三十年一代是後起計算）。"
   "音源：源自風吹樹葉的悉索聲；義音同「蛇」（《史記》「抴獨繭之褕袘」，《漢書》作「袣」）。字族衍義：①葉挂枝頭→牽引拖拽 ②葉多→層層疊疊 ③葉更替→改易逾越 ④葉間縫隙→洩漏光明。")
def card(ch,py,pang,lian,sm):
    return {"char":ch,"pinyin":py,"bus":["365.世部"],"sources":["卷六十二  蛇.docx 365.世部"],
            "sections":[S("bengen","字根（第365部：世部）",H),S("xingpang","形旁·声旁",pang),
                        S("hengxiang","横向比较",lian),S("shengmu","声母义",sm)]}
cards=[
card("世","shì","世＝象枝葉之形（葉之初文），本義草木之葉。引申更迭、世代、年歲、時代、一生。","同取枝葉：世（枼）葉｜枼（木）葉｜葉（艸）葉。","審母sh，「失收」取「收」：葉落而收。"),
card("枼","yè","枼（枽）＝木上世形，象枝葉，葉之初文；引申世系（枼从世）。","同取葉：枼（木）葉｜葉（艸）同｜世（世）世代。","喻母y（零聲母），不系。"),
card("抴","yè","抴＝手（形旁）＋世（聲旁）。《說文》「捈也」——拉引；shé 數也（揲，閱持）。","同取牽引：抴（手）拉｜拽（手）拖｜揲（手）數。","喻母y，不系。"),
card("紲","xiè","紲（緤）＝糸（形旁）＋世（聲旁）。《說文》「系也」（引《春秋傳》「臣負羈絏」）——繩索、馬韁；《釋名》「制也，牽制之也」。","同取繫繩：紲（糸）韁｜緤（糸）同｜縲（糸）纍。","心母x，「失收」取「收」：繫而收之。"),
card("靾","xiè","靾＝革（形旁）＋世（聲旁）。《集韻》「馬被具」；《廣韻》「以馬鞍贈亡人」「系也」——馬鞍具。","同取馬具：靾（革）鞍｜鞍（革）鞍｜韉（革）韉。","心母x，「失收」取「收」：繫馬而收。"),
card("袣","yì","袣（絏）＝衣（形旁）＋世（聲旁）。《集韻》「衣長皃，一曰袖也，亦从曳」；《廣韻》「長被」。","同取衣長：袣（衣）長衣｜曳（曰）拖曳｜絏（糸）繫。","喻母y，不系。"),
card("枻","yì","枻（栧柂）＝木（形旁）＋世（聲旁）。《集韻》「楫謂之枻，一曰柂也」短槳、船舵；xiè 檠枻（正弓弩之器）。","同取槳舵：枻（木）槳｜柂（木）舵｜楫（木）楫。","喻母y，不系。"),
card("呭","yì","呭（詍）＝口（形旁）＋世（聲旁）。《說文》「多言也」（引《詩》「無然呭呭」）；《廣韻》「樂」。","同取多言：呭（口）多言｜詍（言）同｜譊（言）譊。","喻母y，不系。"),
card("齛","xiè","齛＝齒（形旁）＋世（聲旁）。《說文》「羊粻也」羊反芻；shì 同噬（咬）。","同取反芻：齛（齒）反嚼｜齸（齒）鹿反芻｜噬（口）咬。","心母x，「失收」取「收」：食而收。"),
card("伳","xiè","伳＝人（形旁）＋世（聲旁）。《集韻》「侈也」——奢侈。","同取侈：伳（人）侈｜侈（人）侈｜奢（大）奢。","心母x，「失收」取「收」：奢而失收。"),
]
for c in cards:
    open(os.path.join(D,c["char"]+".json"),"w",encoding="utf-8",newline="\n").write(json.dumps(c,ensure_ascii=False,indent=1))
print("cards",len(cards))
B="源自《系統漢語》卷六十二「蛇」部之「世部」（第365部）；字卡五步规程。"
rows=[
("zk-296","世本義：象枝葉之形，草木之葉（枼之初文）","世（shì）象枝葉之形，本義草木之葉，「枼（葉）」之初文；轉義更迭、世代、年歲、時代、一生。辯證：《說文》「三十年為一世，从卅而曳長之」析形不確。音源：風吹樹葉悉索聲。"),
("zk-297","枼本義：木上世形，象枝葉（葉之初文）","枼（yè）从木从世，象枝葉，葉之初文；引申世系（枼从世）。"),
("zk-298","抴本義：从手世聲，捈也（拉引）","抴（yè）从手、世聲，轉注。《說文》「捈也」拉引；shé 數也（《集韻》「揲，閱持也」）。"),
("zk-299","紲本義：从糸世聲，系也（繩索馬韁）","紲（xiè）从糸、世聲，轉注。《說文》「系也」；《玉篇》「馬韁也」；《釋名》「制也，牽制之也」。"),
("zk-300","靾本義：从革世聲，馬被具","靾（xiè）从革、世聲，轉注。《集韻》「馬被具」；《廣韻》「以馬鞍贈亡人」「系也」。"),
("zk-301","袣本義：从衣世聲，衣長皃","袣（yì）从衣、世聲，轉注。《集韻》「衣長皃，一曰袖也」；《廣韻》「長被」。"),
("zk-302","枻本義：从木世聲，楫也（短槳、舵）","枻（yì）从木、世聲，轉注。《集韻》「楫謂之枻，一曰柂也」；xiè 檠枻，正弓弩之器。"),
("zk-303","呭本義：从口世聲，多言也","呭（yì）从口、世聲，轉注。《說文》「多言也」（引《詩》「無然呭呭」）；《廣韻》「樂」。"),
("zk-304","齛本義：从齒世聲，羊粻也（羊反芻）","齛（xiè）从齒、世聲，轉注。《說文》「羊粻也」；shì 同噬（咬）。"),
("zk-305","伳本義：从人世聲，侈也","伳（xiè）从人、世聲，轉注。《集韻》「侈也」奢侈。"),
]
draft={"schema_version":1,"intent":"字卡世部10条入库 2026-10-23","risk":"low","claims":[]}
for cid,title,stmt in rows:
    draft["claims"].append({"id":cid,"node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":title,"statement":stmt,
      "boundary":B,"permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"})
fn="intake/20261023-字卡第三十一批.json"
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