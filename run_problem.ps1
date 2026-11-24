param(
    [Parameter(Mandatory=$true)]
    [ValidateSet(1,2,3,4)]
    [int]$Problem,

    [string]$Goal = "",
    [string[]]$ExtraTex = @(),
    [switch]$DryRun
)

# Ép giới hạn 4 luồng CPU nếu dùng kèm model local
$env:OLLAMA_NUM_THREAD = "4"
$env:OMP_NUM_THREADS = "4"

$pyArgs = @("orchestrator.py", "--problem", $Problem)
if ($Goal -ne "") {
    $pyArgs += @("--goal", $Goal)
}
if ($ExtraTex.Count -gt 0) {
    $pyArgs += "--extra-tex"
    $pyArgs += $ExtraTex
}
if ($DryRun) {
    $pyArgs += "--dry-run"
}

Write-Host "Khởi chạy pipeline 7 Agent cho Bài toán $Problem..." -ForegroundColor Cyan
python @pyArgs