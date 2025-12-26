from analyzer.indicators import SUSPICIOUS_KEYWORDS
import os

def analyze_log(file_path):
    """
    Analyze log file for suspicious keywords.
    
    Args:
        file_path: Path to the log file to analyze
        
    Returns:
        List of suspicious log entries found
    """
    findings = []
    
    # Check if file exists
    if not os.path.exists(file_path):
        return findings
    
    try:
        with open(file_path, "r", errors="ignore") as f:
            for line in f:
                for word in SUSPICIOUS_KEYWORDS:
                    if word.lower() in line.lower():
                        findings.append(line.strip())
                        break
    except (IOError, OSError) as e:
        # Return empty findings if file can't be read
        return findings
    
    return findings
