@echo off
setlocal
chcp 65001 >nul
set "PATH=%~dp0..\..\.tools\mingit\cmd;%PATH%"
"%~dp0..\..\portable-knowledge\.venv\Scripts\pkc.exe" %*
