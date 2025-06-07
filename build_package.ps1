# PowerShell script to compile purviewcli as a single CLI executable named pv.exe

$entryFile = "purviewcli\__main__.py"
$outputName = "pv"

# 🧹 Clean old builds
Write-Host "🧹 Cleaning previous builds..."
Remove-Item -Recurse -Force "build", "dist", "$outputName.spec" -ErrorAction SilentlyContinue

# 🚀 Build executable
Write-Host "🚀 Building executable..."
pyinstaller `
    --name $outputName `
    --onefile `
    --console `
    $entryFile

# ✅ Move output to root
Move-Item -Path ".\dist\$outputName.exe" -Destination ".\$outputName.exe" -Force

Write-Host "✅ Done! Run it with: .\$outputName.exe"
