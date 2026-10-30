$ErrorActionPreference = 'Continue'
$web = Split-Path -Parent $MyInvocation.MyCommand.Path
$root = Split-Path -Parent $web
$cache = Join-Path $web '.cache'
New-Item -ItemType Directory -Force -Path $cache | Out-Null

$node = 'C:\Users\萧磊\.dsh\dsh-runtimes\dsh-primary-runtime\dependencies\node\bin\node.exe'
if (-not (Test-Path $node)) { $node = 'node' }

Write-Host '============================================'
Write-Host '    系统汉字 · 启动服务'
Write-Host '============================================'
Write-Host ''

Write-Host '[1/3] 启动问答服务，端口 8088 ...'
Start-Process -FilePath $node -ArgumentList "`"$web\server.mjs`"" -WorkingDirectory $root -WindowStyle Hidden -RedirectStandardOutput "$cache\server.log" -RedirectStandardError "$cache\server.err.log"
Start-Sleep -Seconds 4
try {
    $h = Invoke-WebRequest -Uri 'http://127.0.0.1:8088/api/health' -UseBasicParsing -TimeoutSec 6
    Write-Host "      服务已启动：$($h.Content)"
} catch {
    Write-Host '      服务还没起来，稍后看 .cache\server.err.log'
}

Write-Host '[2/3] 启动公网隧道，要等 5-10 秒 ...'
Start-Process -FilePath "$web\bin\cloudflared.exe" -ArgumentList 'tunnel', '--url', 'http://127.0.0.1:8088', '--no-autoupdate' -WindowStyle Hidden -RedirectStandardOutput "$cache\tunnel.log" -RedirectStandardError "$cache\tunnel.err.log"
Start-Sleep -Seconds 10

Write-Host '[3/3] 对外地址，发给客户的就是下面这个：'
Write-Host ''
$url = Select-String -Path "$cache\tunnel.err.log" -Pattern 'https://[a-z0-9-]+\.trycloudflare\.com' -AllMatches |
    ForEach-Object { $_.Matches.Value } | Select-Object -Unique -First 1
if ($url) { Write-Host "      $url" } else { Write-Host '      没拿到地址，看 .cache\tunnel.err.log' }
Write-Host ''
Write-Host '    本机打开：http://127.0.0.1:8088'
Write-Host '    后台管理：http://127.0.0.1:8088/admin'
Write-Host ''
Write-Host '    服务和隧道在后台跑，这个窗口关掉也不影响。'
Write-Host '    要停止服务，双击 web\stop.cmd。'
Write-Host '    电脑重启后，再双击 web\start.cmd，会拿到一个新地址。'
Write-Host ''

Start-Process 'http://127.0.0.1:8088'
Read-Host '按回车键关闭这个窗口'
