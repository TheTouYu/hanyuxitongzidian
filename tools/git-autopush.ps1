<#
  系统汉字 · 每日自动推送
  ------------------------------------------------------------------
  只推送「已经提交」的 main 分支；绝不提交、绝不改动工作区。
  由 Windows 计划任务「系统汉字-每日自动推送」调用。
  日志 / 状态：%LOCALAPPDATA%\system-hanzi\
#>

$ErrorActionPreference = 'Continue'

$repo     = Split-Path -Parent $PSScriptRoot          # tools\ 的上一级
$git      = Join-Path $repo 'tools\git.cmd'
$stateDir = Join-Path $env:LOCALAPPDATA 'system-hanzi'
$logFile  = Join-Path $stateDir 'git-autopush.log'
$statusFile = Join-Path $stateDir 'git-autopush-status.txt'

if (-not (Test-Path $stateDir)) { New-Item -ItemType Directory -Path $stateDir -Force | Out-Null }

function Write-Log {
    param([string]$Message)
    $line = '{0}  {1}' -f (Get-Date -Format 'yyyy-MM-dd HH:mm:ss'), $Message
    Add-Content -LiteralPath $logFile -Value $line -Encoding UTF8
}

function Write-Status {
    param([string]$Result, [string]$Detail)
    $text = @(
        "最后运行: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')",
        "结果: $Result",
        $Detail
    ) -join "`r`n"
    Set-Content -LiteralPath $statusFile -Value $text -Encoding UTF8
}

# 日志超过 512 KB 截断，只保留最后 400 行
if ((Test-Path $logFile) -and ((Get-Item -LiteralPath $logFile).Length -gt 512KB)) {
    $tail = Get-Content -LiteralPath $logFile -Tail 400
    Set-Content -LiteralPath $logFile -Value $tail -Encoding UTF8
}

$env:GIT_TERMINAL_PROMPT = '0'
$exitCode = 0

Push-Location $repo
try {
    $branch = (& $git symbolic-ref --short HEAD 2>$null | Out-String).Trim()
    if (-not $branch) { $branch = '(detached)' }
    Write-Log "开始：分支 $branch"

    if ($branch -ne 'main') {
        Write-Log "当前分支不是 main，跳过"
        Write-Status '跳过' "分支: $branch（不是 main）"
    }
    else {
        # 远端跟踪分支是否可用
        & $git rev-parse --verify --quiet origin/main 2>$null | Out-Null
        $hasRemoteRef = ($LASTEXITCODE -eq 0)

        $ahead = 0
        if ($hasRemoteRef) {
            $ahead = [int](((& $git rev-list --count 'origin/main..HEAD') -join '')).Trim()
        }
        else {
            $ahead = [int](((& $git rev-list --count 'HEAD') -join '')).Trim()
        }

        # 没有待推提交：不联网，直接结束（登录触发时几乎零开销）
        if ($hasRemoteRef -and $ahead -eq 0) {
            Write-Log '没有待推送的提交，跳过'
            Write-Status '无事可做' '本地与远端一致'
            $exitCode = 0
        }
        else {
            # 有东西要推：先对齐远端，判断是否被抢先
            & $git fetch --quiet origin 2>&1 | Out-Null
            if ($LASTEXITCODE -ne 0) {
                Write-Log 'fetch 失败（网络或认证问题）'
                Write-Status '失败' 'git fetch 失败，详见日志'
                $exitCode = 1
            }
            else {
                $ahead  = [int](((& $git rev-list --count 'origin/main..HEAD') -join '')).Trim()
                $behind = [int](((& $git rev-list --count 'HEAD..origin/main') -join '')).Trim()
                Write-Log "ahead=$ahead behind=$behind"

                if ($behind -gt 0) {
                    Write-Log '远端有本地没有的提交，需先合并，本次不推'
                    Write-Status '跳过' "远端领先 $behind 个提交，需人工处理"
                    $exitCode = 2
                }
                elseif ($ahead -eq 0) {
                    Write-Log 'fetch 后确认没有待推送的提交'
                    Write-Status '无事可做' '本地与远端一致'
                }
                else {
                    $pushed = $false
                    for ($i = 1; $i -le 3; $i++) {
                        $out = (& $git push origin main 2>&1 | Out-String).Trim()
                        $code = $LASTEXITCODE
                        if ($code -eq 0) { $pushed = $true; break }
                        Write-Log "第 $i 次推送失败（exit $code）：$out"
                        if ($i -lt 3) { Start-Sleep -Seconds 20 }
                    }
                    if ($pushed) {
                        $head = (& $git rev-parse --short HEAD | Out-String).Trim()
                        Write-Log "推送成功：$ahead 个提交，HEAD=$head"
                        Write-Status '成功' "推送 $ahead 个提交，HEAD=$head"
                    }
                    else {
                        Write-Log '三次推送均失败'
                        Write-Status '失败' "$ahead 个提交未能推送，详见日志"
                        $exitCode = 1
                    }
                }
            }
        }
    }
}
catch {
    Write-Log "异常：$($_.Exception.Message)"
    Write-Status '失败' $_.Exception.Message
    $exitCode = 1
}
finally {
    Pop-Location
}

exit $exitCode
