#!/usr/bin/env python3
"""pkc-bridge.py — 安全、强制 UTF-8 地调用 PKC，供 web/server.mjs 使用。

为什么需要它：
1. PKC 在 Windows 重定向输出时按本地码页（GBK）编码，中文会乱；这里强制 UTF-8。
2. 直接 spawn pkc.exe 会因 PATH 缺 mingit 报 [WinError 2]；这里补 PATH。
3. Node 侧用参数数组调用本脚本（不开 shell），用户问题不会被当成命令行解释。

用法：
  python pkc-bridge.py query "<问题>" [limit]
  python pkc-bridge.py show  <clm_id>
  python pkc-bridge.py tree
"""

import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PKC = os.path.join(ROOT, ".runtime", "venv", "Scripts", "pkc.exe")
MINGIT = os.path.join(ROOT, ".runtime", "mingit", "cmd")


def child_env():
    env = dict(os.environ)
    env["PATH"] = MINGIT + os.pathsep + env.get("PATH", "")
    env["PYTHONIOENCODING"] = "utf-8"
    env["PYTHONUTF8"] = "1"
    return env


def emit(text):
    """按 UTF-8 字节直接写 stdout，绕开控制台码页（否则中文会再被编成 GBK）。"""
    sys.stdout.buffer.write(text.encode("utf-8"))
    sys.stdout.buffer.flush()


def fail(code, message, exit_code=1):
    emit(
        json.dumps(
            {"ok": False, "command": "bridge", "errors": [{"code": code, "message": message}]},
            ensure_ascii=False,
        )
    )
    return exit_code


def run_pkc(args):
    try:
        proc = subprocess.run(
            [PKC, *args],
            cwd=ROOT,
            env=child_env(),
            capture_output=True,
            timeout=120,
        )
    except FileNotFoundError:
        return fail("PKC_NOT_FOUND", "找不到 " + PKC)
    except subprocess.TimeoutExpired:
        return fail("PKC_TIMEOUT", "pkc 超过 120 秒未返回")

    out = proc.stdout.decode("utf-8", "replace")
    err = proc.stderr.decode("utf-8", "replace")
    if not out.strip():
        return fail("PKC_EMPTY_OUTPUT", (err or "pkc 没有输出")[-800:], proc.returncode or 1)
    emit(out)
    return 0 if proc.returncode == 0 else proc.returncode


def run_tree():
    """tree 是纯文本，包成 JSON 统一给 Node 解析。"""
    try:
        proc = subprocess.run(
            [PKC, "tree", "--format", "text"],
            cwd=ROOT,
            env=child_env(),
            capture_output=True,
            timeout=120,
        )
    except FileNotFoundError:
        return fail("PKC_NOT_FOUND", "找不到 " + PKC)
    except subprocess.TimeoutExpired:
        return fail("PKC_TIMEOUT", "pkc 超过 120 秒未返回")
    text = proc.stdout.decode("utf-8", "replace")
    if not text.strip():
        return fail("PKC_EMPTY_OUTPUT", proc.stderr.decode("utf-8", "replace")[-800:])
    emit(json.dumps({"ok": True, "command": "tree", "text": text}, ensure_ascii=False))
    return 0


def main():
    if len(sys.argv) < 2:
        return fail("USAGE", "用法: pkc-bridge.py query|show|tree ...", 2)

    cmd = sys.argv[1]

    if cmd == "query":
        if len(sys.argv) < 3 or not sys.argv[2].strip():
            return fail("USAGE", "缺少问题文本", 2)
        limit = sys.argv[3] if len(sys.argv) > 3 else "5"
        if not limit.isdigit():
            limit = "5"
        return run_pkc(
            ["query", sys.argv[2], "--format", "json", "--level", "2",
             "--permission", "public", "--limit", limit]
        )

    if cmd == "show":
        if len(sys.argv) < 3:
            return fail("USAGE", "缺少 claim_id", 2)
        return run_pkc(
            ["show-claim", sys.argv[2], "--format", "json", "--permission", "public"]
        )

    if cmd == "tree":
        return run_tree()

    return fail("UNKNOWN_COMMAND", "未知命令: " + cmd, 2)


if __name__ == "__main__":
    sys.exit(main())
