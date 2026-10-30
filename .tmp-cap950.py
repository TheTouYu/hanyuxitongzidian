# -*- coding: utf-8 -*-
import json,io,os,subprocess,sys,time
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
ENV["PYTHONUTF8"]="1"; ENV["PYTHONIOENCODING"]="utf-8"
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,env=ENV)
    return (r.stdout or b"").decode("utf-8","replace")+(r.stderr or b"").decode("utf-8","replace")
rows=[("尺","chǐ","從尸足部标记，指膝下至踝之尺骨；引申量尺"),
      ("蚇","chǐ","尺蠖，行动一屈一伸如量尺"),("伬","chǐ","工尺谱记音符号"),("訳","yì","同「譯」"),
      ("𧺫","qǐ","同「起」"),("釈","shì","同「釋」"),("呎","chǐ","英尺旧称"),("屍","shī","《說文》「終主。从尸从死」，屍體")]
claims=[{"id":f"shi-{i:02d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi",
  "title":f"{ch}（第17部尸部）","statement":f"{ch}（{py}）：{tx}。",
  "boundary":"源自《系統漢語》第17部「尸部」（卷三 矢）；字卡五步规程。","permission":"public",
  "fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,py,tx) in enumerate(rows,1)]
p=r"D:\系统汉字\intake\20261028-尸部尺系.json"
json.dump({"schema_version":1,"intent":f"尸部尺系{time.strftime('%Y%m%d-%H%M%S')}","risk":"low","claims":claims},
          io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",p,"--format","json")
j=json.loads(out) if out.strip().startswith("{") else {}
print("ok",j.get("ok"),str(j.get("errors"))[:200])
if j.get("ok"):
    bd=j["bundle_id"]; h=j["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); print(run("validate","--format","json")[:120])