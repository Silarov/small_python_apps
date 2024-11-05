#erstellt den Ordner "Probe2", um alles darin abzuspeichern
$Folder = 'C:\work\Probe2'
if (-not(Test-Path -Path $Folder)) {
    New-Item -Path $Folder -ItemType Directory
}
$Location = $Folder + "\duplikate.txt"
Start-Transcript -Append $Folder\log.txt -NoClobber 

#Pfad von Duplikatsuche
$filepath = Read-Host 'Dateipfad fuer die Suche nach Duplikaten eingeben (z. B. c:\temp)'
 
If (Test-Path $filepath) {
Write-Warning 'Suche nach Duplikaten ... Bitte warten ...'
 
$duplicates = Get-ChildItem $filepath -File -Recurse `
-ErrorAction SilentlyContinue |
Get-FileHash |
Group-Object -Property Hash |
Where-Object Count -GT 1
 
#schaut, ob es keine Duplikate gibt
If ($duplicates.count -lt 1)
 
{
Write-Warning 'Keine Duplikate gefunden.'
Break ''
}
 
else {
Write-Warning "Duplikate gefunden."
$date = Get-Date -Format "MM-dd-yyyy HH:mm:ss"
$distance = "-------------------------------------------------------------------"

#schreibt alle Duplikate in "Duplikate.txt"
$result = foreach ($d in $duplicates)
{
    $date | Out-File -Append $Location
    $d.Group | Select-Object -Property Path, Hash | Out-File -Append $Location
    $distance | Out-File -Append $Location
}
}

Start-Process $Location

}
else
{
Write-Warning `
"Den Ordner, den Sie ausgewaehlt haben, gibt es nicht. Probieren Sie es nochmals (Bsp: c:\temp)"
}
[void][System.Console]::ReadKey($true)