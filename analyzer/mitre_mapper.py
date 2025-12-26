MITRE_MAPPING = {
    "powershell": "T1059.001 – PowerShell",
    "cmd.exe": "T1059.003 – Command Shell",
    "failed login": "T1110 – Brute Force",
    "unauthorized": "T1078 – Valid Accounts",
    "sql": "T1190 – Exploit Public-Facing App"
}

def map_to_mitre(findings):
    mapped = []
    for line in findings:
        for key, tactic in MITRE_MAPPING.items():
            if key in line.lower():
                mapped.append({"indicator": line, "technique": tactic})
    return mapped
