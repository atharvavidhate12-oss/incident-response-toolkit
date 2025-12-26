from datetime import datetime
import json

def generate_report(data):
    report = f"""
INCIDENT RESPONSE REPORT
========================
Date: {datetime.now()}

--- SYSTEM INFO ---
{json.dumps(data['system'], indent=2)}

--- PROCESSES ---
Total: {len(data['processes'])}

--- NETWORK CONNECTIONS ---
Total: {len(data['network'])}

--- LOG FINDINGS ---
{len(data['log_findings'])} suspicious entries found

--- RECOMMENDATION ---
• Investigate suspicious processes
• Block malicious IPs
• Preserve disk images
"""
    return report
