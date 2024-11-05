$date = get-date -format "dd-MM-yyyy"
$user = [System.Environment]::UserName

Write-Output "it's $date and the user is $user"