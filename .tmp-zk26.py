import json,subprocess,os,re,io
B="源自《系統漢語》卷六十二「蛇」部之「乙部」（第361部）；字卡五步规程。"
rows=[
("zk-245","鳦本義：从鳥乙聲，燕也","鳦（yǐ）从鳥、乙聲，轉注，取燕。《廣韻》「燕也」——疑源於商人燕生神話，而時見蛇吞食燕卵，故以為蛇、燕相關。"),
("zk-246","亄本義：从乙衣省聲，嗇貪也","亄（yì）从乙、衣省聲，轉注，取吞食貪婪。《方言》「亄，嗇貪也，荊汝江湘之間凡貪而不施者謂之亄」。"),
("zk-247","𩚂本義：从食壹聲，飰傷濕也","𩚂（饐饖，yì）从食、壹聲，轉注。《集韻》引《說文》「飰傷濕也」——食物受濕熱而腐臭。"),
("zk-248","㲸本義：从水乙聲，水涸也","㲸（xī）从水、乙聲，轉注。《字彙補》「許泣切，音吸，水涸也」。"),
("zk-249","肊本義：从肉乙聲，胷骨也；氣滿","肊（臆，yǐ）从肉、乙聲，轉注。《說文》「胷骨也」；《廣韻》「氣滿」；或从意作「臆」。"),
("zk-250","𪖐本義：从鼻乙聲，仰鼻也","𪖐（yà/yào）从鼻、乙聲，轉注，取蛇鼻朝上。《玉篇》「仰鼻也」；《集韻》「𪖛𪖐，仰鼻也」。"),
("zk-251","䎲本義：从耳乙聲，聲耴；耳垂皃","䎲（耴，yì/zhé）从耳、乙聲，轉注。《類篇》「聲耴，魚鳥之狀」；zhé「耳垂皃，秦穆公子耳垂字之曰耴」。"),
("zk-252","礼本義：从示乙聲，曲身致敬；禮之古文","礼（禮𠃞，lǐ）从示、乙聲，轉注，取曲身致敬。《集韻》「礼，《說文》履也，所以事神致福也，古作禮、𠃞」；禮从豊（豐盛食物），礼从乙——當指曲身表示尊敬。"),
("zk-253","𨦂本義：从金禮聲，連鉤釣","𨦂（𨰋，lǎi）从金、禮聲，轉注。《集韻》「連鉤釣曰𨦂，或从禮」。"),
("zk-254","䯆本義：从骨乙聲，小骨","䯆（yì）从骨、乙聲，轉注。《篇海》「音弋，小骨」。"),
("zk-255","𧈝本義：从虫乙聲，虫聲；無角龍","𧈝（yà）从虫、乙聲，轉注。《類篇》「乙黠切，音軋，虫聲」；《龍龕》「無角龍也」。"),
("zk-256","劜本義：从力乙聲，勜劜屈強","劜（yà）从力、乙聲，轉注。《集韻》「勜劜，屈強也」——屈曲而倔强。"),
("zk-257","𥃤本義：从目乙聲，目重皮（雙眼皮）","𥃤（𥄩𥆎，jiǎo）从目、乙聲，轉注，取重疊。《字彙》「居小功，音絞，目重皮也」——雙眼皮。"),
]
draft={"schema_version":1,"intent":"字卡乙部12条入库 2026-10-23","risk":"low","claims":[]}
for cid,title,stmt in rows:
    draft["claims"].append({"id":cid,"node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":title,"statement":stmt,
      "boundary":B,"permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"})
fn="intake/20261023-字卡第二十六批.json"
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