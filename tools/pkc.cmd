@echo off
setlocal
chcp 65001 >nul
set "PATH=%~dp0..\.runtime\mingit\cmd;%PATH%"
rem Run pkc through pkc_tmpfix.py instead of pkc.exe: under the restricted
rem (low integrity) sandbox, tempfile's 0o700 temp dirs are inaccessible and
rem pkc's temporary project overlay fails. See the header of pkc_tmpfix.py.
"%~dp0..\.runtime\venv\Scripts\python.exe" "%~dp0pkc_tmpfix.py" %*
