$ErrorActionPreference = "Stop"

$repoRoot = (Resolve-Path "$PSScriptRoot/..").Path
Set-Location $repoRoot

git rev-parse --is-inside-work-tree *> $null
if ($LASTEXITCODE -ne 0) {
    Write-Error "Current directory is not a git repository: $repoRoot"
    exit 1
}

git config core.hooksPath .githooks
if ($LASTEXITCODE -ne 0) {
    Write-Error "Failed to set core.hooksPath to .githooks"
    exit 1
}

Write-Host "Git hooks installed. core.hooksPath=.githooks" -ForegroundColor Green
