@echo off
for /f "tokens=5" %%a in ('netstat -ano ^| findstr ":8088" ^| findstr "LISTENING"') do taskkill /f /pid %%a >nul 2>&1
taskkill /f /im cloudflared.exe >nul 2>&1
echo Stopped: server on 8099 and tunnel are closed.
pause