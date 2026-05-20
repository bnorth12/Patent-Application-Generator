param(
    [string]$BaseBranch = "main"
)

$ErrorActionPreference = "Stop"

function Fail([string]$Message) {
    Write-Host "[FAIL] $Message" -ForegroundColor Red
    exit 1
}

function Pass([string]$Message) {
    Write-Host "[PASS] $Message" -ForegroundColor Green
}

$currentBranch = (git rev-parse --abbrev-ref HEAD).Trim()
if (-not $currentBranch) {
    Fail "Unable to determine current branch."
}

if ($currentBranch -eq $BaseBranch) {
    Fail "Direct pushes from '$BaseBranch' are blocked by local pre-push policy. Use a feature branch and pull request."
}

& "$PSScriptRoot/pre-merge-gate.ps1" -BaseBranch $BaseBranch
if ($LASTEXITCODE -ne 0) {
    Fail "Pre-merge gate failed during pre-push checks."
}

Pass "Pre-push governance gate completed successfully."
