param(
    [string]$BaseBranch = "main",
    [switch]$AllowDirty
)

$ErrorActionPreference = "Stop"

function Fail([string]$Message) {
    Write-Host "[FAIL] $Message" -ForegroundColor Red
    exit 1
}

function Pass([string]$Message) {
    Write-Host "[PASS] $Message" -ForegroundColor Green
}

git rev-parse --is-inside-work-tree *> $null
if ($LASTEXITCODE -ne 0) {
    Fail "Current directory is not a git repository."
}

$currentBranch = (git rev-parse --abbrev-ref HEAD).Trim()
if ($currentBranch -eq $BaseBranch) {
    Fail "Run this gate from a feature branch, not from '$BaseBranch'."
}

if (-not $AllowDirty) {
    $status = git status --porcelain
    if ($status) {
        Fail "Working tree is dirty. Commit or stash changes before running pre-merge gate."
    }
}

git fetch origin $BaseBranch --quiet
if ($LASTEXITCODE -ne 0) {
    Fail "Failed to fetch origin/$BaseBranch."
}

$mergeBase = (git merge-base HEAD origin/$BaseBranch).Trim()
if (-not $mergeBase) {
    Fail "Unable to determine merge base with origin/$BaseBranch."
}

$mergeTree = git merge-tree $mergeBase HEAD origin/$BaseBranch
if ($mergeTree -match "<<<<<<<|=======|>>>>>>>") {
    Fail "Potential merge conflict detected against origin/$BaseBranch."
}
Pass "No merge conflict markers detected in merge simulation."

$diffCheck = git diff --check origin/$BaseBranch...HEAD
if ($diffCheck) {
    Fail "Whitespace or conflict-marker issues detected in changed content.\n$diffCheck"
}
Pass "Diff quality checks passed."

$changedFiles = git diff --name-only origin/$BaseBranch...HEAD
if ($changedFiles) {
    $markers = Select-String -Path $changedFiles -Pattern "^(<<<<<<<|=======|>>>>>>>)" -ErrorAction SilentlyContinue
    if ($markers) {
        Fail "Conflict markers detected in changed files."
    }
}
Pass "No conflict markers found in changed files."

Write-Host "Pre-merge gate completed successfully." -ForegroundColor Cyan
exit 0
