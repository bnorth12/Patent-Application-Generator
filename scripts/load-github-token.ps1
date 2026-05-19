param(
    [string]$TokenFile = ".local-secrets/github-token.env"
)

if (-not (Test-Path -Path $TokenFile)) {
    Write-Error "Token file not found: $TokenFile"
    exit 1
}

$line = Get-Content -Path $TokenFile |
    Where-Object { $_ -match '^\s*GITHUB_TOKEN\s*=' } |
    Select-Object -First 1

if (-not $line) {
    Write-Error "GITHUB_TOKEN entry not found in $TokenFile"
    exit 1
}

$token = ($line -split '=', 2)[1].Trim()
if ([string]::IsNullOrWhiteSpace($token)) {
    Write-Error "GITHUB_TOKEN is empty in $TokenFile"
    exit 1
}

$env:GITHUB_TOKEN = $token
Write-Host "GITHUB_TOKEN loaded into current PowerShell session."
