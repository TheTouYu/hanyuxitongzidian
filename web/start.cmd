@echo off
chcp 65001 >nul
setlocal
cd /d "%~dp0.."

set "NODE=C:\Users\萧磊\.dsh\dsh-runtimes\dsh-primary-runtime\dependencies\node\bin\node.exe"
if not exist "%NODE%" set "NODE=node"

echo [1/2] 启动问答服务 ...  http://127.0.0.1:8080
start "系统汉字-服务" /min "%NODE%" "%~dp0server.mjs"

timeout /t 3 /nobreak >nul

echo [2/2] 启动公网隧道 ...
echo       （下面出现 https://xxx.trycloudflare.com 就是对外地址，Ctrl+C 停止）
"%~dp0bin\cloudflared.exe" tunnel --url http://127.0.0.1:8080 --no-autoupdate

endlocal
