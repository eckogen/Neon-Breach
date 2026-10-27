$ErrorActionPreference = 'Stop'
Set-Location -LiteralPath (Split-Path -Parent $PSScriptRoot)
$gitCommand = Get-Command git -ErrorAction SilentlyContinue
$taskGit = if ($gitCommand) { $gitCommand.Source } else { Join-Path $env:USERPROFILE '.cache\codex-runtimes\codex-primary-runtime\dependencies\native\git\cmd\git.exe' }
if (!(Test-Path -LiteralPath $taskGit)) { throw 'Git was not found. Install Git for Windows, then run this script again.' }
function Invoke-TaskGit {
    & $taskGit @args
    if ($LASTEXITCODE -ne 0) { throw 'Git command failed. No force push was attempted.' }
}
if (!(Test-Path -LiteralPath '.git')) { Invoke-TaskGit init -b main }
Invoke-TaskGit config user.name 'eckogen'
Invoke-TaskGit config user.email 'donnovanroe@gmail.com'
$existingRemote = & $taskGit remote get-url origin 2>$null
if ($LASTEXITCODE -ne 0) {
    Invoke-TaskGit remote add origin 'https://github.com/eckogen/Neon-Breach.git'
} elseif ($existingRemote -ne 'https://github.com/eckogen/Neon-Breach.git') {
    throw "Origin already points to $existingRemote. Review it before continuing."
}
Invoke-TaskGit add .gitignore outputs/index.html outputs/README.md outputs/assets work/check.cjs
& $taskGit diff --cached --quiet
if ($LASTEXITCODE -eq 1) { Invoke-TaskGit commit -m 'Add Neon Breach FPS and level editor' }
elseif ($LASTEXITCODE -ne 0) { throw 'Could not inspect staged changes.' }
$branch = & $taskGit branch --show-current
Invoke-TaskGit push -u origin "${branch}:main"
Write-Host 'Neon Breach pushed to https://github.com/eckogen/Neon-Breach' -ForegroundColor Green
