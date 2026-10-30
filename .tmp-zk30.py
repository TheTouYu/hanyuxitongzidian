import json,subprocess,os,re,io
B="源自《系統漢語》卷六十二「蛇」部之「益部」（第364部）；字卡五步规程。"
rows=[
("zk-286","益本義：从皿中水滿形，水滿溢出（溢之初文）","益（yì）甲骨文从皿中水滿形，與「易」同源，象水滿溢之狀——《說文》「器滿也」，「溢」之初文；轉義富饒、增加、助益（《說文》「益，饒也」）。"),
("zk-287","溢本義：从水益聲，器滿也","溢（yì）从水、益聲，轉注。《說文》「器滿也」；《小爾雅》「沒也」水氾濫淹沒；《爾雅》「盈也」；《集韻》「米二十四分升之一」。"),
("zk-288","齸本義：从齒益聲，鹿麋粻（反芻）","齸（yì）从齒、益聲，轉注。《說文》「鹿麋粻」——麋鹿反芻嚼食，意即溢出而食；亦指反芻胃（《集韻》「麋鹿受食處」）。"),
("zk-289","鎰本義：从金益聲，金之數（二十兩）","鎰（yì）从金、益聲，轉注。《玉篇》「二十兩」；《集韻》「二十四兩為鎰，通作溢」——金之滿數。"),
("zk-290","賹本義：从貝益聲，記人物也","賹（ài）从貝、益聲，轉注。《廣韻》「記人物也」；商代金文从賏（朋），成串之貝。"),
("zk-291","縊本義：从糸益聲，經也（勒死）","縊（yì）从糸、益聲，轉注。《說文》「經也」（引《春秋傳》「夷薑縊」）；《廣雅》「絞也」——用繩索勒死。"),
("zk-292","搤本義：从手益聲，捉也","搤（è）从手、益聲，轉注。《說文》「捉也」；《集韻》「扼也，持也」；yì 拉也。"),
("zk-293","𪕶本義：从鼠益聲，鼠屬（黃鼠狼）","𪕶（yì）从鼠、益聲，轉注。《說文》「鼠屬，或从豸」——疑指黃鼠狼，捕獵物先吸血如先縊之。"),
("zk-294","蠲本義：从虫益聲，馬蠲（百足蟲）","蠲（juān）从虫、益聲，轉注。《說文》「馬蠲也」百足蟲（線蟲），觸而蜷縮如鐲，故音同卷；《玉篇》「明也、除也、疾也」；《廣韻》「潔也」。"),
("zk-295","鷁本義：从鳥益聲，水鳥（魚鷹）","鷁（yì）从鳥、益聲，轉注。《正字通》「鶂，水鳥，高飛似鴈，色蒼白」——疑即魚鷹，漁民項系繩使不能吞魚，故有縊意。"),
]
draft={"schema_version":1,"intent":"字卡益部10条入库 2026-10-23","risk":"low","claims":[]}
for cid,title,stmt in rows:
    draft["claims"].append({"id":cid,"node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":title,"statement":stmt,
      "boundary":B,"permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"})
fn="intake/20261023-字卡第三十批.json"
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