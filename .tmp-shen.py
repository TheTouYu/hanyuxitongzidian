import sys,json,os,glob,re,subprocess
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
ROOT=r"D:\系统汉字"
sec=[{"key":"bengen","label":"字根本义","text":"【第114部「申部」·申字族一（伸展、延长）】申＝象閃電之形，電之初文；本部音源為雷。胂从肉申聲，取閃電光帶直長之象，指夾在脊骨兩旁的長條肉。","cites":["clm_4F80EBA6D60F208052C6DA76C2"]},
{"key":"zigen","label":"字形","text":"字形：字形庫未收本字；聲根申有 21 形（web/public/glyphs/申/），本部無插圖。","cites":[]},
{"key":"xingpang","label":"形旁声旁","text":"形旁「肉」定類別（身體部位）；聲旁「申」取閃電之伸展、直長；六書：轉注（形聲兼會意）。shēn，《說文》「夾脊肉也」；shèn 為化學借音（砷化氫羟基取代物）。","cites":["clm_BC5802525C2231F8FC6F051536"]},
{"key":"hengxiang","label":"横向对照","text":"申字族一同取「象閃電一樣伸展」：胂（肉）夾脊長條肉、抻（手）拉長、伸（人）展肢申理、紳（糸）禮服大帶、𧌫（虫）虹（籀文从申）。聲符給義、形符定落點。","cites":["clm_BC5802525C2231F8FC6F051536"]},
{"key":"shengmu","label":"声母义","text":"sh（失收）取「收而復發」一面：電光先收後張，胂為貼脊收束之肉條。","cites":[]}]
json.dump({"char":"胂","pinyin":"shēn","bus":[{"num":114,"name":"申"}],"sections":sec},open(ROOT+r"\web\public\cards\胂.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":"lshen001","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":"胂·shēn","statement":"胂：从肉申聲，申取閃電伸展直長之象，指夾在脊骨兩旁的長條肉（《說文》「夾脊肉也」）；shèn 為化學借音。","boundary":"源自《系統漢語》第114部「申部」申字族一；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"}]
json.dump({"schema_version":1,"intent":"胂卡-2026-10-24","risk":"low","claims":cl},open(ROOT+r"\intake\20261024-字卡-胂.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
ENV=dict(os.environ); ENV["PATH"]=ROOT+r"\.runtime\mingit\cmd;"+ENV["PATH"]
PY=ROOT+r"\.runtime\venv\Scripts\python.exe"; SH=ROOT+r"\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=ROOT,capture_output=True,env=ENV); return (r.stdout+b"\n"+r.stderr).decode("utf-8","replace")
out=run("knowledge-plan","capture","--file",ROOT+r"\intake\20261024-字卡-胂.json","--format","json")
print("dup:","PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(ROOT+r"\data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=re.search(r'"content_hash":\s*"([0-9a-f]{64})"',run("bundle-status",bd,"--format","json")).group(1)
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); print("err",json.loads(run("validate","--format","json")).get("errors"),bd)
subprocess.run([ROOT+r"\tools\git.cmd","add","web/public/cards/胂.json","knowledge","data/knowledge","intake/20261024-字卡-胂.json"],cwd=ROOT,capture_output=True,env=ENV)
r=subprocess.run([ROOT+r"\tools\git.cmd","commit","-m","cards+knowledge: 释胂(五步)"],cwd=ROOT,capture_output=True,env=ENV)
print((r.stdout+r.stderr).decode("utf-8","replace")[:60])