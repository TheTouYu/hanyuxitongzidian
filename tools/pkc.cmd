@echo off
setlocal
chcp 65001 >nul
set "PATH=%~dp0..\.runtime\mingit\cmd;%PATH%"
"%~dp0..\.runtime\venv\Scripts\pkc.exe" %*
