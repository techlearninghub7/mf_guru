# PowerShell script to create mf-guru project structure

# Define the root directory
$rootDir = "mf-guru"

# Create root directory
New-Item -ItemType Directory -Path $rootDir -Force

# Create root-level files
$rootFiles = @(
    "README.md",
    "requirements.txt",
    ".env.example",
    "run_local.bat",
    "vercel.json",
    "Dockerfile"
)
foreach ($file in $rootFiles) {
    New-Item -ItemType File -Path "$rootDir\$file" -Force
}

# Create src directory and files
New-Item -ItemType Directory -Path "$rootDir\src" -Force
$srcFiles = @(
    "__init__.py",
    "main.py",
    "config.py",
    "db.py",
    "models.py",
    "schemas.py",
    "api.py",
    "amfi_fetcher.py"
)
foreach ($file in $srcFiles) {
    New-Item -ItemType File -Path "$rootDir\src\$file" -Force
}

# Create src/migrations directory and file
New-Item -ItemType Directory -Path "$rootDir\src\migrations" -Force
New-Item -ItemType File -Path "$rootDir\src\migrations\init_db.py" -Force

# Create tests directory and file
New-Item -ItemType Directory -Path "$rootDir\tests" -Force
New-Item -ItemType File -Path "$rootDir\tests\test_health.py" -Force

Write-Host "Project structure for mf-guru created successfully!"