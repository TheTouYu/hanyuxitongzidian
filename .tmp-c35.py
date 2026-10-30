import json,os,io,re,subprocess
D=r"web\public\cards"
def S(k,l,t): return {"key":k,"label":l,"text":t,"cites":[]}
H=("部頭世（丗㔺卋）：象枝葉之形，是「枼（葉）」的初文。轉義更迭、世代、年歲、時代、一生。"
   "辯證：《說文》「三十年為一世，从卅而曳長之」析形不確。音源：風吹樹葉悉索聲。字族衍義：①牽引拖拽 ②層層疊疊 ③改易逾越 ④洩漏光明。")
def card(ch,py,pang,lian,sm):
    return {"char":ch,"pinyin":py,"bus":["365.世部"],"sources":["卷六十二  蛇.docx 365.世部"],
            "sections":[S("bengen","字根（第365部：世部）",H),S("xingpang","形旁·声旁",pang),
                        S("hengxiang","横向比较",lian),S("shengmu","声母义",sm)]}
rows=[
("貰","shì","貰＝貝（形旁）＋世（聲旁）。《說文》「貸也」賒借；《篇海》「恕也」赦免寬縱。","③改易：貰（貝）賒借｜賒（貝）賒｜貸（貝）貸。","審母sh，「失收」取「收」：借而待收。"),
("勩","yì","勩＝力（形旁）＋貰（聲旁）。《說文》「勞也」（《詩》「莫知我勩」）；《段注》「凡物久用而勞敝曰勩」——磨損失稜。","③改易：勩（力）勞敝｜敝（攴）敝｜疲（疒）疲。","喻母y，不系。"),
("跇","yì","跇（𧻸跩𨒧迣）＝足（形旁）＋世（聲旁）。《說文》「述也」超越；《集韻》「超逾也」；chì 跳也踰也。","③改易：跇（足）超越｜踰（足）逾｜跳（足）跳。","喻母y，不系。"),
("迣","zhì","迣（迾）＝辵（形旁）＋世（聲旁）。《說文》「迾也，晉趙曰迣」遮攔；《集韻》「車駕清道」；《廣韻》「度也」。","③改易：迣（辵）遮攔｜迾（辵）清道｜越（走）逾。","照母zh，「鑿總」取「鑿」：截而遮之。"),
("髰","tì","髰（鬄剃𩬲髢）＝髟（形旁）＋世（聲旁）。《集韻》「髲也」假髮；《字彙補》「古文剃字」。","③改易：髰（髟）假髮｜剃（刀）剃｜髢（髟）髢。","透母t，「涂突」取「突」：剃而去之。"),
("鉪","dì","鉪＝金（形旁）＋世（聲旁）。《釋名》「殺也，言殺草也」——金屬農具除草。","③改易：鉪（金）殺草｜刈（刀）刈｜銍（金）銍。","定母d，「囤動」取「動」：動而除草。"),
("泄","yì","泄（洩）＝水（形旁）＋世（聲旁）。《說文》「水，受九江博安洵波，北入氐」——今安徽汲河；引申洩漏、宣洩。","④洩漏：泄（水）漏｜洩（水）同｜漏（水）漏。","喻母y，不系。"),
("怈","yì","怈（𢘽𢖪）＝心（形旁）＋世（聲旁）。《集韻》引《說文》「習也」，一曰明也——心竅透亮。","④光明：怈（心）明｜習（羽）習｜惺（心）惺。","喻母y，不系。"),
("屜","tì","屜＝尸（形旁）＋世（聲旁）。《字彙》「鞌屜」馬鞍墊；今指抽屜、窗櫺——取葉之層層疊疊。","②層疊：屜（尸）抽屜｜屟（尸）屟｜笹（竹）同屜。","透母t，「涂突」取「突」：層層抽出。"),
("笹","tì","笹＝竹（形旁）＋世（聲旁）。《字海》同「屜」；yè 甲骨文从竹从世，當指竹葉。","②層疊：笹（竹）竹葉｜屜（尸）屜｜葉（艸）葉。","透母t，「涂突」取「突」。"),
]
for ch,py,pang,lian,sm in rows:
    c=card(ch,py,pang,lian,sm)
    open(os.path.join(D,ch+".json"),"w",encoding="utf-8",newline="\n").write(json.dumps(c,ensure_ascii=False,indent=1))
print("cards",len(rows))
B="源自《系統漢語》卷六十二「蛇」部之「世部」（第365部）；字卡五步规程。"
cl=[]
for i,(ch,py,pang,lian,sm) in enumerate(rows):
    t=ch
    cl.append((f"zk-{306+i}",f"{t}本義：{pang.split('。')[0]}",f"{t}（{py}）：{pang} 橫向：{lian}"))
draft={"schema_version":1,"intent":"字卡世部余10条入库 2026-10-23","risk":"low","claims":[]}
for cid,title,stmt in cl:
    draft["claims"].append({"id":cid,"node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":title,"statement":stmt,
      "boundary":B,"permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"})
fn="intake/20261023-字卡第三十二批.json"
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