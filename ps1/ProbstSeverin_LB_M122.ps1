<#

    Version:    1.0
    Author:     Severin Julian Probst
    Date:       07/01/2022 11:22
    Module:     122

#>

# Set-ExecutionPolicy RemoteSigned -Force -Scope CurrentUser


#create folder with config and log file
$Folder = 'C:\work\ProbstSeverin_LB_M122'
if (-not(Test-Path -Path $Folder)) {
    New-Item -Path $Folder -ItemType Directory
}
Start-Transcript -Append $Folder\log.txt -NoClobber 
$config = $Folder + "\config.txt"
if (-not(Test-Path -Path $config)) {
    New-Item -Path $config -ItemType File

    $again = $true
    
    while($again) {
        
        #path of start folder
        $startpath = Read-Host "Path of folder you want to backup (Bsp: c:/temp) "

        if(Test-Path -Path $startpath) {
            $startpath | Out-File -Append $config
            $again = $false
        } else {
            Write-Warning "Please enter a valid path "
        }
    }

    $destpath = Read-Host "Path of Folder from Destination (Bsp: c:/work) "
    $destpath | Out-File -Append $config
    if (-not(Test-Path -Path $destpath)) {
        New-Item -Path $destpath -ItemType Directory
    }
}

$again = $true
while ($again) {
        $yourself = Read-Host "Name yourself or date? [y/d] "
        if($yourself -eq "y") {
            $name = Read-Host "Name of Backup "
            $again = $false
        } elseif($yourself -eq "d") {
            $name = Get-Date -Format "dd-MM-yyyy HH-mm-ss"
            write-host $name
            $again = $false
        } else {
            Write-Warning "Please enter 'd' or 'y' "
        }
}


#load paths from txt
$txt = Get-Content -Path $config

$startpath = $txt[0]
$destpath = $txt[1]


if($type -eq "full") {
    [System.Windows.Forms.MessageBox]::Show("You have backed up successfully! ", [System.Windows.Forms.MessageBoxButtons]::Cancel)
} 
else {
    Write-Warning "Error"
    [System.Windows.Forms.MessageBox]::Show("There was an Error while backing up, Please try again. ", [System.Windows.Forms.MessageBoxButtons]::Cancel)
    Break ''
}

$zipfolder = $destpath + "\" + $name + ".zip"

# copy folder to destination
Compress-Archive $startpath -DestinationPath $zipfolder -CompressionLevel Fastest -Force