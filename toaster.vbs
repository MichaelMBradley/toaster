Set oShell = CreateObject ("Wscript.Shell") 
Dim strArgs
strArgs = ".venv\Scripts\python.exe toaster.py"
Set args = WScript.Arguments
for i = 0 to args.Count - 1
    strArgs = strArgs & " " & args(i)
Next
oShell.Run strArgs, 0, false
