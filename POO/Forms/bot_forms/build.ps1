$exclude = @("venv", "bot_forms.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "bot_forms.zip" -Force