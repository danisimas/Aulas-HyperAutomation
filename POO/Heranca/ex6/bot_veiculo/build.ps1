$exclude = @("venv", "bot_veiculo.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "bot_veiculo.zip" -Force