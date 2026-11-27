' 通用无窗口启动器（系统汉字）
' 用法：wscript.exe //B //NoLogo "D:\系统汉字\tools\run-hidden.vbs" "D:\系统汉字\web\keepalive.ps1"
' 作用：以窗口样式 0 调起 PowerShell 跑指定脚本，不弹控制台窗口。
' 为什么不直接在计划任务里跑 powershell.exe：-WindowStyle Hidden 对控制台程序无效，
' 任务计划用 InteractiveToken 启动时照样闪出 C:\WINDOWS\System32\WindowsPowerShell\... 窗口并抢焦点
' （2026-11-27 主人要求：不要再弹这个窗口）。
Option Explicit
Dim fso, sh, target, cmd
If WScript.Arguments.Count = 0 Then WScript.Quit 2
target = WScript.Arguments(0)
Set fso = CreateObject("Scripting.FileSystemObject")
If Not fso.FileExists(target) Then WScript.Quit 3
Set sh = CreateObject("WScript.Shell")
cmd = "powershell.exe -NoProfile -NonInteractive -ExecutionPolicy Bypass -WindowStyle Hidden -File """ & target & """"
sh.Run cmd, 0, False
