🛡️ Cross-Platform Incident Response Toolkit (SOC Edition)

A professional, SOC-level Incident Response Toolkit built in Python for cross-platform forensic triage and incident analysis.
This toolkit simulates real-world Blue Team / DFIR workflows including artifact collection, log analysis, malware detection, MITRE ATT&CK mapping, SIEM-ready outputs, and reporting.

🚀 Features
🔍 Artifact Collection

System information (OS, hostname, architecture)

Running processes

Active network connections

Memory usage & high-memory processes

File hashing for integrity verification

📊 Log Analysis

Suspicious keyword detection

Security event extraction

IOC-based pattern matching

🦠 Malware Detection

YARA rule scanning

Detection of suspicious binaries and scripts

🧠 Threat Intelligence

MITRE ATT&CK technique mapping

Identification of adversary behavior patterns

☁️ SIEM Integration

JSON event output

Ready for ingestion into ELK, Splunk, Sentinel (simulation)

📄 Reporting

Automated Incident Response report

SOC-style recommendations

Investigation summary

🌐 Dashboard

Flask-based HTML dashboard

Visual inspection of findings

🏗️ Project Architecture
ir_toolkit/
│
├── collector/          # Artifact collection modules
├── analyzer/           # Log, YARA, MITRE analysis
├── dashboard/          # Web dashboard (Flask)
├── report/             # Report generation
├── yara_rules/         # YARA detection rules
├── data/
│   ├── collected/
│   ├── analysis/
│   ├── siem/
│
├── main.py
├── requirements.txt
└── README.md

⚙️ Installation
1️⃣ Clone the repository
git clone https://github.com/atharvavidhate12-oss/incident-response-toolkit.git
cd incident-response-toolkit

2️⃣ Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows

3️⃣ Install dependencies
pip install -r requirements.txt

▶️ Usage
Run Incident Response Workflow
python main.py

Outputs Generated

IR_Report.txt — Incident Response report

data/analysis/results.json — Analysis results

data/siem/event.json — SIEM-ready event

Launch SOC Dashboard
python dashboard/app.py


Open browser:

http://127.0.0.1:5000

📌 Use Cases

SOC Analyst training

DFIR practice

Incident triage simulation

Cybersecurity portfolio project

Blue Team skill demonstration

⚠️ Disclaimer

This project is intended for educational and defensive security purposes only.
Do NOT use this toolkit on systems without proper authorization.

📈 Future Enhancements

Sigma rule support

Timeline reconstruction

IOC enrichment

Threat scoring engine

Full memory forensics integration

👤 Author

Atharva Vidhate
GitHub: atharvavidhate12-oss