rule Suspicious_Keywords
{
    strings:
        $cmd1 = "powershell"
        $cmd2 = "cmd.exe"
        $cmd3 = "wget"
        $cmd4 = "curl"
    condition:
        any of them
}
