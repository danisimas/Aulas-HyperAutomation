$exclude = @("venv", "bot_funcionário.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "bot_funcionário.zip" -Force