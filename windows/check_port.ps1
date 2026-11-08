
param(
    [Parameter(Mandatory = $true)]
    [int]$Port,

    [string]$HostName = "127.0.0.1"
)

if ($Port -lt 1 -or $Port -gt 65535) {
    Write-Output "ERROR: Invalid port"
    exit 2
}

$client = New-Object System.Net.Sockets.TcpClient

try {
    $asyncResult = $client.BeginConnect(
        $HostName,
        $Port,
        $null,
        $null
    )

    $connected = $asyncResult.AsyncWaitHandle.WaitOne(3000, $false)

    if ($connected) {
        $client.EndConnect($asyncResult)
        Write-Output "OPEN: ${HostName}:$Port"
        exit 0
    }
    else {
        Write-Output "CLOSED: ${HostName}:$Port"
        exit 1
    }
}
catch {
    Write-Output "CLOSED: ${HostName}:$Port"
    exit 1
}
finally {
    $client.Close()
}
