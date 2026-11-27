' 系统汉字 · 网页守护启动器（无窗口）
' 计划任务「系统汉字-网页守护」每分钟调用本文件；用 wscript 以窗口样式 0 启动 PowerShell，
' 避免每次巡检弹出黑色控制台窗口（2026-11-27 主人要求：不要再弹 C:/Windows 窗口）。
' 传参、日志、幂等逻辑全部仍在 web\keepalive.ps1 里，本文件只负责“悄悄启动”。
Option Explicit
Dim fso, sh, here, script, cmd
Set fso = CreateObject("Scripting.FileSystemObject")
Set sh = CreateObject("WScript.Shell")
here = fso.GetParentFolderName(WScript.ScriptFullName)
script = fso.BuildPath(here, "keepalive.ps1")
cmd = "powershell.exe -NoProfile -NonInteractive -ExecutionPolicy Bypass -WindowStyle Hidden -File """ & script & """"
sh.Run cmd, 0, False
