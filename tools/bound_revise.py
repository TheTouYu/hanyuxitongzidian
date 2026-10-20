"""驱动 pkc knowledge-plan revise-claim，把 539 条 Claim 的 boundary 统一改写。

用法：
  python intake\_tmp_bound_revise.py <plan_id> [--limit N] [--start N]

数据源：intake\_tmp_bound_map.json（由 intake\_tmp_bound_map.py 生成）
"""
import io, json, os, subprocess, sys, time

ROOT = r'D:\系统汉字'
PY = ROOT + r'\.runtime\venv\Scripts\python.exe'
TMPFIX = ROOT + r'\tools\pkc_tmpfix.py'
REASON = '统一 boundary 写法：只注明出处部次，不再声明是否为学界共识'

env = dict(os.environ)
env['PYTHONUTF8'] = '1'
env['PYTHONIOENCODING'] = 'utf-8'
env['PATH'] = ROOT + r'\.runtime\mingit\cmd;' + env.get('PATH', '')

rows = json.load(io.open(ROOT + r'\intake\_tmp_bound_map.json', encoding='utf-8'))
rows.sort(key=lambda r: (r['file'], r['idx']))

plan_id = sys.argv[1]
limit = None
start = 0
for i, a in enumerate(sys.argv):
    if a == '--limit':
        limit = int(sys.argv[i + 1])
    if a == '--start':
        start = int(sys.argv[i + 1])

log = io.open(ROOT + r'\intake\_tmp_bound_revise.log', 'w', encoding='utf-8')
todo = rows[start:start + limit] if limit else rows[start:]
t0 = time.time()
for n, r in enumerate(todo, 1):
    cmd = [PY, TMPFIX, 'knowledge-plan', 'revise-claim', plan_id,
           '--claim-id', r['id'],
           '--statement', r['statement'],
           '--boundary', r['new_boundary'],
           '--semantic-declaration', 'clarify',
           '--reason', REASON,
           '--format', 'json']
    p = subprocess.run(cmd, env=env, capture_output=True, cwd=ROOT)
    out = p.stdout.decode('utf-8', 'replace')
    err = p.stderr.decode('utf-8', 'replace')
    ok = False
    try:
        ok = p.returncode == 0 and json.loads(out).get('ok') is True
    except Exception:
        ok = False
    log.write('%d %s %s rc=%s\n' % (n, r['id'], 'OK' if ok else 'FAIL', p.returncode))
    if not ok:
        log.write('CMD_STDOUT: %s\nCMD_STDERR: %s\n' % (out[:2000], err[:2000]))
        log.flush()
        print('FAIL at %d %s' % (n, r['id']), file=sys.stderr)
        print(out[:800], err[:800], file=sys.stderr)
        break
    if n % 20 == 0:
        el = time.time() - t0
        log.flush()
        print('%d/%d %.1fs (%.2fs/条)' % (n, len(todo), el, el / n), file=sys.stderr)
log.write('DONE %d 条，用时 %.1fs\n' % (n, time.time() - t0))
log.close()
print('plan', plan_id, 'done', n)
