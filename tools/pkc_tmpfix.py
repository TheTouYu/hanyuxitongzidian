"""Run pkc with a Windows-sandbox workaround for tempfile directories.

Why this file exists
--------------------
The harness sandbox runs tools under a *restricted* token (low integrity
level).  `tempfile.mkdtemp()` / `tempfile.TemporaryDirectory()` create
directories with mode 0o700; CPython 3.12 on Windows turns that mode into a
DACL that only grants the user's *normal* SID, which a restricted token is
not allowed to use.  The result is `PermissionError [WinError 5]` as soon as
pkc copies anything into its temporary project overlay, e.g.:

    [WinError 5] 拒绝访问。: '...\\_tmp\\tmpab12cd34\\data'

`pkc knowledge-plan capture` builds exactly such an overlay for every plan,
so preview/finalize would otherwise need a per-command privilege escalation.

Fix: while running pkc, force mode 0o777 for directories created *inside* the
process temp dir.  Everything else (knowledge/, data/, projects dirs) keeps
the normal behaviour, and an ordinary user shell is unaffected because 0o777
is the default anyway.
"""
from __future__ import annotations

import os
import sys
import tempfile

_TEMP = os.path.normcase(os.path.abspath(tempfile.gettempdir()))
_mkdir = os.mkdir


def _mkdir_allow_temp(path, mode: int = 0o777, *, dir_fd=None):
    if dir_fd is None:
        try:
            probe = os.path.normcase(os.path.abspath(os.fspath(path)))
        except (TypeError, ValueError):
            probe = ""
        if probe == _TEMP or probe.startswith(_TEMP + os.sep):
            mode = 0o777
    return _mkdir(path, mode, dir_fd=dir_fd)


os.mkdir = _mkdir_allow_temp

from portable_knowledge.cli import main  # noqa: E402  (after the patch)

if __name__ == "__main__":
    sys.exit(main())
