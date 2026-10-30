import json,subprocess,os,re,io
B="源自《系統漢語》卷六十一「犀（屖）」部（第353部）；字卡五步规程。"
items=[
("zk-063","犀本義：甲骨文象獨角犀牛，金文演為从牛㞑聲","犀（xī/sì）甲骨文象獨角犀牛形，本「兕」或「𤉡」（《說文》「如野牛而青，象形」）；西周金文演變成象聲字，从牛㞑聲（《說文》「南徼外牛，一角在鼻，一角在頂，似豕」）。轉義：皮厚作鎧甲→堅牢；角中空堅牢→酒杯飾品；身軀龐大行走遲緩→遲緩，或分化作屖。辯證：本部字根實為「屖」（見屖條），犀之「从牛」為後起。"),
("zk-064","屖本義：从尸辛聲，遲也，本部真字根","屖（xī）＝尸（人跪跽之訛）＋辛（刻刀）。《說文》「遟也。从尸辛聲。先稽切」，滯留不進；《字彙》「堅也」。辯證：甲骨文本从卩从辛，初義當指刻字或紋身，因刻速緩慢而引申遲緩，與犀牛無關；故原稿斷「从字根的角度來說，本部當為『屖』部」。又卩可引申符節，屖另分化作辟（璧之初文）。"),
("zk-065","遲本義：从辵犀聲，徐行也","遲（chí/zhì）从辵、犀聲，屬轉注，聲旁取遲緩。《說文》「徐行也。从辵犀聲，《詩》曰行道遲遲，直尼切」，籀文从屖；《廣韻》「徐也、久也、緩也」；zhì《集韻》「待也」，等待、希望。"),
("zk-066","謘本義：从言屖聲，語諄謘，語言遲鈍","謘（chí）从言、屖聲，屬轉注，聲旁取遲緩。《說文》「語諄謘也。从言屖聲。直離切」，語言遲鈍；《集韻》「啍謘，語不正也」。"),
("zk-067","摨本義：从手犀聲，揩摨，摩也","摨（搱，nái/zhì）从手、犀聲，屬轉注。《集韻》「《博雅》：揩摨，摩也」，揩擦、研磨；zhì《字彙》「摴蒲，采名」，《正字通》「同搱」，古代類似擲骰的賭博遊戲。"),
("zk-068","𧭟本義：从言屖聲，言逸也，失言","𧭟（謘、𧭋，chí）从言、屖聲，屬轉注。《字彙》「言逸也」，失言；《正字通》「俗謘字」。取「語不檢點、脫口而出」。"),
]
draft={"schema_version":1,"intent":"字卡犀部六条入库 2026-10-22","risk":"low","claims":[]}
for cid,title,stmt in items:
    draft["claims"].append({"id":cid,"node":"hanzi-yinyuan","topic_id":"topic-zika-shizi",
      "title":title,"statement":stmt,"boundary":B,"permission":"public",
      "fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"})
fn="intake/20261022-字卡第十批.json"
io.open(fn,"w",encoding="utf-8",newline="\n").write(json.dumps(draft,ensure_ascii=False,indent=1))
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
def run(*a):
    p=subprocess.run([r"D:\系统汉字\tools\pkc.cmd",*a],cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",errors="replace",env=env)
    return p.stdout+p.stderr
out=run("knowledge-plan","capture","--file",fn,"--format","json")
pid=re.search(r'pln_[0-9a-f]+',out).group(0); print("PLAN",pid)
fin=run("knowledge-plan","finalize",pid,"--format","json")
b=re.search(r'bnd_[0-9a-f]+',fin).group(0); print("BUNDLE",b)
h=re.search(r'"content_hash":\s*"([0-9a-f]{64})"',run("bundle-status",b,"--format","json")).group(1)
print("HASH",h)
run("bundle-approve",b,"--apply","--content-hash",h); run("bundle-apply",b,"--apply","--content-hash",h)
print("done")