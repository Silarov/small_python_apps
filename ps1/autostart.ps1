[void] [System.Reflection.Assembly]::LoadWithPartialName("System.Drawing") 
[void] [System.Reflection.Assembly]::LoadWithPartialName("System.Windows.Forms") 
$signature=@'
[DllImport("user32.dll",CharSet=CharSet.Auto,CallingConvention=CallingConvention.StdCall)]
public static extern void mouse_event(long dwFlags, long dx, long dy, long cButtons, long dwExtraInfo);
'@
$SendMouseClick = Add-Type -memberDefinition $signature -name "Win32MouseEventNew" -namespace Win32Functions -passThru

$remoteDesktop = "C:\WINDOWS\system32\mstsc.exe"
$brave = "C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
$notion = "C:\Users\probst_s\AppData\Local\Programs\Notion\Notion.exe"
$spotify = "C:\Users\probst_s\AppData\Roaming\Spotify\Spotify.exe"
$outlook = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Outlook 2016"
$wshell = New-Object -ComObject wscript.shell;
$pw = 'M@$C3tN5'

#startet Remote Desktop + Anmeldung
Start-Process $remoteDesktop
$x = 1037
$y = 456
[System.Windows.Forms.Cursor]::Position = New-Object System.Drawing.Point($x, $y)
Start-Sleep -seconds 1
$SendMouseClick::mouse_event(0x00000002, 0, 0, 0, 0);
$SendMouseClick::mouse_event(0x00000004, 0, 0, 0, 0);
Start-Sleep -Seconds 1
$wshell.SendKeys($pw)
$wshell.SendKeys('~')

# #startet Brave
Start-Process $brave
Start-Sleep -Seconds 1

#startet outlook
Start-Process $outlook
Start-Sleep -seconds 1

#startet spotify + spielt favorite songs
Start-Process $spotify
Start-Sleep -Seconds 8
$x = 368
$y = 302
[System.Windows.Forms.Cursor]::Position = New-Object System.Drawing.Point($x, $y)
Start-Sleep -milliseconds 50
$SendMouseClick::mouse_event(0x00000002, 0, 0, 0, 0);
$SendMouseClick::mouse_event(0x00000004, 0, 0, 0, 0);
Start-Sleep -Seconds 1
$x = 571
$y = 445
[System.Windows.Forms.Cursor]::Position = New-Object System.Drawing.Point($x, $y)
Start-Sleep -milliseconds 50
$SendMouseClick::mouse_event(0x00000002, 0, 0, 0, 0);
$SendMouseClick::mouse_event(0x00000004, 0, 0, 0, 0);

# #startet notion
Start-Process $notion
Start-Sleep -Seconds 1