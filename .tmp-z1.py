import json, subprocess, os, sys
draft={
 "schema_version":1,
 "intent":"补茁字本义(释字入库) 2026-10-22",
 "risk":"low",
 "claims":[{
  "id":"zhuo-01","node":"hanzi-yinyuan","topic_id":"topic-juan-38-guai",
  "title":"茁本義：从艸出聲，艸初生出地皃，指草芽破土而出",
  "statement":"茁（zhuó《說文》「艸初生出地皃。从艸出聲。《詩》曰：彼茁者葭。鄒滑切」）从艸、出声，是转注字：形符艸定其类为草，声符出取其本义「自内而出」，故本义指草芽冒出地面。《廣雅》「出也」正用此义；zhú 读为名物，《廣韻》「草牙也」，指草芽；《集韻》又记草名葫䔞。凡从出之字各以形符定落点：拙（手）不能出巧、黜（黑）贬而出朝、掘（手）挖而出之、崛（山）突出而起、屈（尾）不得出而曲，皆同一「出」义之正反两面。",
  "boundary":"源自《系統漢語》卷三十八「夬」出部。",
  "permission":"public","fact_classes":["evidence_scope"],
  "duplicate_resolution":"create_distinct_with_boundary"}]}
os.makedirs("intake",exist_ok=True)
fn="intake/20261022-茁.json"
open(fn,"w",encoding="utf-8",newline="\n").write(json.dumps(draft,ensure_ascii=False,indent=1))
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
def run(*a):
    p=subprocess.run([r"D:\系统汉字\tools\pkc.cmd",*a],cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",errors="replace",env=env)
    return p.stdout+p.stderr
out=run("knowledge-plan","capture","--file",fn,"--format","json")
import re
m=re.search(r'pln_[0-9a-f]+',out); print("PLAN",m.group(0) if m else out[-400:])
if not m: sys.exit(1)
pid=m.group(0)
print(run("knowledge-plan","check",pid,"--mode","delta")[-200:])
fin=run("knowledge-plan","finalize",pid,"--format","json"); print("FIN",fin[-400:])
b=re.search(r'bnd_[0-9a-f]+',fin)
if b:
    st=run("bundle-status",b.group(0),"--format","json"); print("STATUS",st[-300:])