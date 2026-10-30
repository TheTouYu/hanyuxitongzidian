import json,os,io,re,subprocess
D=r"web\public\cards"
def S(k,l,t): return {"key":k,"label":l,"text":t,"cites":[]}
Y=("部頭易：甲骨文象傾盞注液之形，分化為「易」（施與）與「益」（受注）二系。轉義轉換、改變、容易。辯證：《說文》以蜥蜴為本義不確，西周晚金文盞形已失。音源：借音，義音同「也」。字族衍義：①改易 ②簡易 ③形近「昜」之訛。")
def card(ch,py,pang,lian,sm):
    return {"char":ch,"pinyin":py,"bus":["367.易部"],"sources":["卷六十二  蛇.docx 367.易部"],
            "sections":[S("bengen","字根（第367部：易部）",Y),S("xingpang","形旁·声旁",pang),
                        S("hengxiang","横向比较",lian),S("shengmu","声母义",sm)]}
rows=[
("蜴","xī","蜴＝虫（形旁）＋易（聲旁）。《廣韻》「蜥蜴」——變色龍、四腳蛇；《集韻》「楚謂欺慢為脈蜴」。","①改易：蜴（虫）蜥蜴｜蜥（虫）蜥｜蛇（虫）蛇。","心母x，「失收」取「失」。"),
("鯣","yì","鯣＝魚（形旁）＋易（聲旁）。《篇海》「鱺鯣」魚名，疑指章魚，能變色。","①改易：鯣（魚）魚名｜鰂（魚）烏賊｜魷（魚）魷。","喻母y，不系。"),
("儩","sì","儩＝人（形旁）＋賜聲。 《集韻》「盡也」——人盡、物盡。","①改易：儩（人）盡｜賜（貝）賜｜盡（皿）盡。","心母s，「失收」取「收」。"),
("敡","yì","敡＝攴（形旁）＋易（聲旁），易亦聲。《說文》「侮也」輕侮怠慢；《廣韻》「輕簡為敡」；《廣雅》「轉也」改易。","②簡易：敡（攴）輕侮｜易（皿）簡易｜慢（心）慢。","喻母y，不系。"),
("舓","shì","舓（𦧇）＝舌（形旁）＋易（聲旁）。《說文》「以舌取食也」——用舌取食。","②簡易：舓（舌）舔食｜舐（舌）舐｜舔（舌）舔。","審母sh，「失收」取「收」。"),
("焬","xī","焬（焲焱）＝火（形旁）＋易（聲旁）。《集韻》「乾皃」物被烘乾；yì 火光。","①改易：焬（火）烘乾／火光｜焲（火）火光｜炙（火）炙。","心母x，「失收」取「失」。"),
("𤟍","zhé","𤟍＝犬（形旁）＋易（聲旁）。《說文》「犬張耳皃」——狗張耳、耳能轉動，即「惕」義。","①改易：𤟍（犬）張耳｜惕（心）警戒｜聳（耳）聳。","照母zh，「鑿總」取「鑿」。"),
("𧀩","sì","𧀩＝艸（形旁）＋賜聲。 《說文》「艸也」。","①改易：𧀩（艸）草名｜艸（艸）草｜賜（貝）賜。","心母s，「失收」取「收」。"),
]
for ch,py,pang,lian,sm in rows:
    open(os.path.join(D,ch+".json"),"w",encoding="utf-8",newline="\n").write(json.dumps(card(ch,py,pang,lian,sm),ensure_ascii=False,indent=1))
print("cards",len(rows))
B="源自《系統漢語》卷六十二「蛇」部之「易部」（第367部）；字卡五步规程。"
cl=[(f"zk-{383+i}",f"{ch}本義：{pang.split('。')[0]}",f"{ch}（{py}）：{pang} 橫向：{lian}")
    for i,(ch,py,pang,lian,sm) in enumerate(rows)]
draft={"schema_version":1,"intent":"字卡易部余8条入库 2026-10-23","risk":"low","claims":[]}
for cid,title,stmt in cl:
    draft["claims"].append({"id":cid,"node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":title,"statement":stmt,
      "boundary":B,"permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"})
fn="intake/20261023-字卡第四十批.json"
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