# -*- coding: utf-8 -*-
"""给每个部的部首字本义条补一句声母义（revise-claim 批量）。"""
import re, glob, os, json, subprocess, sys

ROOT = r"D:\系统汉字"
PYC = [os.path.join(ROOT, ".runtime", "venv", "Scripts", "python.exe"),
       os.path.join(ROOT, "tools", "pkc_tmpfix.py")]

sm = open(os.path.join(ROOT, "knowledge", "hanzi-yinyuan", "02z-shengmu-yi.md"), encoding="utf-8").read()
smp = re.compile(r"### (\S+?)部：声母义（([^）]*)）\s*\n\n(.*?)\n\n#### 适用边界", re.S)
BU = {}
for m in smp.finditer(sm):
    body = m.group(3)
    g = re.search(r"声母义：(\S+?)（(.+?)音）", body)
    mi = re.search(r"拟态义「(.+?)」", body)
    pc = re.search(r"同部位\s*(\d+)\s*字，占\s*(\d+)%", body)
    BU[m.group(1)] = {"grade": m.group(2).split("·")[-1], "ini": g.group(1) if g else "",
                      "grp": g.group(2) if g else "", "mime": mi.group(1) if mi else "",
                      "pct": pc.group(2) if pc else ""}
zm = re.search(r"### 零声母诸部.*?\n\n(.*?)\n\n#### 适用边界", sm, re.S)
ZERO = set(re.findall(r"「(\S+?)部」", zm.group(1)))

pat = re.compile(r"<!-- CLAIM:START (clm_[0-9A-F]+) -->\s*\n### (.+?)\n\n(.*?)\n\n#### 适用边界\s*\n\n(.*?)\n\n<!-- CLAIM:END", re.S)
anchors = {}
for f in sorted(glob.glob(os.path.join(ROOT, "knowledge", "hanzi-yinyuan", "*.md"))):
    if "02z" in f:
        continue
    t = open(f, encoding="utf-8").read()
    for m in pat.finditer(t):
        title, body, bd = m.group(2), m.group(3), m.group(4)
        if "声母义" in body:
            continue
        mb = re.search(r"第\s*(\d+)\s*部「(.+?)部」", bd)
        if not mb:
            continue
        no, bu = int(mb.group(1)), mb.group(2)
        if no in anchors or not (bu in BU or bu in ZERO):
            continue
        clean = title.lstrip("「『")
        if clean.startswith(bu):
            anchors[no] = (m.group(1), title, body, bd, bu)


def sent(bu, no):
    if bu in ZERO:
        return (f"声母义：第 {no} 部「{bu}部」读零声母，绪论七组声母未列零声母，"
                f"故本部不系拟态声母义（见「零声母诸部」条）。")
    d = BU[bu]
    pct = f"，部内同部位占 {d['pct']}%" if d["pct"] else ""
    return (f"声母义：第 {no} 部「{bu}部」读 {d['ini']}（{d['grp']}），拟态义「{d['mime']}」"
            f"{pct}，一致度{d['grade']}（见「{bu}部：声母义」条）。")


MINGIT = os.path.join(ROOT, ".runtime", "mingit", "cmd")
ENV = dict(os.environ, PATH=MINGIT + os.pathsep + os.environ.get("PATH", ""),
           PYTHONIOENCODING="utf-8", PYTHONUTF8="1")


def pkc(*args):
    out = subprocess.run(PYC + list(args), capture_output=True, cwd=ROOT, env=ENV)
    txt = out.stdout.decode("utf-8", "replace").lstrip("\ufeff")
    try:
        return json.loads(txt)
    except Exception:
        print("BAD OUTPUT:", txt[:400], out.stderr.decode("utf-8", "replace")[:400])
        raise


if sys.argv[1:] == ["--dry"]:
    print("anchors", len(anchors), "missing", [n for n in range(1, 83) if n not in anchors])
    for no in sorted(anchors)[:3]:
        cid, title, body, bd, bu = anchors[no]
        print("==", title[:22], "|", sent(bu, no))
    sys.exit(0)

plan = pkc("knowledge-plan", "init", "--intent", "补声母义：部首字本义条后附本部声母义与一致度（三版）",
           "--risk", "medium", "--format", "json")
if not plan.get("ok"):
    print("INIT FAIL", json.dumps(plan, ensure_ascii=False)[:400])
    sys.exit(1)
pid = plan.get("plan_id") or plan.get("id")
print("plan", pid)


def revise(cid, stmt, bd):
    for attempt in (1, 2):
        r = pkc("knowledge-plan", "revise-claim", pid, "--claim-id", cid, "--statement", stmt,
                "--boundary", bd, "--semantic-declaration", "clarify",
                "--reason", "补声母义：在部首字本义条后附所属部的声母义与一致度", "--format", "json")
        if r.get("ok"):
            return r
        codes = [e.get("code") for e in r.get("errors", [])]
        if attempt == 1 and "PLAN_STALE_BASELINE" in codes:
            rb = pkc("knowledge-plan", "rebase", pid, "--reason", "并行录入提交后同步基线", "--format", "json")
            print("rebase", rb.get("ok"), rb.get("baseline_commit"))
            continue
        return r
    return r


ok = skipped = 0
for no in sorted(anchors):
    cid, title, body, bd, bu = anchors[no]
    r = revise(cid, body + "\n\n" + sent(bu, no), bd)
    if not r.get("ok"):
        codes = [e.get("code") for e in r.get("errors", [])]
        if set(codes) & {"PLAN_CLAIM_NOT_FOUND", "CLAIM_NOT_FOUND", "KNOWLEDGE_ERROR"}:
            print("SKIP", cid, codes)
            skipped += 1
            continue
        print("FAIL", cid, json.dumps(r, ensure_ascii=False)[:300])
        break
    ok += 1
print("revised", ok, "skipped", skipped)
fin = pkc("knowledge-plan", "finalize", pid, "--format", "json")
print(json.dumps({k: fin.get(k) for k in ("ok", "bundle_id", "content_hash", "operations", "expected_changed_files", "plan_state")},
                 ensure_ascii=False, indent=1))
if not fin.get("ok"):
    print(json.dumps(fin.get("errors"), ensure_ascii=False)[:500])
