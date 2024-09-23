Set WshShell = CreateObject("WScript.Shell")
WshShell.Run "cmd.exe /c cd /d YOURPATH && venv\Scripts\activate && python main.py", 0
Set WshShell = Nothing
