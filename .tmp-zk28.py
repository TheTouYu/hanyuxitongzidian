import json,subprocess,os,re,io
B="源自《系統漢語》卷六十二「蛇」部之「札部」（第362部）；字卡五步规程。"
rows=[
("zk-265","札本義：从木乙聲，牒也，長條木片","札（zhá）从木、乙聲，轉注，取長條。本義長條木片（牒）；轉義隨用途分：簡牘（《釋名》「札，櫛也，編之如櫛，齒相比也」）、船槳（在旁撥水，形似札）、皮革包邊、簡易棺木→夭折瘟疫、車輪→碾壓（義音同軋）。"),
("zk-266","紮本義：从糸札聲，纏弓弝，纏束","紮（zā/zhā）从糸、札聲，轉注，取長條。《廣韻》「纏弓弝也」；《集韻》「纏束也」；zhā 駐紮。"),
("zk-267","𩿤本義：从鳥札聲，鳥雜毛色","𩿤（zhá）从鳥、札聲，轉注。《玉篇》「鳥雜毛色」；《正字通》「鳥，似百舌，喙長，善食魚」。"),
("zk-268","𡥑本義：从子札聲，蟲動也","𡥑（𢧨，sà）从子、札聲，轉注。《五音集韻》「與𢧨同」；《集韻》「𢧨，蟲動也」——蠢動。"),
("zk-269","㳐本義：从水札聲，水流皃","㳐（zhá）从水、札聲，轉注。《集韻》「㳐㳐，水流皃」；《篇海》「㳐㳐，水聲」。"),
("zk-270","𤵦本義：从疒札聲，夭亡","𤵦（zhá）从疒、札聲，轉注，取木片之薄。《釋名》「𤵦，截也，氣傷人，如有斷截也」——夭亡。"),
("zk-271","蚻本義：从虫札聲，麥蚻（小蟬）","蚻（zhá）从虫、札聲，轉注。《方言》「蟬其大者謂之蟧，其小者謂之麥蚻」——小蟬。"),
("zk-272","𧉹本義：从虫札聲，螞蚱","𧉹（zhà）从虫、札聲，轉注，螞蚱（蝗類）。"),
]
draft={"schema_version":1,"intent":"字卡札部8条入库 2026-10-23","risk":"low","claims":[]}
for cid,title,stmt in rows:
    draft["claims"].append({"id":cid,"node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":title,"statement":stmt,
      "boundary":B,"permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"})
fn="intake/20261023-字卡第二十八批.json"
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