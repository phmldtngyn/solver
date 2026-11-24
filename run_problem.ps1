param(
    [Parameter(Mandatory=$true)]
    [ValidateSet(1,2,3,4)]
    [int]$Problem,

    [string]$Goal = "",
    [string[]]$ExtraTex = @()
)

# Nếu chạy kèm model local (Ollama/llama.cpp), ép giới hạn 4 luồng CPU
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

Write-Host "Khởi chạy pipeline 7 Agent cho Bài toán $Problem..." -ForegroundColor Cyan
python @pyArgs
