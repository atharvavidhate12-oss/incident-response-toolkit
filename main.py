from collector.system_info import collect_system_info
from collector.process_info import collect_processes
from collector.network_info import collect_network
from collector.memory_artifacts import collect_memory_artifacts
from analyzer.log_analyzer import analyze_log
from analyzer.yara_scanner import scan_with_yara
from analyzer.mitre_mapper import map_to_mitre
from report.report_generator import generate_report
from datetime import datetime
import json
import os

log_findings = analyze_log("sample.log")

data = {
    "system": collect_system_info(),
    "processes": collect_processes(),
    "network": collect_network(),
    "memory": collect_memory_artifacts(),
    "log_findings": log_findings,
    "yara": scan_with_yara("."),
    "mitre": map_to_mitre(log_findings)
}

# Ensure directory exists before writing
os.makedirs("data/analysis", exist_ok=True)
with open("data/analysis/results.json", "w") as f:
    json.dump(data, f, indent=2)

report = generate_report(data)
with open("IR_Report.txt", "w") as f:
    f.write(report)

print("SOC-Level Incident Response Completed")
