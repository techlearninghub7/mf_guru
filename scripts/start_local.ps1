# start_local.ps1
# Run FastAPI with uvicorn in the virtual environment (Windows)

$venv = "$PSScriptRoot\..\venv"
if (Test-Path $venv) {
    Write-Host "Using venv at $venv"
    $python = Join-Path $venv "Scripts\python.exe"
    & $python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
} else {
    Write-Host "No venv found. Create one with: python -m venv venv; .\venv\Scripts\Activate.ps1; pip install -r requirements.txt"
}
