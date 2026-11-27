# 系统汉字 · 网页守护（单次巡检，幂等）
# 计划任务「系统汉字-网页守护」每分钟调用一次：
#   1) 8088 服务不在就重新拉起；
#   2) cloudflared 隧道不在就重新拉起；
#   3) 每轮都以隧道日志里的最新地址为准刷新 web\.cache\当前公网地址.txt；
#   4) 进程在、但公网连续 3 次不通（quick tunnel 会被云端回收）就重启隧道换新地址。
# 重复调用安全：已在跑的不重复起；上一轮没跑完则本轮直接退出。
$ErrorActionPreference = 'SilentlyContinue'

$web = Split-Path -Parent $MyInvocation.MyCommand.Path
$root = Split-Path -Parent $web
$cache = Join-Path $web '.cache'
if (-not (Test-Path $cache)) { New-Item -ItemType Directory -Force -Path $cache | Out-Null }

$logf = Join-Path $cache 'keepalive.log'
$statef = Join-Path $cache 'keepalive-state.json'
$urlf = Join-Path $cache '当前公网地址.txt'
$lockf = Join-Path $cache 'keepalive.lock'

function Log($msg) {
    Add-Content -Path $logf -Value ((Get-Date -Format 'yyyy-MM-dd HH:mm:ss') + ' ' + $msg) -Encoding UTF8
}

# 单实例：上一轮没跑完就直接退出，避免并发重复起进程
$lock = $null
try { $lock = [System.IO.File]::Open($lockf, 'Create', 'Write', 'None') } catch { exit 0 }
try {
    $node = 'C:\Users\萧磊\.dsh\dsh-runtimes\dsh-primary-runtime\dependencies\node\bin\node.exe'
    if (-not (Test-Path $node)) { $node = 'node' }
    $cf = Join-Path $web 'bin\cloudflared.exe'
    $serverErr = Join-Path $cache 'server.err.log'
    $serverOut = Join-Path $cache 'server.log'
    $tunnelErr = Join-Path $cache 'tunnel.err.log'
    $tunnelOut = Join-Path $cache 'tunnel.log'

    function Test-WebPort {
        foreach ($l in (netstat -ano | Select-String ':8088\s')) {
            if ($l.Line -match 'LISTENING') { return $true }
        }
        return $false
    }

    function Start-WebServer {
        Start-Process -FilePath $node -ArgumentList ('"' + (Join-Path $web 'server.mjs') + '"') `
            -WorkingDirectory $root -WindowStyle Hidden `
            -RedirectStandardOutput $serverOut -RedirectStandardError $serverErr
        for ($i = 0; $i -lt 20; $i++) {
            Start-Sleep -Seconds 1
            if (Test-WebPort) { Log '服务已拉起，8088 正在监听'; return $true }
        }
        Log '服务拉起失败，见 web\.cache\server.err.log'
        return $false
    }

    # 隧道日志里最后一个（最新）公网地址
    function Get-LoggedUrl {
        if (-not (Test-Path $tunnelErr)) { return '' }
        $m = Select-String -Path $tunnelErr -Pattern 'https://[a-z0-9-]+\.trycloudflare\.com' -AllMatches |
            ForEach-Object { $_.Matches.Value } | Select-Object -Unique
        if (-not $m) { return '' }
        return @($m)[-1]
    }

    function Save-Url($u) {
        if (-not $u) { return $false }
        $old = ''
        if (Test-Path $urlf) { $old = (Get-Content $urlf -Raw -Encoding UTF8).Trim() }
        Set-Content -Path $urlf -Value $u -Encoding UTF8
        if ($u -ne $old) { Log ('公网地址已更新 ' + $u) }
        return $true
    }

    function Start-Tunnel {
        if (-not (Test-Path $cf)) { Log '找不到 web\bin\cloudflared.exe'; return }
        if (Test-Path $tunnelErr) { Move-Item -Path $tunnelErr -Destination (Join-Path $cache 'tunnel.prev.err.log') -Force }
        Start-Process -FilePath $cf -ArgumentList 'tunnel', '--url', 'http://127.0.0.1:8088', '--no-autoupdate' `
            -WindowStyle Hidden -RedirectStandardOutput $tunnelOut -RedirectStandardError $tunnelErr
        for ($i = 0; $i -lt 45; $i++) {
            Start-Sleep -Seconds 1
            if (Save-Url (Get-LoggedUrl)) { Log '隧道已拉起'; return }
            if (-not (Get-Process cloudflared -ErrorAction SilentlyContinue)) { Log 'cloudflared 启动后立即退出，见 tunnel.err.log'; return }
        }
        Log '隧道拉起后 45 秒内没拿到公网地址'
    }

    function Test-PublicHealth {
        param([string]$Url)
        if (-not $Url) { return $false }
        $target = $Url.TrimEnd('/') + '/api/health'
        & $node -e "fetch(process.argv[1],{signal:AbortSignal.timeout(15000)}).then(r=>process.exit(r.ok?0:1)).catch(()=>process.exit(1))" $target 2>$null | Out-Null
        return ($LASTEXITCODE -eq 0)
    }

    $bad = 0
    if (Test-Path $statef) {
        try { $bad = [int](Get-Content $statef -Raw -Encoding UTF8 | ConvertFrom-Json).publicFail } catch { $bad = 0 }
    }

    $actions = @()

    if (-not (Test-WebPort)) {
        if (Start-WebServer) { $actions += '服务' }
    }

    $tunnelAlive = @(Get-Process cloudflared -ErrorAction SilentlyContinue).Count -gt 0
    if (-not $tunnelAlive) {
        Start-Tunnel
        $bad = 0
        $actions += '隧道'
    } elseif (Test-WebPort) {
        # 进程在但地址文件可能过期：以日志最新地址为准
        $logged = Get-LoggedUrl
        if ($logged) { Save-Url $logged | Out-Null }
        $u = ''
        if (Test-Path $urlf) { $u = (Get-Content $urlf -Raw -Encoding UTF8).Trim() }
        if (Test-PublicHealth $u) {
            $bad = 0
        } else {
            $bad++
            Log ('公网健康检查失败（连续第 ' + $bad + ' 次）address=' + $u)
            if ($bad -ge 3) {
                Log '公网连续不通，重启隧道换地址'
                Stop-Process -Name cloudflared -Force -ErrorAction SilentlyContinue
                Start-Sleep -Seconds 2
                Start-Tunnel
                $bad = 0
                $actions += '隧道(重建)'
            }
        }
    }

    if ($actions.Count -gt 0) { Log ('本轮处理：' + ($actions -join '、')) }
    @{ publicFail = $bad; checkedAt = (Get-Date -Format 'yyyy-MM-dd HH:mm:ss') } |
        ConvertTo-Json | Set-Content -Path $statef -Encoding UTF8
}
finally {
    if ($lock) { $lock.Close() }
}
